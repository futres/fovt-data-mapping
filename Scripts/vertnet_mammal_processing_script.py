"""
Data Wrangling Script for VertNet Mammal Data

Neeka Sewnath
nsewnath@ufl.edu

"""

#===========================================================================================================================================

import pandas as pd
import argparse 
import numpy as np
import multiprocessing
import re
import uuid 

#===========================================================================================================================================

try:
    import warnings
    warnings.filterwarnings('ignore')
except:
    pass

#===========================================================================================================================================

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='API data scrape and reformat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help = 'File input',
                        metavar = 'url',
                        type = str,
                        default = "./../Original_Data/all_mammals_2021-11-09a/all_mammals_2021-11-09a.csv")

    parser.add_argument('-o',
                        '--output',
                        help = 'Output file name',
                        metavar = 'output',
                        type = str)

    return parser.parse_args()

#===========================================================================================================================================

date_filter = """IV|0000|September|<|NW|latter|unknown|(MCZ)|(MSU)|present|
                 and|;|&|mainly|between|Between|BETWEEN|OR|Unknown|UNKNOWN|
                 #|TO|\?|\'|----|19--|No Date|\,|\d{4}-\d{4}|(/n) /d|\d{4}[s]|
                 \d{4}\'[S]|1075-07-29|975-07-17|2088|9999|0201|1197|
                 1260|4560|1024|1119|1192|1072|1186|2364"""


# TODO: Turn into mapping file 
country_dictionary = {"United States":"USA", "U S A":"USA", 
                      "Philippine Islands":"Philippines",
                      "Indonesia; Borneo":"Indonesia",
                      "Malaysia; Malaya":"Malaysia",
                      "U.S. Virgin Islands":"Virgin Islands",
                      "Republic of South Africa":"South Africa",
                      "Ivory Coast":"Cote d'Ivoire",
                      "Federated States of Micronesia":"Micronesia",
                      "Lesser Antilles; Grenada":"Grenada",
                      "Indonesia; Java":"Indonesia",
                      "Lesser Antilles; Saint Vincent":"Saint Vincent and the Grenadines",
                      "Lesser Antilles; Barbados":"Barbados",
                      "ST VINCENT":"Saint Vincent and the Grenadines",
                      "Lesser Antilles; Montserrat": "Montserrat",
                      "Indonesia; Sumatra":"Indonesia",
                      "Virgin Islands, US":"Virgin Islands",
                      "Lesser Antilles; Antigua":"Antigua and Barbuda",
                      "England":"United Kingdom",
                      "Republic of Trinidad and Tobago":"Trinidad and Tobago",
                      "Trinidad And Tobago; Trinidad":"Trinidad and Tobago",
                      "COMMONWEALTH OF THE NORTHERN MARIANA ISLANDS":"Northern Mariana Islands",
                      "Congo":"Democratic Republic of the Congo",
                      "Malaysia; Sabah":"Malaysia",
                      "Lesser Antilles; Martinique":"Martinique",
                      "Republic of the Marshall Islands":"Marshall Islands",
                      "Commonwealth of the Bahamas":"Bahamas",
                      "Trinidad & Tabago":"Trinidad and Tobago",
                      "United Kingdom; England":"United Kingdom",
                      "United Kingdom; Scotland":"United Kingdom",
                      "United Kingdom; Wales":"United Kingdom",
                      "Lesser Antilles; Dominica":"Dominica",
                      "Papua, New Guinea":"Papua New Guinea",
                      "People's Republic of China":"China",
                      "SCOTLAND":"United Kingdom"}

desired_columns = ['catalognumber','collectioncode','decimallatitude','individualID',
                  'decimallongitude', 'verbatimElevation', 'maximumelevationinmeters',
                  'minimumelevationinmeters','institutioncode','verbatimEventDate',
                  'occurrenceremarks','occurrenceid','verbatimlongitude',
                  'verbatimlatitude', 'verbatimLocality', 'samplingProtocol',
                  'sex', 'country', 'lifestage_cor', 'binomial', 'basisOfRecord',
                  'yearCollected', 'body_mass.value','body_mass.units',
                  'ear_length.value', 'ear_length.units','hind_foot_length.value',
                  'hind_foot_length.units', 'tail_length.value','tail_length.units',
                  'total_length.value', 'total_length.units','body_mass.units_inferred',
                  'ear_length.units_inferred', 'hind_foot_length.units_inferred',
                  'tail_length.units_inferred','total_length.units_inferred',
                  'body_mass.estimated_value','ear_length.estimated_value',
                  'hind_foot_length.estimated_value','tail_length.estimated_value',
                  'total_length.estimated_value']

rename_dict = {'catalognumber': 'catalogNumber',
               'collectioncode':'collectionCode',
               'decimallatitude':'decimalLatitude',
               'decimallongitude':'decimalLongitude',
               'institutioncode' :'institutionCode',
               'occurrenceremarks':'occurrenceRemarks',
               'maximumelevationinmeters':'maximumElevationInMeters',
               'minimumelevationinmeters':'minimumElevationInMeters',
               'occurrenceid':'occurrenceID',
               'verbatimlongitude':'verbatimLongitude',
               'verbatimlatitude':'verbatimLatitude',
               'lifestage_cor':'lifeStage',
               'binomial':'scientificName'}
#===========================================================================================================================================

def assign_indivdual_ID(data):
    """
    Add individualID and populate with UUID
    
    """
    data = data.assign(individualID = '')
    data['individualID'] = [uuid.uuid4().hex for _ in range(len(data.index))]

    return data

def year_search(year):
    """
    Search string for 4 digit number and pass to correct function

    """
    if (re.search(r'\d{4}$', year)):
        return year_cleaner_front(year)
    elif (re.search(r'^\d{4}', year)):
        return year_cleaner_back(year)

def year_cleaner_front(year):
    """
    Isolate the year at the beginning of the string

    """
    cleaned_year = year[len(year)-4:len(year)]
    return cleaned_year

def year_cleaner_back(year):
    """
    Isolate the year at the end of the string

    """
    cleaned_year = year[0:4]
    return cleaned_year

def clean_year_collected(data):
    """
    Clean yearCollected column

    """

    # Filling N/As with "Unknown"
    data["eventdate"] = data["eventdate"].fillna("Unknown")

    # Create yearCollected Column
    data = data.assign(yearCollected = '')

    # Creating event date variable
    verbatim_date = data['eventdate']

    # Establishing vertnet filter
    vertnet_date_filter = verbatim_date.str.contains(date_filter)

    # Grabbing clean data
    verbatim_date_clean= verbatim_date[vertnet_date_filter==False]

    # Cleaning year data
    data["yearCollected"] = verbatim_date_clean.apply(year_search)
    data["yearCollected"] = data["yearCollected"].fillna("Unknown")

    return data

def clean_lifestage_column(data):
    """
    Clean lifestage column 

    """
    # Fill in NA
    data["lifestage_cor"] = data['lifestage_cor'].fillna("Not Collected")

    # Create Filters
    adult = data['lifestage_cor'] == "Adult"
    juvenile = data['lifestage_cor'] == "Juvenile"
    ns = data['lifestage_cor'] == "NS"

    # Assign correct terms using filters
    data['lifestage_cor'][adult] = "adult"
    data['lifestage_cor'][juvenile] = "juvenile"
    data['lifestage_cor'][ns] = "Not Collected"

    return data 

def clean_sex_column(data):
    """
    Clean sex column
    
    """

    female = data['sex'] == "female"
    male = data['sex'] == "male"
    data['sex'][(female == False) & (male == False)] = ""

    return data

def fill_unknown(data):
    """
    Fill scientificName data with "unknown"

    """
    data["binomial"] = data["binomial"].fillna("Unknown")

    return data 

def add_req_cols(data):
    """
    Add required GEOME columns
    
    """

    data["samplingProtocol"] = "Unknown"
    data["basisOfRecord"] = "PreservedSpecimen"
    data["locality"] = "Unknown"

    return data 

def adding_verbatim_date(data):
    """
    Adding verbatimEventDate column to dataframe

    """

    data['verbatimEventDate'] = data['verbatimeventdate']

    return data

def country_correction(country): 
    """Corrects country column to geome specific country list"""

    # Read GEOME country list
    geome_countries = pd.read_csv("./../Mapping Files/geome_country_list.csv")

    if country in geome_countries.values:
        return country
    elif country in country_dictionary.keys():
        return country_dictionary[country]
    else:
        country = "Unknown"
        return country 

def clean_country(data):
    """
    Cleaning country column 
    
    """
    # Append countries to verbatim locality column
    data["verbatimLocality"] = data["locality"] + "," + data["country"]

    # Clean country names
    data['country'] = data['country'].apply(country_correction)

    return data

def verbatim_elev(data):
    """
    Create verbatimElevation columns

    """
    string_max = data["maximumelevationinmeters"].astype(str)
    string_min = data["minimumelevationinmeters"].astype(str)
    data['verbatimElevation'] = string_max + "," + string_min

    return data

def col_rearrange(data):
    """
    Rearrange columns so that template columns are first, followed by measurement values

    """

    # Create column list
    cols = data.columns.tolist()

    # Specify desired columns
    cols = desired_columns

    # Subset dataframe
    data = data[cols]

    return data 

def match_cols(data):
    """
    Matching template and column terms

    """
    
    data = data.rename(rename_dict)

    return data

def create_id(data):
    """
    Create materialSampleID which is a UUID for each measurement, 
    Create eventID and populate it with materialSampleID
    
    """

    data['materialSampleID'] = [uuid.uuid4().hex for _ in range(len(data.index))]
    data["eventID"] = data['materialSampleID']

    return data


#===========================================================================================================================================


def main():

    # Fetch arguments 
    args = get_args()
    file = args.file

    # Read input file 
    print("\n Reading in data...")
    data = pd.read_csv(file)

    # Assign individualID
    print("\n Assigning individualID...")
    data = assign_indivdual_ID(data)

    # Clean yearCollected column
    print("\n Cleaning yearCollected column...")
    data = clean_year_collected(data)

    # Clean lifeStage column
    print("\n Cleaning lifeStage column...")
    data = clean_lifestage_column(data)

    # Clean sex column
    print("\n Cleaning sex column...")
    data = clean_sex_column(data)

    # Cleaning scientificName column
    print("\n Cleaning scientificName column...")
    data = fill_unknown(data)

    # Adding required GEOME columns
    print("\n Adding GEOME required column...")
    data = add_req_cols(data)

    # Adding verbatimEventDate column
    print("\n Adding verbatimEventDate column...")
    data = adding_verbatim_date(data)

    # Clean up country column 
    print("\n Cleaning country column...")
    data = clean_country(data)

    # Create verbatimElevation columns
    print("\n Creating verbatimElevation columns...")
    data = verbatim_elev(data)

    # Matching column names with template names
    print("\n Matching column names with template names...")
    data = match_cols(data)

    # Create materialSampleID and eventID
    print("\n Creating materialSampleID...")
    data = create_id(data)

    #TODO: sort of the measurementmethod stuff

#===========================================================================================================================================

if __name__ == '__main__':
    main()
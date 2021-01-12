#!/usr/bin/env python3
"""
Author:  Neeka Sewnath <nsewnath@ufl.edu>
Purpose: Clean Cougar Data (RShiny py functions example)
"""

import argparse
import numpy as np

def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='File Input for conversion test',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='str',
                        type=argparse.FileType('r'),
                        default='test_data.csv')

    return parser.parse_args()

def clean_sex(sex, ind):
    """cleans sex column in dataset"""
    #can catch incorrect information, needs testing

    #TODO: run a preliminary match, catch "female" and "male", count it up 

    if sex.str.contains("female|F|mujeres"):
        sex = "female"
    elif sex.str.contains("male|M|hombres"):
        sex = "male"
    else:
        print(ind)
        print(sex)
        sex = "not collected"
        #TODO: print(number  changed)
    return sex

def clean_side(side, ind):
    """cleans side column in dataset"""
    #can catch incorrect information, needs testing
    if side.str.contains("R|right|D|derecha"):
        side = "right"
    elif side.str.contains("L|left|I|izquierda"):
        side = "left"
    else:
        print(ind)
        print(side)
        side = "not collected"
        #TODO: print(number  changed)
    return side

def clean_year(year):
    """isolates year in dataset"""
    #only works if year is in XX-XXXX or XX-XX-XXXX format
    #TODO: account for year at beginning 
    year = year.str[-4:]
    #TODO: catch bad years
    return year

def scientific_name(name):
    """dictates scientific name"""
    #sometimes scientific name is not included
    #TODO: catch double capital?
    #TODO: catch one word lowercase
    #TODO: catch weird characters
    #TODO: look at john's example
    name = ""
    return name

def clean_up(data):
    """runs clean up function suite, keeps main clean"""
    data['sex'] = data.apply(lambda x: clean_sex(x.sex, x.ind), axis=1)
    data['side'] = data.apply(lambda x: clean_side(x.side, x.ind), axis=1)
    data["yearCollected"] = data["yearCollected"].apply(clean_year)
    data["scientificName"] = data["scientificName"].apply(scientific_name)
    return data

#def column_correct(data,column_name_dict):
    """corrects column name"""

    #Establish column dictionary
    #column_name_dict = {}
#    column_name_dict["sex"]  = ["Sex","Gender","gender"]
#    column_name_dict["side"] = ["Side"]
#    column_name_dict["yearCollected"] = ["Year", "Date", "date"]
#    column_name_dict["scientificName"] = ["Scientific Name", "taxon","name","Name"]

    #for column in data:
    #    if column in column_name_dict.values:
    #        return column
    #    elif column in column_name_dict.keys():
    #        column = column_name_dict[column]
    #        return column 
    #    else:
    #        print("Error! Column unknown")
            #TODO: prompt user for correct input, modify dictionary 
            #what did you mean by "column"? Does it match any of ours?


#TODO add country function, match to geome country list, print out discrepencies
def country_correct(country):
    #put this somewhere else
    geome_countries = pd.read_csv("./../../Mapping Files/geome_country_list.csv")


#TODO checking discrepencies in lat and long values using country quadrants (flag it)


# --------------------------------------------------
def main():
    """Read file and initiate clean up process"""
    
args = get_args()
data = args

# Fix column names
# column_correct(data,column_name_dict)

# Adds index column to data
data['ind'] = np.arange(1, data.shape[0] + 1)

# Passes data to cleaning functions
clean_up(data)

#TODO outfile creation for run log (csv file)

# --------------------------------------------------
if __name__ == '__main__':
    main()

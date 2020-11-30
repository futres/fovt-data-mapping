#!/usr/bin/env python3
"""
Author:  Neeka Sewnath <nsewnath@ufl.edu>
Purpose: Clean Cougar Data (RShiny py functions example)
"""

import argparse

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
                        default='./../../Original  Data/cougar_data.csv')

    return parser.parse_args()

def clean_sex(sex):
    """cleans sex column in dataset"""
    #can catch incorrect information, needs testing
    if sex.str.contains("female|F"):
        sex = "female"
    elif sex.str.contains("male|M"):
        sex = "male"
    else:
        sex = "not collected"
    return sex

def clean_year(year):
    """isolates year in dataset"""
    #only works if year is in XX-XXXX or XX-XX-XXXX format
    year = year.str[-4:]
    return year

def scientific_name(name):
    """dictates scientific name"""
    #sometimes scientific name is not included
    name = ""
    return name

def clean_up(data):
    """runs clean up function suite, keeps main clean"""
    data["sex"] = data["sex"].apply(clean_sex)
    data["yearCollected"] = data["yearCollected"].apply(clean_year)
    data["scientificName"] = data["scientificName"].apply(scientific_name)

#adding a universal country handler would be useful
#checking discrepencies in lat and long values would be useful



# --------------------------------------------------
def main():
    """Read file and clean sex column"""
    
args = get_args()
data = args

#need a way to standardize column names before clean up functions
#do we want to rename columns with regex?
#needs to also initalize columns such as diagnostic ID


clean_up(data)

# --------------------------------------------------
if __name__ == '__main__':
    main()

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
                        default='./../../Original  Data/cougar_data.csv')

    return parser.parse_args()

def clean_sex(sex, ind):
    """cleans sex column in dataset"""
    #can catch incorrect information, needs testing
    if sex.str.contains("female|F|mujeres|"):
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
    year = year.str[-4:]
    return year

def scientific_name(name):
    """dictates scientific name"""
    #sometimes scientific name is not included
    name = ""
    return name


def clean_up(data):
    """runs clean up function suite, keeps main clean"""
    data['sex'] = data.apply(lambda x: clean_sex(x.sex, x.ind), axis=1)
    data['side'] = data.apply(lambda x: clean_side(x.side, x.ind), axis=1)
    data["yearCollected"] = data["yearCollected"].apply(clean_year)
    data["scientificName"] = data["scientificName"].apply(scientific_name)
    return data


#TODO add country function, match to geome country list, print out discrepencies

#TODO checking discrepencies in lat and long values using country quadrants (flag it)


# --------------------------------------------------
def main():
    """Read file and initiate clean up process"""
    
args = get_args()
data = args

#TODO create dummy file for testing

#TODO develop python dictionary for  columns, taking in user input to  create
#dynamic  dictionary 

#TODO outfile creation for run log (csv file)

# Adds index column to data
data['ind'] = np.arange(len(data))

# Passes data to cleaning functions
clean_up(data)

# --------------------------------------------------
if __name__ == '__main__':
    main()

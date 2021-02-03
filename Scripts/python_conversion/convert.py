
""" Data Wrangler Automation """
""" Author: Neeka Sewnath """

import sys
import os
import pandas as pd

def clean_sex(sex):
    """cleans sex column in dataset"""
    #can catch incorrect information, needs testing

    print(sex)
    if sex.contains("female|F|mujeres"):
        sex = "female"
        print("I think it worked")


        
   # elif sex.str.contains("male|M|hombres"):
   #     sex = "male"
   # else:
   #     print(sex)
   #     sex = "not collected"
   #     #TODO: print(number  changed)
   # return sex

def clean_up(data):
    """runs clean up function suite, keeps main clean"""
    data["SEX"].apply(clean_sex)

# --------------------------------------------------
def main():

    # Read new data
    ifile = open(sys.argv[1], 'rb')
    data = pd.read_csv(ifile)
    
    # Initate clean up sequence
    clean_up(data)


# --------------------------------------------------
if __name__ == '__main__':
    main()
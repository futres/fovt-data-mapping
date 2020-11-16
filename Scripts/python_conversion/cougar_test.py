#!/usr/bin/env python3
"""
Author:  Neeka Sewnath <nsewnath@ufl.edu>
Purpose: Clean Cougar Data
"""
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

# --------------------------------------------------
def main():
    """Read file and clean sex column"""
    
args = get_args()
female = data['Sex']=="F"
male = data['Sex'] == "M"
data['Sex'][(female == False)&(male==False)]="not collected"
data['Sex'][female == True]="female"
data['Sex'][male == True]="male"

return data

# --------------------------------------------------
if __name__ == '__main__':
    main()

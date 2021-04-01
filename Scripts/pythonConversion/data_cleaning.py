# Functions for Data Clean UP
# Prasiddhi Gyawali & Meghan Balk
# prasiddhi@email.arizona.edu; balkm@email.arizona.edu

import pandas as pd
import re
import json

# import courgar data directly from github
coug_data = pd.read_csv(r'/Users/prasiddhigyawali/Downloads/KEYS APP DEMO/cougar_data.csv')

print(coug_data)

# delete empty columns
#coug_data.dropna(how = 'all', axis = 'columns', inplace = True)
# delete empty rows
#coug_data.dropna(how = 'all', axis = 'rows', inplace = True)


# combines Management Unit and County columns to make verbatimLocality
coug_data = coug_data.assign(verbatimLocality = coug_data['Management Unit'] + ', ' + coug_data['County'])

def matSampType():
    # more description to status column -- in connection with GENOME
    whole = coug_data['Status'].str.contains('A', case=False)
    gutted = coug_data['Status'].str.contains('B', case=False)
    skinned = coug_data['Status'].str.contains('C', case=False)

    coug_data['Status'][whole == True] = "whole organism"
    coug_data['Status'][gutted == True] = "part organism"
    coug_data['Status'][skinned == True] = "part organism"

# create yearCollected column & populate
coug_data = coug_data.rename(columns = {"Date":"yearCollected", 'Status':'materialSampleType'})

# sex column: F --> female & M --> male && 

preCln = json.loads(coug_data['Sex'].value_counts().to_json())

# counts values pre-cleaning
# changes 
female = coug_data['Sex'].str.contains('F', case=False)
male = coug_data['Sex'].str.contains('M', case=False)
coug_data['Sex'][(female == False)&(male==False)] = "not collected"
coug_data['Sex'][female == True]= "female"
coug_data['Sex'][male == True]= "male"
# counts values post cleaning

#postCln = json.loads(coug_data['Sex'].value_counts().to_json())

def inandp_conv(): 
    # converting weight and length from inches to mm & pounds to grams
    coug_data['Length'] = coug_data['Length'] * 25.4
    coug_data['Weight'] = coug_data['Weight'] * 453.59237


# deletes Management Unit, County, and Date columns
coug_data = coug_data.drop(columns=['Management Unit', 'County'])

# prints dataset
print(coug_data)
print(preCln)
#print(postCln)

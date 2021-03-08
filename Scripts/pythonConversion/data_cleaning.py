# Functions for Data Clean UP
# Prasiddhi Gyawali & Meghan Balk
# prasiddhi@email.arizona.edu; balkm@email.arizona.edu

import pandas as pd

# import courgar data directly from github
coug_data = pd.read_csv("https://de.cyverse.org/dl/d/F2088922-D273-49AE-985F-8D55966627A9/1987to2019_Cougar_Weight_Length_Public_Request.csv")

# delete empty columns
coug_data.dropna(how = 'all', axis = 'columns', inplace = True)
# delete empty rows
coug_data.dropna(how = 'all', axis = 'rows', inplace = True)


# combines Management Unit and County columns to make verbatimLocality
coug_data = coug_data.assign(verbatimLocality = coug_data['Management Unit'] + ', ' + coug_data['County'])

# more description to status column -- in connection with GENOME
whole = coug_data['Status'].str.contains('A', case=False)
gutted = coug_data['Status'].str.contains('B', case=False)
skinned = coug_data['Status'].str.contains('C', case=False)

coug_data['Status'][whole == True] = "whole organism"
coug_data['Status'][gutted == True] = "part organism"
coug_data['Status'][skinned == True] = "part organism"

'''
# DOESNT WORK

# create yearCollected column
coug_data = coug_data.assign(yearCollected = "")
# condition
check = coug_data['Date'].str.contains('/')
# populate yearCollected column
for i in range(len(coug_data['Date'])):
    if coug_data['Date'].str.contains('/'):
        if int(coug_data['Date'].str[-2:]) > 21:
            coug_data['yearCollected'] = "19" + coug_data['Date'].str[-2:]
        else:
            coug_data['yearCollected'] = "20" + coug_data['Date'].str[-2:]
    else:
        coug_data['yearCollected'] = coug_data['Date'].str[-4:]

'''

# deletes Management Unit, County, and Date columns
coug_data = coug_data.drop(columns=['Management Unit', 'County', 'Date'])


# prints dataset
print(coug_data)
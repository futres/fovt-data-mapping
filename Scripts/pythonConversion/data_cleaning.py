# Functions for Data Clean UP
# Prasiddhi Gyawali & Meghan Balk & Neeka Sewnath
# prasiddhi@email.arizona.edu; balkm@email.arizona.edu; nsewnath@ufl.edu

import pandas as pd
import re
import json

# import courgar data directly from desktop
df = pd.read_csv(r'/Users/prasiddhigyawali/Downloads/coug_data.csv')

# asking what the units of the weight values are
print("This program accepts: ""pounds"", ""kilograms"", ""milligrams"", and ""grams"".")
wght = input("What units are the weight values in? ")

while True:
    if wght == "pounds" or wght == "kilomgrams" or wght == "milligrams" or wght == "grams":
        break
    print("Sorry! That is not an accepted weight unit.")
    print("This program accepts: ""pounds"", ""kilograms"", ""milligrams"", and ""grams"".")
    wght = input("What units are the weight values in? ")

# asking what the units of the length values are
print("This program accepts: ""inches"", ""centimeters"", ""meters"", and ""millimeters"".")
lngth = input("What units are the length values in? ")


while True:
    if lngth == "inches" or lngth == "centimeters" or lngth == "meters" or lngth == "millimeters":
        break
    print("Sorry! That is not an accepted length unit.")
    print("This program accepts: ""inches"", ""centimeters"", ""meters"", and ""millimeters"".")
    lngth = input("What units are the length values in? ")

## PRE-CLEANING

# delete empty columns
df.dropna(how = 'all', axis = 'columns', inplace = True)
# delete empty rows
df.dropna(how = 'all', axis = 'rows', inplace = True)

## DATA STANDARDIZAION

def verLocal(df): 
    # combines Management Unit and County columns to make verbatimLocality
    df = df.assign(verbatimLocality = df['Management Unit'] + ', ' + df['County'])
    # deletes management unity and county columns
    df = df.drop(columns=['Management Unit', 'County'])
    return df

def matSampType(df):
    # more description to status column -- in connection with GENOME
    whole = df['Status'].eq("A", "a")
    gutted = df['Status'].eq("B", "b")
    skinned = df['Status'].eq("C", "c")

    df['Status'][whole == True] = "whole organism"
    df['Status'][gutted == True] = "part organism"
    df['Status'][skinned == True] = "part organism"
    return df

def sex(df):
    # sex column: F --> female & M --> male && 

    # changes values
    female = df['Sex'].eq("F", "f")
    male = df['Sex'].eq("M", "m")
    df['Sex'][(female == False)&(male==False)] = "not collected"
    df['Sex'][female == True] = "female"
    df['Sex'][male == True] = "male"
    return df

def inConv(df):
    # converting length from inches to millimeters
    df['Length'] = df['Length'] * 25.4
    return df

def lbsConv(df):
    # converting weight from pounds to grams
    df['Weight'] = df['Weight'] * 453.59237
    return df

def cmConv(df):
    # converting length from cenitmeters to millimeters
    df['Length'] = df['Length'] * 10
    return df

def kgConv(df):
    # converting weight from kilograms to grams
    df['Weight'] = df['Weight'] * 1000
    return df

def mConv(df):
    # converting length from meters to millimeters
    df['Length'] = df['Length'] * 1000
    return df

def mgConv(df):
    # converting weight from milligrams to grams
    df['Weight'] = df['Weight'] / 1000
    return df

def dataMelt(df):
    df = pd.melt(df, id_vars = ['Date','Sex', 'Age', 'Status', 'verbatimLocality'], 
                    var_name = 'measurementType', value_name = 'measurementValue')
    return df

def yc(df):
    # create and populate yearCollected through the date column
    df = df.assign(yearCollected = df['Date'].str[:4])
    return df

def colRename(df):
    # renames columns through user input
    col_names = []
    for i in range(len(df.columns)):
        inpt = input("What would you like column " + str(i + 1) + " to be named?: ")
        col_names.append(inpt)
    df.columns = col_names
    return df

def callAll(df):
    df = verLocal(df)
    df = matSampType(df)
    df = sex(df)
    df = dataMelt(df)
    df = yc(df)
    return df

df = callAll(df)

# applying weight converstion functions in accordance to inputed unit
if wght == "pounds":
    df = lbsConv(df)
elif wght == "kilograms":
    df = kgConv(df)
elif wght == " milligrams":
    df = mgConv(df)

# applying length converstion functions in accordance to inputed unit
if lngth == "inches":
    df = inConv(df)
elif lngth == "centimeters":
    df = cmConv(df)
elif lngth == " meters":
    df = mConv(df)

# print data frame as it is right now
print("This is your current data frame: ")
print(df)

# asks user if they want to change column names
choice = input("Would you like to change the column names? (Enter ""Yes"" or ""No""): ")

# if yes runs colRename function
if choice == "Yes":
    colRename(df)
    print("Your finalized data frame: ")
    print(df)
else:
    # if not prints data frame once again as it is
    print("Your finalized data frame: ")
    print(df)
# Functions for Data Clean UP
# Prasiddhi Gyawali & Meghan Balk
# prasiddhi@email.arizona.edu; balkm@email.arizona.edu

import pandas as pd
import re
import json


# import courgar data directly from github
df = pd.read_csv(r'/Users/prasiddhigyawali/Downloads/coug_data.csv')

## PRE-CLEANING

# delete empty columns
df.dropna(how = 'all', axis = 'columns', inplace = True)
# delete empty rows
df.dropna(how = 'all', axis = 'rows', inplace = True)

## DATA STANDARDIZAION

def verLocal(df): 
    # combines Management Unit and County columns to make verbatimLocality
    df = df.assign(verbatimLocality = df['Management Unit'] + ', ' + df['County'])
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

    # counts values pre-cleaning
    # changes 
    female = df['Sex'].eq("F", "f")
    male = df['Sex'].eq("M", "m")
    df['Sex'][(female == False)&(male==False)] = "not collected"
    df['Sex'][female == True] = "female"
    df['Sex'][male == True] = "male"
    return df


def in_and_p_conv(df):
    # converting weight and length from inches to mm & pounds to grams
    df['Length'] = df['Length'] * 25.4
    df['Weight'] = df['Weight'] * 453.59237
    return df

def yc(df):
    # create and populate yearCollected
    df = df.assign(yearCollected = df['Date'].str[:4])
    return df

def colRename(df):
    col_names = []
    for i in range(len(df.columns)):
        inpt = input("What would you like column " + str(i + 1) + " to be named?: ")
        col_names.append(inpt)
    df.columns = col_names
    return df


df = verLocal(df)
df = matSampType(df)
df = sex(df)
df = in_and_p_conv(df)
df = yc(df)

print("This is your current data frame: ")
print(df)

choice = input("Would you like to change the column names? (Enter ""Yes"" or ""No""): ")


if choice == "Yes":
    colRename(df)
    print("Your finalized data frame: ")
    print(df)
else:
    print("Your finalized data frame: ")
    print(df)

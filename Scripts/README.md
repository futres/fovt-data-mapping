Data Manipulation
```
R program that is used to clean up and standardize data sets. 

Since data is collected by all sorts of places using different languages and even units of measurement there is no universal standard for it. 
Having a program that sets it to a standard and even cleans it up can make it much easier to understand the data. 

```
For example: This is an excerpt from the cougar data set prior to data cleaning. There are empty columns with no data in them, the meaning of the status column is very hard to understand, and the values in the sex column are just initialied.
```
> head(cougar_data)
     Date Management.Unit    County Sex Age Status Weight Length  X X.1 X.2
1 5/19/87        Mt Emily  Umatilla   F   4      A    105     75 NA  NA  NA
2 8/12/87          Chetco     Curry   F   5      A     64     NA NA  NA  NA
3 9/21/87         Santiam Clackamas   M   2      A    116     76 NA  NA  NA
4 9/28/87          Chetco     Curry   F   3      A     74     70 NA  NA  NA
5 10/4/87        McKenzie      Lane   F   2      A     76     73 NA  NA  NA
6 11/1/87           Tioga      Coos   M   3      B     80     NA NA  NA  NA
```
This this the same data set after it has been run through the program. Unnecessary columns and rows have been removed, columns have been renamed, and values have been specified.

```
> head(cougar_data)
  yearCollected Management Unit    County    Sex Age Status measurementType measurementValue measurementUnit
1       5/19/87        Mt Emily  Umatilla female   4 Intact          Length               75              mm
2       9/21/87         Santiam Clackamas   male   2 Intact          Length               76              mm
3       9/28/87          Chetco     Curry female   3 Intact          Length               70              mm
4       10/4/87        McKenzie      Lane female   2 Intact          Length               73              mm
5      11/18/87       Applegate Josephine   male   2 Intact          Length               84              mm
6      11/21/87          Indigo      Lane   male   2 Intact          Length               84              mm
```

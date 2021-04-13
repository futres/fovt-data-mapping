<h2>Data Manipulation Python Conversions</h2>

Conversions of the perviouly made RShiny app used to convert tabular data with some newly added functions. 

Starting off, data sets tend to look like this:

```
            Date Management Unit     County Sex  Age Status  Weight  Length  Unnamed: 8  Unnamed: 9  Unnamed: 10
0        5/19/87        Mt Emily   Umatilla   F    4      A   105.0    75.0         NaN         NaN          NaN
1        8/12/87          Chetco      Curry   F    5      A    64.0     NaN         NaN         NaN          NaN
2        9/21/87         Santiam  Clackamas   M    2      A   116.0    76.0         NaN         NaN          NaN
3        9/28/87          Chetco      Curry   F    3      A    74.0    70.0         NaN         NaN          NaN
4        10/4/87        McKenzie       Lane   F    2      A    76.0    73.0         NaN         NaN          NaN
...          ...             ...        ...  ..  ...    ...     ...     ...         ...         ...          ...
7836   11/7/2019         Starkey      Union   F    0      A    25.0     NaN         NaN         NaN          NaN
7837   11/7/2019         Starkey      Union   M    0      A    28.0     NaN         NaN         NaN          NaN
7838   11/7/2019         Starkey      Union   M    0      A    28.0     NaN         NaN         NaN          NaN
7839  11/30/2019         Siuslaw       Lane   M    0      A    37.0    52.0         NaN         NaN          NaN
7840  11/30/2019         Siuslaw       Lane   M    0      A    43.0    58.0         NaN         NaN          NaN

```
However, with a couple of conversions, it can be transformed into something like this

```
            Date     Sex  Age materialSampleType       Weight  Length    verbatimLocality yearCollected
0     1987-05-19  female    4     whole organism  47627.19885  1905.0  Mt Emily, Umatilla          1987
1     1987-08-12  female    5     whole organism  29029.91168     NaN       Chetco, Curry          1987
2     1987-09-21    male    2     whole organism  52616.71492  1930.4  Santiam, Clackamas          1987
3     1987-09-28  female    3     whole organism  33565.83538  1778.0       Chetco, Curry          1987
4     1987-10-04  female    2     whole organism  34473.02012  1854.2      McKenzie, Lane          1987
...          ...     ...  ...                ...          ...     ...                 ...           ...
7836  2019-11-07  female    0     whole organism  11339.80925     NaN      Starkey, Union          2019
7837  2019-11-07    male    0     whole organism  12700.58636     NaN      Starkey, Union          2019
7838  2019-11-07    male    0     whole organism  12700.58636     NaN      Starkey, Union          2019
7839  2019-11-30    male    0     whole organism  16782.91769  1320.8       Siuslaw, Lane          2019
7840  2019-11-30    male    0     whole organism  19504.47191  1473.2       Siuslaw, Lane          2019

```
The functions offered by this program are limited at this time. However, datasets can still be cleaned and transformed 
using various functions found in the program.

To achive best results it is asked that all dates are set to a "year, month, day" format. To do this, follow these steps:

      1) Open up data in excel
      2) Select the column heading in which your date values are listed 
      3) Right click and select "Format Cells"
      4) Go to the "Date" category
      5) Select the "year-month-day" format and click "OK"

-----------------------------------------------------------------------------------------------------------------------

<h3>Functions</h3>

```
matSampType()
```
Function presented above allows for the transformation from vague descriptions like A, B, and C to descriptors that 
give more insight onto the dataset. 

```
sex()
```
The sex functions also provides for more description within datasets. It takes values like "F" and "M" and changes them 
into "female" and "male". This function also checks for values that it does not recognize and changes them into 
"not collected".

-----------------------------------------------------------------------------------------------------------------------

<h4>Unit Converstion Function: These allows for a universally understood format which increases accessibility of the data.</h4>

<h5>Users will be asked what units their weights and lengths are in the unedited version of their data.</h5>

```
inConv(df)
```
Function changes values presented in the length column with the inch unit to millimeters.

```
cmConv(df)
```
Changes values centimeter values in the length column to millimeters. 
```
mConv(df)
```
If values in the length column are in meters this function will change them to millimeters.

```
lbsConv(df)
```
Measurements in the weight column which are initially in pounds are changed to grams.
```
kgConv(df)
```
Kilogram to gram conversion for the weight column.
```
mgConv(df)
```
Conversion of milligrams to grams for the weight column. 

-----------------------------------------------------------------------------------------------------------------------

<h3>Changing Column Names</h3>

Once all other functions have been run the program will present the data set and ask users if they would like to change the name of the columns.

If the user says yes, the following function will be run:
```
colRename(df)
```
The function create an empty list and asks the user what they would like each table to be named, the user inputs are then appended to the created list.
The list is then used to change the column names.

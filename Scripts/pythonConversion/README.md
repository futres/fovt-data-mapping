<h2>Data Manipulation Python Conversions</h2>

Conversions of the perviouly made RShiny app used to convert tabular data with some newly added functions. 

Starting off, data sets tend to look like this:

```
      Date Management Unit     County Sex  Age Status  Weight  Length
0     1987        Mt Emily   Umatilla   F    4      A   105.0    75.0
1     1987          Chetco      Curry   F    5      A    64.0     NaN
2     1987         Santiam  Clackamas   M    2      A   116.0    76.0
3     1987          Chetco      Curry   F    3      A    74.0    70.0
4     1987        McKenzie       Lane   F    2      A    76.0    73.0
...    ...             ...        ...  ..  ...    ...     ...     ...
7836  2019         Starkey      Union   F    0      A    25.0     NaN
7837  2019         Starkey      Union   M    0      A    28.0     NaN
7838  2019         Starkey      Union   M    0      A    28.0     NaN
7839  2019         Siuslaw       Lane   M    0      A    37.0    52.0
7840  2019         Siuslaw       Lane   M    0      A    43.0    58.0

```
However, with a couple of conversions, it can be transformed into something like this

```
      yearCollected     Sex  Age materialSampleType       Weight  Length    verbatimLocality
0              1987  female    4     whole organism  47627.19885  1905.0  Mt Emily, Umatilla
1              1987  female    5     whole organism  29029.91168     NaN       Chetco, Curry
2              1987    male    2     whole organism  52616.71492  1930.4  Santiam, Clackamas
3              1987  female    3     whole organism  33565.83538  1778.0       Chetco, Curry
4              1987  female    2     whole organism  34473.02012  1854.2      McKenzie, Lane
...             ...     ...  ...                ...          ...     ...                 ...
7836           2019  female    0     whole organism  11339.80925     NaN      Starkey, Union
7837           2019    male    0     whole organism  12700.58636     NaN      Starkey, Union
7838           2019    male    0     whole organism  12700.58636     NaN      Starkey, Union
7839           2019    male    0     whole organism  16782.91769  1320.8       Siuslaw, Lane
7840           2019    male    0     whole organism  19504.47191  1473.2       Siuslaw, Lane

```
The functions offered by this program are limited at this time. However, datasets can still be cleaned and transformed 
using various functions found in the program.

```
matSampType()
```
The function presented above allows for the transformation from vague descriptions like A, B, and C to descriptors that 
give more insight onto the dataset. 

```
sex()
```
The sex functions also provides for more description within datasets. It takes values like "F" and "M" and changes them 
into "female" and "male". This function also checks for values that it does not recognize and changes them into 
"not collected".

```
inandp_conv()
```
This function changes values presented with the inch unit to millimeters and values presented with the pount unit to
grams. This allows for a universally understood format which increases accessibility of the data. 

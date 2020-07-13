## cougar data set

## installed packages
library(tidyverse)
library(dplyr)
library(tibble)
library(anchors)
library(plyr)
library(reshape2)
library(janitor)


## updated set gets rid of columns w no data
cougar_template <- read.csv("https://raw.githubusercontent.com/futres/fovt-data-mapping/cougar_test/Mapping%20Files/column%20name%20template.csv")
cougar_data <- read.csv("https://de.cyverse.org/dl/d/F2088922-D273-49AE-985F-8D55966627A9/1987to2019_Cougar_Weight_Length_Public_Request.csv")
aepyceros_data <- read.csv("https://de.cyverse.org/dl/d/28031164-7903-4EC1-BA86-6441741BAB35/Extant_Aepyceros_database_updated_11_2016.csv", sep = ",", dec = " ")
aepyceros_template <- read.csv("https://raw.githubusercontent.com/futres/fovt-data-mapping/cougar_test/Mapping%20Files/trait%20mapping.csv", header = TRUE, stringsAsFactors = TRUE)


## delete empty rows and columns
delete_empty_r_and_c <- function(data){
  data <-data %>%
    mutate_all(funs(na_if("", " "))) %>% # if value of something in the data is blank then set it to NA
    remove_empty("cols") %>% # removes all NA cols
    remove_empty("rows") # removes all NA rows
  return(data)
}

## update status
status <- function(data, column, check, replace) 
{
  # data = dataframe
  # column = selected cloumn from dataframe
  # check = values already in data frame, vector created to check for these values
  # replace = what the values from the check vector are to be replaced with
  for(i in 1:length(check)) # i is incremented by 1, it starts at one and goes through how ever many values are in check
  {
    #data[,column][condition] <- replace[i]
    data[,column][data[,column] == check[i]] <- replace[i]
  }
  return(data)
}

#why did this function change?
#previous function:
#cougar_sex <- function(x, y)
#{
#  x[,y] <- gsub(pattern = "\\<f", replacement = "female", x[,y], ignore.case = TRUE)
#  x[,y] <- gsub(pattern = "\\<m", replacement = "male", x[,y], ignore.case = TRUE)
#  return(x)
#}

sex <- function(data, column)
{
  # data = dataframe
  # column = selected column from data frame
  x[,y] <- gsub(pattern = "\\<f", replacement = "female", x[,y], ignore.case = TRUE) # if values in the column starts w 'f' replace it with 'female'
  x[,y] <- gsub(pattern = "\\<m", replacement = "male", x[,y], ignore.case = TRUE) # if values in the column starts w 'r' replace it with 'male'
  return(data)
}

left_right <- function(data, column)
{
  # data = dataframe
  # column = selected column from data frame
  x[,y] <- gsub(pattern = "\\<l", replacement = "left", x[,y], ignore.case = TRUE) # if values in the column starts w 'l' replace it with 'left'
  x[,y] <- gsub(pattern = "\\<r", replacement = "right", x[,y], ignore.case = TRUE) # if values in the column starts w 'r' replace it with 'female'
}

repo_condition <- function(data, column, reproductive, non.reproductive)
{
  # data = dataframe
  # column = column where reproductive/non.reproductive data is being stored
  # reproductive = vector of things that are classified as reproductive
  # non.reproductive = vector of things that are classified as non-reproductive
  for(i in 1:length(reproductive)) # i is incremented by 1, it starts at one and goes through how ever many values are in reproductive
  {
    #data[,column][condition] <- "reproductive"
    data[,column][data[,column] == reproductive[i]] <- "reproductive"
  }
  for(i in 1:length(non.reproductive)) # i is incremented by 1, it starts at one and goes through how ever many values are in non.reproductive
  {
    #data[,column][condition] <- "non-reproductive"
    data[,column][data[,column] == non.reproductive[i]] <- "non-reproductive"
  }
}

life_stage <- function(data, adult, juvenile)
{
  # data = dataframe
  # adult = vector of all possible adult values
  # juvenile = vector of all possible juvenile values
  for(i in 1:length(adult)) # i is incremented by 1, it starts at one and goes through how ever many values are in adult
  {
    #data[,column][condition] <- juvenile[i]
    data[,column][data[,column] == adult[i]] <- juvenile[i]
  }
  return(data)
}
## melt data & filter empty values
melt_data <- function(data, col1, col2)
{
  # data = dataframe
  # col1 = first column we are melting
  # col2 = second column we are melting
  data <- melt(data, measure.vars = c(col1, col2))
  dplyr::filter(data, !is.na(value))
}

## add new column measuremnetUnit
add_col <- function(data)
{
  # data = dataframe
  add_column(data, measurementUnit = NA) #adds column called measureUnit where all of the values are NA
}
## populate measurementUnit
measurement_unit <- function(data, change, check)
{
  # data = dataframe
  # change = column name of values being changed
  # check = column name of values being checked
  data[,change] <- grepl(pattern = "\\<w", data[,check], ignore.case = TRUE) # if string starts w 'w' in check column values in change column are set to true if not they are set to false
  data[,change][data[,change] == TRUE] <- "g" # if value in change column is true replace it with 'g'
  data[,change][data[,change] == FALSE] <- "mm" # if value in change column is false replace it with 'mm'
  return(data)
}

## rename columns
col_rename<- function(data, template, old, new)
  # data = dataframe
  # template = terms being mapped
  # old = old names of columns
  # new = new names of columns
{
  cols <- colnames(data) # vector cols created w column names of dataframe as values
  for(i in 1:nrow(template)) # i incremented by 1 starting at 1 and ending at how ever many rows are in the template data
  {
    if(isTRUE(colnames(data)[i] %in% template[,old])) # if the name of the column from the old column exists  then move on to the next line if not data is incremented again
    { 
      colnames(data)[i] <- template[,new][template[,old] == cols[i]] # if condition from is statement is met rename column in the original data set whatever it is being mapped to in the template data
    }
  }
  return(data)
}

cougar_data <- cougar_data %>%
  delete_empty_r_and_c() %>%
  status("Status", c("A", "B", "C"), c("Intact", "Field Dressed", "Skinned")) %>%
  sex("Sex") %>%
  melt_data("Length", "Weight") %>%
  add_col() %>%
  measurement_unit("measurementUnit", "variable") %>%
  col_rename(cougar_template, "Column.Name", "Template.Name")

aepyceros_data1 <- life_stage(aepyceros_data, "Age..juv..prime.adult..older.adult..old.")
aepyceros_data1 <- col_rename(data = aepyceros_data, template = aepyceros_template, old = "label", new = "term")

aepyceros_data <- aepyceros_data %>%
  delete_empty_r_and_c() %>%
  #status("Status", c("A", "B", "C"), c("Intact", "Field Dressed", "Skinned")) %>%
  sex("SEX")
  #melt_data("Length", "Weight") %>%
  #add_col() %>%
  #measurement_unit("measurementUnit", "variable") %>%
  col_rename(aepyceros_template, "label", "term")

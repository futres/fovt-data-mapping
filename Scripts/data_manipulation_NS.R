# Functions for General Data Clean Up
# Neeka Sewnath
# nsewnath@ufl.edu

library(dplyr)

# input files (cougar dataset as toy data)
template <- read.csv("https://raw.githubusercontent.com/futres/fovt-data-mapping/cougar_test/Mapping%20Files/column%20name%20template.csv")
data <- read.csv("https://de.cyverse.org/dl/d/F2088922-D273-49AE-985F-8D55966627A9/1987to2019_Cougar_Weight_Length_Public_Request.csv")

# delete empty rows and columns
data <- data %>% filter(complete.cases(.))  
data <- data %>% na.omit








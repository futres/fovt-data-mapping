#add rownames for indexing
rownames(df) <- seq(1, nrow(df),1)

#need to select out trait
#remove NAs from trait
#apply maha() function
#select out indices
#label those rows as outliers

#want to find outliers for known adults and non-estimated values
sp <- unique(scientificName)

mh.outlierTest <- function(df, group, trait){
	#df = dataset
	#group = what you're grouping by, in this case it is scientific name (vector sp)
	#trait = the trait you're testing (e.g., mass)
}
for(i in 1:length(group_by)){
  sub <- subset(df, subset = df[,scientificName] == group[i] & 
                  df[,"measurementValueEstimated"] != "True" & 
                  df[,"measurementType"] == trait & 
                  df[,"lifeStage"] == "Adult", 
                select = "measurementValue") %>%
    drop_na()
  if(isTRUE(nrow(sub) >= 10)){
    outlier <- maha(sub, cutoff = 0.95, rnames = FALSE)
    index <- names(outlier[[2]])
    if(isTRUE(length(index) != 0)){
      data.test[index,"measurementStatus"] <- "outlier"
    }
  }
  else if(isTRUE(nrow(sub) <= 10)){
      df$measurementStatus[group == group_by[i]] <- "too few records"
    }
  else{
    next
  }
}

traits <- unique(measurementType)

for(i in length(traits)){
	mh.OutlierTest(df, group_by = sp, trait = traits[i])
}

##write out Mahalanobis outlier test data----
df.mh <- df

data.noInfer_Adults <- subset(df.mh, subset = c(df.mh$measurementStatus != "outlier" &
                                                    df.mh$measurementStatus != "too few records" &
                                                    df.mh$lifeStage == "Adult" &
                                                    df.mh$measurementValueEstimated != "True"))
                                                    
limits <- function(df, group, trait){
	df %>%
	dplyr::group_by(group, trait) %>%
	dplyr::summarise(sampleSize = length(measurementValue[!is.na(measurementValue) & measurementValue > 0]),
		 	 avgValue = mean(measurementValue[!is.na(measurementValue) & measurementValue > 0], na.rm = TRUE),
                     	 sigmaValue = sd(measurementValue[!is.na(measurementValue) & measurementValue > 0], na.rm = TRUE),
                     	 upperLimit = avgValue + (3*sigmaValue),
                     	 lowerLimit = avgValue - (3*sigmaValue)) %>%
              as.data.frame()
}

limits(df, group = "scientificName", trait = "measurementType")

#merge things together

##add stats to dataframe
df.limits$sampleSize <- ""
df.limits$upperLimit <- ""
df.limits$lowerLimit <- ""
df.limits$avgValue <- ""
df.limits$sigmaValue <- ""

#cbind by scientificName and measurementType


function(df, trait, group_by, column){
df.limits[df.limits$measurementType == trait & df.limits$scientificName == group_by[i], column.x] <- data.noInfer_stats[column.y & scientificName == group_by[i]]	
}


sp = unique(scientificName)
columns.y <- data.noInfer_stats[2, lenght(data.noInfer_stats)]
traits = unique(meausrementType)
columns.x <- c(sampleSize, upperLimit, lowerLimit, avgValue, sigmaValue)

for(i in 1:length(sp)){
	for(j in 1:length(columns)){
		for(k in 1:length(traits)){
			df.limits$
		}
	}
}

df.limits <- merge(df.mh, data.noInfer_stats, by = "scientificName", all.x = TRUE, all.y = FALSE)

##write out csv with limits----
write.csv(data.limit, "data.limit.csv")

##label outliers----
df.limits$index <- rownames(df.limits)
limit.label <- function(df, sample){
	#sample = which sample size you're concerned about
df$measurementStatus[df$sample < 10] <- "too few records"	
}
samples <- c("sample.size.length", "sample.size.mass", "sample.size.tail") #make this so that it pulls samples; should get a column called "sampleSize"
for(i in length(samples)){
	
}
df.limits$measurementStatus[df.limits$sample.size.length < 10] <- "too few records"
df.limits$measurementStatus[data.limit$sample.size.mass < 10] <- "too few records"
df.limits$measurementStatus[data.limit$sample.size.tail < 10] <- "too few records"
df.limits$measurementStatus[is.na(data.limit$measurementValue)] <- "ignore"
df.limitst$measurementValue[data.limit$measurementValue < 0 | is.infinite(data.limit$measurementValue)] <- ""
data.check <- data.limit[data.limit$measurementStatus != "too few records" & 
                         data.limit$measurementStatus != "outlier" &
                           data.limit$measurementStatus != "ignore",]
data.uncheck <- data.limit[data.limit$measurementStatus == "too few records" | 
                             data.limit$measurementStatus == "outlier" |
                             data.limit$measurementStatus == "ignore",]

sp <- unique(data.check$scientificName)
length(sp) #240
nrow(data.check) #1681159

#need to split up datasets to test
#mass
for(i in 1:length(sp)){
  sub <- data.check[data.check$scientificName == sp[i] & 
                  data.check$measurementType == "mass",]
  for(j in 1:nrow(sub)){
    if(isTRUE(sub$measurementValue[j] <= sub$lower.limit.mass[1])){
      data.check$measurementStatus[data.check$index == sub$index[j]] <- "possibly not adult"
    }
    else if(isTRUE(sub$measurementValue[j] >= sub$upper.limit.mass[1])){
      data.check$measurementStatus[data.check$index == sub$index[j]] <- "possibly not adult"
    }
    else{
      data.check$measurementStatus[data.check$index == sub$index[j]] <- "possibly adult"
    }
  }
} 

#total length
for(i in 1:length(sp)){
  sub <- data.check[data.check$scientificName == sp[i] & 
                      data.check$measurementType == "total.length",]
  for(j in 1:nrow(sub)){
    if(isTRUE(sub$measurementValue[j] <= sub$lower.limit.length[1])){
      data.check$measurementStatus[data.check$index == sub$index[j]] <- "possibly not adult"
    }
    else if(isTRUE(sub$measurementValue[j] >= sub$upper.limit.length[1])){
      data.check$measurementStatus[data.check$index == sub$index[j]] <- "possibly not adult"
    }
    else{
      data.check$measurementStatus[data.check$index == sub$index[j]] <- "possibly adult"
    }
  }
} 

#tail length
for(i in 1:length(sp)){
  sub <- data.check[data.check$scientificName == sp[i] & 
                      data.check$measurementType == "tail.length",]
  for(j in 1:nrow(sub)){
    if(isTRUE(sub$measurementValue[j] <= sub$lower.limit.tail[1])){
      data.check$measurementStatus[data.check$inde == sub$index[j]] <- "possibly not adult"
    }
    else if(isTRUE(sub$measurementValue[j] >= sub$upper.limit.tail[1])){
      data.check$measurementStatus[data.check$index == sub$index[j]] <- "possibly not adult"
    }
    else{
      data.check$measurementStatus[data.check$index == sub$index[j]] <- "possibly adult"
    }
  }
} 

data.total <- rbind(data.check, data.uncheck)



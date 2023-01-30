import pandas as pand

# two main data types in pandas
# series -- 1 dimensional array
# dataFrame -- 2 dimensional array

# series 

car=pand.Series(['Hero','Toyota','Honda'])
print(car)

colors=pand.Series(['Red','Green','Blue'])
print(colors)


# data Frame

carList=pand.DataFrame({'Cars':car,'Colors':colors})
print(carList)

carList.to_csv('carList.csv')

# import data from csv

importedData=pand.read_csv('test.csv')
print(importedData)

#export data 

export_data=importedData.to_csv('newOne.csv',index=False)
print(pand.read_csv('newOne.csv'))


# export data from git sample
# exportData_git=pand.read_csv('https://raw.githubusercontent.com/mrdbourke/zero-to-mastery-ml/master/data/heart-disease.csv')
# print(exportData_git)


#Descripe Data

#without () is a attibute , with () is a function

print(importedData.dtypes)  # describe the each column data type

print(importedData.columns) #it's retruns the csv columns into list

column_new=importedData.columns
print(column_new) # we can assign columns list to another variable

 
print(importedData.index) #It's describes the index starting and ending value

print(importedData.describe()) # it's totaly describe the count,mean,std,min..etc for each integer or floating columns in csv

print(importedData.count()) # we can particularly which function  need to apply 

print(importedData['query id'].sum()) # and we can do some validation

print(len(importedData)) # get the length of dataFrame


# Selecting and viewing Data

print(importedData.head()) # it's give the snapshot of our data top 5 values

print(importedData.head(2)) # we can mention how many values we need


print(importedData.tail()) # it's same like head, it's return last 5 rows

# loc -- find data with index and iloc -- find data with posistion

sampleData=pand.Series(['data','point','analytics','Model','science'],index=[3,5,2,1,4]) # we can give our own index in series creation

print(sampleData.loc[5])  # it's returns the 5th index we given in our given data

print(sampleData.loc[1]) # Note : for loc use [] not ()

# iloc

print(sampleData.iloc[1]) # it's returns the value "point" but in above loc returns the "Model" value it's retrun the value based on posistioning

print(sampleData.loc[:1],'loc') # we can slice the data easily with ":" symbol

print(sampleData.iloc[:3])


print(importedData["query id"])

print(importedData[ importedData['id']==1 ]) # we can filter the data with this syntax




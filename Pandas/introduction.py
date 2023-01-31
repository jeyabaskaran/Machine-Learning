import pandas as pand

import matplotlib.pyplot as plt
import numpy as np

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

print(importedData[ importedData['id']==1 ]) # we can filter the data with this synt



# cross tab

car_sale=pand.read_csv('car-sales.csv')
print(pand.crosstab(car_sale['Make'],car_sale['Doors']))

print(car_sale.groupby(['Make']).std())

#car_sale.plot()    # polt a graph
#car_sale['Odometer (KM)'].plot()    # polt a graph  for paticular numerical column
#car_sale['Odometer (KM)'].hist()    # return a graph histogram for each numerical column

print(car_sale)

doloarizer=lambda x: float(x[1:-1])

car_sale['Price']=car_sale['Price'].str.replace('[\$\,]|\.\d*','').astype(int)

print(car_sale)
car_sale['Price'].plot()
#plt.show()  this keyword used to show our graph

car_sale['Make']= car_sale['Make'].str.lower() # conver the values into lower case
print(car_sale)

#importing missing values

car_missing_data=pand.read_csv('car-sales-missing-data.csv')
print(car_missing_data)


# replace Nan values into some static values

car_missing_data['Odometer'].fillna(car_missing_data['Odometer'].mean(),inplace=True)

print(car_missing_data)

car_missing_data.dropna(inplace=True) # it's drop the na values overall u have in your csv
print(car_missing_data)

car_missing_data=pand.read_csv('car-sales-missing-data.csv')
car_missing_droped=car_missing_data.dropna()
car_missing_droped.to_csv('droped.csv')

print(car_missing_data)


#series from column

seats=pand.Series([5,5,5,5,5,5])
car_sale['Seats']=seats  #creating new column
print(car_sale)

#filling nan values

car_sale['Seats'].fillna(5,inplace=True)
print(car_sale)

#column from list
liter=[7.3,6.3,6.33,6.1,9.6,8,3,6,8,10]
car_sale['litre']=liter
print(car_sale)

car_sale['litre (li)']=liter
print(car_sale)



# drop a column

car_sale=car_sale.drop('litre',axis=1)
print(car_sale)

# some calculation with existing data to create new column

car_sale['total litre occupied']=car_sale['Odometer (KM)']/100*car_sale['litre (li)']
print(car_sale)


# add a single value to whole csv

car_sale['wheels']=4
car_sale['Saftey certified']=True
print(car_sale)



# suffeld data

car_sale_shuffled=car_sale.sample(frac=0.5)  # we can shuffled our data using sample, 
#and frace if we give one it's totally shuffled all data else how many percent we give , base on that input it's shuffled
print(car_sale_shuffled)

print(car_sale_shuffled.reset_index(drop=True))

car_sale['Odometer (KM)']=car_sale['Odometer (KM)'].apply(lambda x : x/100)  # lambda function
print(car_sale)


car_miss=pand.read_csv('car-sales-missing-data.csv')
print(car_miss[car_miss['Odometer'].notna()]) # it's same like drop na , go to remove the na values in particular column
                                              # but dropna remove the drop the na values in all columns
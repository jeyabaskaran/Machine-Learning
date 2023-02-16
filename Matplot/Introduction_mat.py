import matplotlib.pyplot as plt
import numpy as np
import pandas as pand

#plt.plot([1,2,3,4,5])
#plt.show()

x=[1,2,3,4]
y=[10,20,30,40]
#plt.plot(x,y)

# first method to create matplot 

# fig=plt.figure()
# ax=fig.add_subplot()
# ax.plot(x,y)
# plt.show()

#second method to create matplot

# fig=plt.figure()
# ax=fig.add_axes([1, 1, 1, 1])
# ax.plot(x,y)
# plt.show()

#3rd method

# fig,ax=plt.subplots()
# ax.plot(x,[50,100,200,250])
# plt.show()


# workflow for Matplot lip

# x=[10,20,30,40,50]
# y=[100,150,250,400,450]
# fig,ax=plt.subplots(figsize=[5,4])
# ax.plot(x,y)
# ax.set(title="Plotting value",xlabel='Data Initializing',ylabel='Data Analyzing')
# fig.savefig("E:\Learning\Machine-Learning\__MACOSX\data.png")
# plt.show()


# Matplot with Scatterd Plot , Histogram, Lineplot, Bars plot

# x=np.linspace(0,10,100)
# print(x[:10])
 
# fig,ax=plt.subplots()  # line plot
# ax.plot(x,x**2)

# fig,ax=plt.subplots()
# ax.scatter(x,np.sin(x))


# plot data from dictionary

dict={"Monthly":200,"weekly":500,"yearly":5000}

# fig,ax=plt.subplots()
# ax.bar(dict.keys(),dict.values())
# ax.set(title="Analytics",xlabel='Data',ylabel='YData')

# bar h(horizontal bar), Histogram and Subplot options

# fig, ax=plt.subplots(figsize=(10,4))
# ax.barh(list(dict.keys()),list(dict.values()))
# ax.set(title='Data FROM dict',xlabel='x',ylabel='y')


#historgram

# fig,histo=plt.subplots()
# histo.hist(np.random.random(10))


#subplot options1

# fig,((su1,su2),(su3,su4))=plt.subplots(figsize=(10,10),ncols=2,nrows=2)
# su1.scatter(np.random.rand(100),np.random.rand(100))
# su1.set(title='Scatter Plot')
# su2.plot(dict.keys(),dict.values())
# su2.set(title='Line plot')
# su3.bar(dict.keys(),dict.values())
# su3.set(title='Bar Plot')
# su4.hist(np.random.rand(100))
# su4.set(title='Historgram Plot')

#subplots options2

fig, ax=plt.subplots(ncols=2,nrows=2,figsize=(10,5))
ax[0,0].plot(np.random.rand(100),np.random.rand(100))
ax[0,1].scatter(np.random.random(200),np.random.random(200))
ax[1,0].bar(dict.keys(),dict.values())
ax[1,1].hist(np.random.random(100))


#DataFRame visualization 1
plt.close('all')
car_sale=pand.read_csv('E:\Learning\Machine-Learning\Pandas\car-sales.csv')
dt=car_sale.cumsum()
plt.figure()
car_sale.plot()

plt.close('all')

time_se=pand.Series(np.random.randn(10000),index=(pand.date_range('1/1/2000',periods=10000)))
print(time_se)
time_se=time_se.cumsum()
time_se.plot()

plt.close('all')

#DataFrame Visualization 2

car_sale['Price']=car_sale['Price'].str.replace('[\$\,]|\.\d*','').astype(int)
car_sale['Delivery Date']=pand.date_range('1/01/2020',periods=len(car_sale))
car_sale['Total Sales']=car_sale['Price'].cumsum()
car_sale.plot(x='Delivery Date',y='Total Sales')
car_sale.plot(x='Odometer (KM)',y='Price',kind='scatter')

plt.close('all')
print(car_sale)


#DataFrame visualization 3

plt.close('all')

x= np.random.rand(10,4)
df=pand.DataFrame(x,columns=['a','b','j','e'])
df.plot.bar()

df.plot(kind='bar')

car_sale.plot.bar()

car_sale['Price'].plot.pie()
car_sale['Odometer (KM)'].plot(kind='hist')

plt.close('all')

# DataFrame visualization 4
heart_disease=pand.read_csv('E:\Learning\Machine-Learning\Pandas\heart-disease.csv')
print(heart_disease.head())

heart_disease['age'].plot.hist(bins=500)

plt.close()
heart_disease.plot.hist(figsize=(50,50),subplots=True)

#DataFrame visualization 5
plt.close('all')

# two methods to plot the values pyplot vs matplotlip OO method for quick graph use pyplot, for advanced use OO methode
#pyplot
over_50=heart_disease[heart_disease['age']>50]

over_50.plot(kind='scatter',x='age',y='chol',c='target')

#OO method mixed with pyplot

fix,ax=plt.subplots()
over_50.plot(kind='scatter',x='age',y='chol',c='target',figsize=(10,6),ax=ax)
ax.set_xlim([45,100])
plt.close('all')


#oo method from scratch (object oriented method) #dataframe data visualization 6

fig, ax=plt.subplots(figsize=(10,6));
scatter=ax.scatter(x=over_50["age"],y=over_50["chol"],c=over_50['target'])
ax.set(xlabel='Age',ylabel='chol',title='Heart Disease Analysis')
ax.legend(*scatter.legend_elements(),title='Target')
ax.axhline(over_50['chol'].mean(),linestyle='--')
plt.close('all')

#DataFrame Visualization 7

fig,(ax0,ax1)=plt.subplots(nrows=2,ncols=1 ,figsize=(10,10),sharex=True)

scatter=ax0.scatter(x=over_50['age'],y=over_50['chol'],c=over_50['target'])
ax0.set(title='Hear Disease with Chol',ylabel='Chol')
ax0.legend(*scatter.legend_elements(),title='Target')
ax0.axhline(y=over_50['chol'].mean(),linestyle='--')


scatter=ax1.scatter(x=over_50['age'],y=over_50['thalach'],c=over_50['target'])
ax1.set(title='Heart disease with Thalach analsysis',xlabel='Age',ylabel='Thalach')
ax1.legend(*scatter.legend_elements(),title="Target")
ax1.axhline(y=over_50['thalach'].mean(),linestyle='--')

fig.suptitle('HEART DISEASE ANAYLYSIS',fontsize='16',fontweight='bold')

plt.show()



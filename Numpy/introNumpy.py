import numpy as np

#numpy is a nDimensionaly array (ndarray)
# main data type in numpy is ndarray

a=np.array([1,2,3]) 
print(type(a))  # ndarray data type

a2=np.array([[1,22,44.22],[1.3,5.3,5.22]])
print(a2.dtype, a.dtype) # data type for  elments in array


a3=np.array([
    [
    [1,2,3],[2,4,5],[2,5,3]
    ],
             [
                 [1,2,4],[25,6,3],[2,5,2]
             ]
             ])
print(a3.shape, a2.shape, a.shape)                                   #get dimensionaly shapes in array


print(a3.ndim, a2.ndim, a.ndim)  # it's return the number of dimensions we have


print(a3.size,a2.size,a.size) # it's return the size of the ndarray(** how many elements in array)


import pandas as pand

# #convert to numpy ndarray to dataFrame, it's only allow to convert 2 dimensional array only
df=pand.DataFrame(a2)

print(df)


#numpy ones,zeros,random,range

sample_array=np.array([1,2,3])
print(sample_array)

ones=np.ones(shape=(1,3))
print(ones)

zero=np.zeros(shape=(4,4),dtype=float)
print(zero)

#range
range_array=np.arange(0,40,1)
print(range_array)


random_int=np.random.randint(20,size=(4,8))
print(random_int)

random_random=np.random.random(size=(2,3))
print(random_random)

random_rand=np.random.rand(5,5)
print(random_rand)


np.random.seed(100)
random_array5=np.random.randint(10,size=(5,4))
print(random_array5)


#Viewing array and matrixes

array_5=np.random.randint(20,size=(3,8))
print(array_5)

print(np.unique(array_5))  # it's return the unique elements in array

print(a[0])
print(a2[0])
print(a3[0][1][0])   # we can access elemnts value using index


print(a[:2])
print(a3, a3.shape)
print(a3[:1,:2,:1])  #splicing a array data

# Here, another best example 
array_new=np.random.randint(20,size=(2,3,4,5))
print(array_new)

print(array_new[:,:,:,:1],'da')

#artithmetic operation in numpy array

print(a+ones)
print(a*ones)

print(a*a3)

print(a3**2)

print(a/a2)
print(a%a2)
print(np.add(a,a2), np.square(a2)) # Also, we can use numpy built in function

#numpy aggregation function

import timeit
print(np.sum(a3)) 

massive_data=np.random.random(100000)
print(massive_data[:10])

start=timeit.default_timer()
print(start,sum(massive_data),timeit.default_timer())

print(start,timeit.default_timer(), np.sum(massive_data))

print(np.mean(a2))

print(np.std(a2))

print(np.var(a2))

print(np.sqrt(np.var(a2)))

print(np.min(a3))
print(np.max(a3))


#standard deviation with numpy array

import matplotlib.pyplot as plt

high_variance=np.array([1,100,500,3000,5000])
low_variance=np.array([2,4,6,8,10])
print(np.var(high_variance), np.var(low_variance))

print(np.mean(high_variance), np.mean(low_variance))

print(np.std(high_variance), np.std(low_variance))

# plt.hist(high_variance)
# plt.show()

# plt.hist(low_variance)
# plt.show()


# numpy array transpose and reshape

print(a2, a2.shape)
print(a2.reshape(2,3,1), a2.reshape(2,3,1).shape)  # we can easily change our numpy dimension using reshape 
a2_reshape=a2.reshape(2,3,1) 
print(a2_reshape * a3)


# transpose it's just like the rows-> column (or) flip the axis

print(a2.T, a2.T.shape)
print(a3.T, a3.T.shape)  # it's alos change the dimenion of numpy array


# DOT product is like a matrix multiplication 

print(a*a2) # normal multiplication

np.random.seed(0)

mat1= np.random.randint(10,size=(5,3))
mat2=np.random.randint(10, size=(5,3))  

print(np.dot(mat1,mat2.T))  # matrix multiplication perform (hint why we transponse the mat2 
 # because the shape of mat1 is 5,3 mat2 is 5,3 but dot is must match the mat1 last dimension with mat2 first dimension
 # so we transpose the mat2 )



# sample product with DOT


np.random.seed(0)
product= np.random.randint(200, size=(5,3))
print(product)

product_frame= pand.DataFrame(product, index=['Monday','Tuesday','Wednesday','Thursday','Firday'],
                              columns=['Idly','Dossai','Vadai'])
print(product_frame)

price=np.random.randint(100,size=(1,3))
price_sale=pand.DataFrame(price,index=['price'],columns=['Idly','Dossai','Vadai'])
print(price_sale)

daily_sale=price.dot(product.T)
print(daily_sale)

product_frame['Total Sale($)']= daily_sale.T
print(product_frame)


#numpy comparision operators

print(a>=a2)  # it's just return the true false matching with each elements
print(a<5)
print(a==a2)


# numpy sorting arrays

np.random.seed(0)
sort_f_data=np.random.randint(20,size=(5,6))
print(sort_f_data)

print(np.sort(sort_f_data))  # it's normaly sorting the each row 

print(np.argsort(sort_f_data)) # it's sorting and returns the indexes of each element

print(np.argmin(sort_f_data,axis=0), np.argmin(sort_f_data,axis=1))

print(np.argmax(sort_f_data,axis=0), np.argmax(sort_f_data,axis=1))


#converting images into ndarray using numpy

import matplotlib.image as img

panda=img.imread('panda2.jpg')
print(panda)


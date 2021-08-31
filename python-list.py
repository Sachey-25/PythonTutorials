currencies = ['Dollar','Euro','INR','Pound']
 #append --> Adding new elemet to the list
 #'yen'

currencies.append('AUSD')
currencies.append('Yuan')
currencies.append('Reals')
currencies.append('INR')
#Index method
index = currencies.index('Pound')
print("The index of 'Pound'  is ", index)

#index range---- > start : end,  and also start:end:step
#insert (possition, value)
print("In the possition 4 'Yen' is inserted")
currencies.insert(4, 'Yen')
print(currencies.index('Yen'))

new_list = [1,2,3,4]
currencies.insert(0, new_list)

python_tuple = ('Sachin','Bidar','Karnataka')
print(type(python_tuple))
currencies.insert(5,python_tuple)
print("***************************************************")
#Extend
extended_list=['Bangalore', 'Hydrabad','Pune','Kolkatta']
extended_list1=['Sachin','Sourav','Rahul','Yuvraj']

extended_list.extend(extended_list1)
print("Hi There! I am extended list",extended_list)

print(currencies)

sort(), copy(), reverse() 

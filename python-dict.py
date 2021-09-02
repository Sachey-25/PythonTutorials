'''set_info={1,2,3}
list_info=[2,3,4]

if(set_info.intersection(list_info)=={4,5}):
    print("If block is true")
else:
    print("If block doesnt return any values")


enter = list(input("Enter something"))
print(enter)
enter_another=list(int(input("Enter again please:")))
print(enter_another)'''

#Grouping -- list, tuple, set
'''Numbers=list(input("Enter something"))
Even_list=[]
Odd_list=[]
if(Numbers%2==0):
    Numbers.append(Even_list)) #2.,4,6,8.......
    print(greet)
elif(Numbers&2==1):
    Numbers.append(Odd_list))
else:
    pass'''

dictionary={}
#key:value --> int : int --> string: string --> int:string --> string :int
print(type(dictionary))


example_dict={'key':'value'}
print(type(example_dict))
example_dict={1:'value'}
print(type(example_dict))
example_dict={1:100}
print(type(example_dict))
example_dict={'value':200}
print(type(example_dict))

print("*****************************************************")
Example_dict={'Name':'Sachin', 1:[1,2,3,4,], 'age':27, 2: 'Cricket'}
print(type(Example_dict))

#Note : the values of dictionary can be printed with the help of key only.
#Frm sequence having each item as a pair
print("-------------------------------------------------------------------")
sequence_dict=( { 1:'apple' , 2:'ball' } )
print(type(sequence_dict))

'''seq_dict=([(1,'apple'),(2,'ball')])
seq_dict1=[(1,'apple'),(2,'ball')]

seq_dict=((1,'apple'),(2,'ball'))  # BODMAS
seq_dict=[(1,'apple'),(2,'ball')]'''

#accessing the elements from the dictionary!
Example_dict={'Name':'Sachin', 1:[1,2,3,4,], 'age':27, 2: 'Cricket'}
print("This is printing value present in dict & i.e.. :",Example_dict['Name'])
print("This is printing value present in dict & i.e.. :",Example_dict[1])
print("This is printing value present in dict & i.e.. :",Example_dict['age'])
print("This is printing value present in dict & i.e.. :",Example_dict[2])

#If i do with the value.... what will happen?
#print("This is going to error i.e .. KeyError:",Example_dict['Sachin'])

#Changing and adding Dictionary Elements
Example_dict={'Name':'Sachin', 1:[1,2,3,4,], 'age':27, 2: 'Cricket'}

Example_dict['Name'] = 'Tendulkar'
Example_dict[2]="Football"
print(Example_dict)
print("--------------------------------------------------------------")
print("Value for key 0 is :", Example_dict["Name"],
      "Value for key 2 is:", Example_dict[2])

#methods of dictionary
#keys() and values()---> return the key name
employee={'Name':'Sachin','Salary':1000,'Company':'Wipro', 'pin':560045}
print(employee)
print("-------------The below are the dict keys------------------- ")
print(employee.keys())
print("-------------The below are the dict values-----------------")
print(employee.values())

#update()
employee_dict={'desgination': 'Team Lead'}
employee.update(employee_dict)
print("This is updated dict",employee)

#How keys() wokrs when dictionary is updated???
employee={'Name':'Sachin','Salary':1000,'Company':'Wipro', 'pin':560045}
print("Before dictionary updated")
keys=employee.keys()
print(keys)

#adding an element to the dictionary

employee.update({'city':'Bangalore'})
print("After the dict updated")
print(keys)

#popitem()
'''result = employee.popitem()
print("Return value=", result)
result_onemore=employee.popitem()
print("Return value=", result_onemore)
print(employee)
#setdefault (key[, default_value])'''
employee={'Name':'Sachin','Salary':1000,'Company':'Wipro', 'pin':560045}

Company = employee.setdefault('Company')
print('employee = ',employee) #this is the place where default has to be set
print('Company= ' , Company)

#pop() #pop take one parameter....
marks ={'physics': 76, 'Chemistry': 73, 'Math': 90}

#Element that you want  to remove...
element = marks.pop('Chemistry')
print('Popped Marks:', element)
print("The dictionary left with values after pop:", marks)



















    

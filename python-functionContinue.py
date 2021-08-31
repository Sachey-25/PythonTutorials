#Default argument Functions

def default(name = "Pratik", age=27, city="Bangalore"):
    print("My Name is : " + name)
    print("I am :", age , "Old")
    print("I belong to :" , city)
    #
    #
#invoke the function
#First function call -- with parameter value
default("Sachin",32, "Channai")
#Second time calling the function - without parameter value
default()
#Third time Function call with all the possitional params
default("SomeName",27)
print("_________________________________")
#Return values / types
def returnfunc(value):
    return (10*value)

print(returnfunc(2))

def freeup():
    pass
print("Hello ")

#Python lambda Function
'''1. A lambda function is a small anonymous function
    2. A lambda function can take any number of arguments,
    but can only have one expression
    Syntax:
        lambda Expression/arguments : test_expressions'''

'''value = lambda calc : calc+10
demon = lambda free:free-10

print(value(10))
print(demon(2))

#nested - lambda function are very much useful.

def my_function(n):
    
    return lambda swing: swing * n

#Create an object
Object = my_function(2)
object = my_function(3)
print(Object(3))
print(object(3))'''

#Python -data structures -- List, Tuple, Set, Dictionary
# [] , () , {} , {}
'''print("_-------------------------------------------")

my_first = []
print(type(my_first))'''

#Listes are Ordered, Changable, Allow Duplicate items

'''say = [2345,"qwerty",5432, "qwerty", 5432]
#print(say)
#Lists are idexed. 0,1,2,3,4........N
print(say[0])
print(say[1])
print(say[2])
print(say[3])
print(say[4])'''
'''if you are tying to check for index is not present in the
list then we will end up with an error or outofrange'''
#print(say[5])

#len --> length of the list
'''print("The length of list is : ")
print(len(say))
print("The length of list is :", len(say))'''

#List holds any interger, string, boolean and combination
#of these three

'''python_integer = [12345, 876543, 22, 45, 567]
python_string =['Name','Age','City','Address']
python_bool = [True, False, True, True]
print(python_integer)
print(python_string)
print(python_bool)

python_alltype_list=[11,22,'Name',True, False,'age','city',11,
                     22,'Name',True, False,'age','city']
print(python_alltype_list)

print(python_string[4:4])
print("***********************************")'''

'''Syntax =[11,22,33,44,55]
if 20 in Syntax:
    print("22 is present")
    print("Condition checked for python list")
elif 43 not in Syntax:
    print("This is elif block")
print(len(Syntax))
print("*****************************")'''

'''Syntax_one =[11,22,33,44,55]
if(Syntax[0]==11):
    #Im trying to change the first element of the list
    Syntax[0] = 'Sachin' #string - Sachin is new data - index 0
    print("This is first index got changed and assigned to : ", Syntax[0])
    
print(len(Syntax))

freedup_list = ['Nokia','Samsung','MI','Vivo']'''

'''List Methods 1. append
2. copy
3. count
4. clear
5. insert
6. extend
7. pop
8. remove
9. index
10. reverse
11. sort'''

 currencies = ['Dollar','Euro','INR','Pound']
 #append --> Adding new elemet to the list
 #'yen'

currencies.append('Yen')
print(currencies)
    































#Python - Functions

'''def <function_name>:
    #Function body'''

#Function defination
def greet(Name):
    print("Hello EveryOne, My name is Function")
    print("We are dicussing the function concept")
    print(Name)

#Invoke the function
greet('My name is Sachin')

#Pass the parameter def greet (parameter)

#python function with the return type
def value(number):
    '''I am going to demonstrate with return type'''

    if(number >= 0):
        return number
    else:
        return -number  # -- >   - (-1234) ---> 1234
print("This is possitive number", value(1234))
print("This is negative number", value(1234))

#variable within the function
def my_function():
    #Function variable
    object = "Sachin"
    print("This from inside function: ", object)
#Outside of the function
music = "I like something"
#Invoke function
my_function()
print("This is from outside the function:", music)

#Python has two ways of function represention
#1. User defined function
#2. Built - in function

'''def add_numbers(number_one, number_two):
    result = number_one+number_two
    return result

number_one=int(input("enter a number"))
number_two=int(input("Enter another number"))
print("Magic or Logic", add_numbers(number_one, number_two))'''

#1. Possitional argument functions
#2. Arbitrary argument functions
#3. Keyword functions
#4. Default functions
#5. Lambda functions
#6. Return Values  # Recursions

'''def function_name(para1, para2, para3........ para N):
    #Understanding purpose

    #para1 --> int
    #para2 ---> string
    #paar3 ---> int
function_name(10,'Sachin', )  --> '''

def possitonal_function(joursey,name,age):
    #Function variables
   ''' joursey = 10;
    name ="Sachin Tendulkar"
    age = 40'''
   return joursey, name, age
#Invoke the function

print(possitonal_function(10,'Sachin Tendulkar', 40))

#Arbitrary Function
def my_function(*Cricketer):
    print("Six sixes in T20:  " + Cricketer[1])


my_function("Sachin Tendulkar","Yuvraj Singh","Virendra Sehwag")

print("----------------------------------------------------------------------")
#Keyword Function
def my_function(Cricket, FootBaller, Badminton):
    print(" Indian Footballer :" +FootBaller)

#invoke function
my_function(Cricket = "Sachin Tendulkar",
            FootBaller ="Sunil chitree", Badminton = "Saina Nehwal")


    






















    

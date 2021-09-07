#
# '#' --> Regex

#passord --> re.fullmacth('[a-k][0369][a-zA-Z0-9]*','\s')

'''Modules in python --> A file containng a set of
functions/python code which you want to include
in your application'''

'''def test_module(name):
    print("I am printing from another python file")

person_info = {
    "name":"Sachin",
    "age":30,
    "coutry":"India"
    }
print("------------Built-in Modules---------------")
#Built-in Modules #platform --> OS
import platform

module_info=platform.system()
module_infor = platform.machine()
print(module_info)
print(module_infor)

resonable = dir(platform)
print(resonable)'''

#python mathematics
import math

#math.acos() ---> Return the cosine of a number

print("The cos10 value is: ",math.acos(0.23452))
print("The sin20 value is:", math.asin(-0.75))
print("The tan20 valus is:",math.atan(-0.20))
print("The factorial of 4 is: ",math.factorial(4))
print("The exponential of 2 is:", math.exp(2))

''' The math.exp() method returns E raised to the
of the  power of variable number that taken E.
E ---> 2.71'''
print("absolute value of :", math.fabs(7.3409))
print("Floor digit is:", math.floor(7.3409))
print("Modulous of :", math.fmod(16,3))
print("Summation of values:", math.fsum([10,20,30,40]))
print("power of x and y:", math.pow(12,4))


print("--------------Python Random Module---------")

import random
print(random.randrange(2,6)) #start, stop, step
print(random.randint(2,6))#any random number between the range
list_info=['apple','banana','orange','mango']
print(random.choice(list_info))
print(random.choices(list_info))
print(random.getstate())

#Print a random number
print(random.random())

#capture the states
state=random.getstate() #object

#print another random number
print(random.random())

#restore the state --- > setstate()
random.setstate(state) #object

#the next random number should be the same
#as the state is been set
print("This will be same object set for first object",random.random())

print("-----------------------------------------")
#seed()
random.seed(10)
print(random.random())

random.seed(10)
print(random.random())

import datetime
time = datetime.datetime.now()
print("Current time is: ",time)

#%a ---> Tuesday ----> Tue %A
day=datetime.datetime.now()
print(day.strftime('%a'))
day=datetime.datetime.now()
print(day.strftime('%A'))


#python objects -- can be converted into JSON strings

'''dict ----> Object
list ----> Array
tuple ----> Array
str ---> String
int, float --> Number
True, False, None ---> true, false, null'''

import json

#dict representation
first_json='{"name":"sachin","age":30,"city":"Bangalore","state":"Karnataka"}'

#parse an info first_json
result_json=json.loads(first_json)

#print my output

print(result_json['name'])

#dict representation
first_json='{"name":"SACHIN","age":30,"city":"BANGLORE","state":"Karnataka"}'

#parse an info first_json
result_json=json.dumps(first_json)

#print my output

print(result_json)
print(type(result_json))

#fileHandling ------> open() close()-----> 'r', 'w', 'x', 'a'
print("------------------------------------------------")

file_example=open('testmodule.py','r')
print(file_example.read())



























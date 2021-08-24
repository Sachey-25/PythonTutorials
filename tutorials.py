print("helloWorld")

x,y,z = 10,20,30
print(x)
print(y)
print(z)

name,employee,city ='Sachin','Wipro','Bangalore'
print(name,employee,city) #Here comma is works as seperator
print(name)
print(employee)
print(city)
#If we are using print keyword to the next then by default print ,method takes the
#execution to the nextline

print()
print()
print()

#Unpack the a list --> which we denote in []
employee =["Sachin","Wipro","Bangalore"]
#we need to assign the list values to the other variables
name,employee,city=employee
print(type(employee))
print(name, employee,city)


"""Python Datatypes
text types : str
Numeric Types : int, float, complex
Sequesne Types : list, tuple, range
Mapping Types : dict
Set Types : set
Booloan Type: bool
Binary Types: bytes, bytearray, memoryview"""

#Anything enclosed with single or double or single thriple or double triple quotations
#are called as strings

mobile = 'Nokia' #string
Mobile = "Samsung" #string
Device = '''Laptop'''
device = """Surface"""

print(type(mobile))
print(type(Mobile))
print(type(Device))
print(type(device))

#index slicing

print(mobile[0])
print(mobile[1])
print(mobile[2])
print(mobile[3])
print(mobile[4])

#range or index Operator
print(mobile[0:2])

#index operator --> [start:end] end index is exclusive

#String negative slicing

'''N               O                   K               I               A
0               1                    2               3              4
-5                -4                -3             -2               -1'''

#Negative indexing must starting with lowest negative number


print(mobile[-5:-1])
print(mobile[-5: ])
print(mobile[-1:-5])
print(mobile[ : -1])

#range [start:end:step]
print("---------------------------------------------------------------")
print(mobile[0:5:2])








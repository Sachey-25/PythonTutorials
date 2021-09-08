#MEthodogoies in python files and folder
# opening a file
#read or write operation
#close the file

file_open=open('testmodule.py','r')
print(file_open.read(5))

file_open=open('testmodule.py','r')
for readlines in file_open:
    print(readlines,end=" ")

'''file_append=open('testmodule.py','a')
#write() ---> Writes the information into the file without
#making any problem to the already data present in file.
file_append.write("This  is a sentence")
file_append.write("This  is another sentence")
file_append.close()
print("New info added to the file")


#open and read the file after appending.
file_append=open('testmodule.py', 'r')
print(file_append.read())'''

'''file_overwrite=open('test.txt','w')
file_overwrite.write("Earlier there were three sentence but as of now its one")
file_overwrite.close()'''

'''file_test = open("test.txt",'r')
print(file_test.read())
file_test.close()
print("--------------------------------------------")
folder = open("C:\\Users\\Coding-Machine\\Desktop\\test.txt",'r')
print(folder.read())
print("----------------------------------------------")
file_promise=open("C:\\Users\\Coding-Machine\\Desktop\\Promise\\PythonTutorials\\test.txt",'r')
print(file_promise)
file_promise.close()

#delete the file ----> module os
import os
#os.rmdir() #folder
os.remove('test.txt')
print("file deleted successfully")'''

#Python OOPS
#Class ---> object --> constructor

class employee():
    #contructor
    def __init__(self,eno,ename,esal,ecity):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.ecity=ecity
    def info(self):
        print("Employee number:",self.eno)
        print("Employee name:",self.ename)
        print("Employee salary:",self.esal)
        print("Employee city:",self.ecity)
        print("*" *30)
#instantiate the class
obj = employee(101,'Sachin',1000,'Mumbai')
obj_one = employee(102,'Sourav',2000,'West-bengal')
obj_two= employee(103,'Rahul',3000,'Bangalore')
obj_three = employee(104,'Yuvraj',4000,'Panjab')
obj.info()
obj_one.info()
obj_two.info()
obj_three.info()


#The self
''' self is itself a variable that aleways pointing to current object
current obect --- reference variable, within python class, to refer
current object, we should use self variable'''


class Employee():
    print(__doc__)



class employee():
    #contructor
    def __init__(self,eno,ename,esal,ecity):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.ecity=ecity
        print(id(self))
#instantiate the class
obj = employee(eno=101,ename='Sachin',esal=1000,ecity='Mumbai')

print(obj.eno)
print(obj.ename)
print(obj.esal)
print(obj.ecity)
print('*' * 30)

#mulitple constructors

class Test():
    def __init__(self,x):
        print("First Constructor")
    def __init__(self,y):
        print("Second Constructor")

obj = Test(100)
obje = Test(200)



        
'''class Test():
    def __init__(self,someinfo):
        print("Constructor executed")
        self.someinfo = 100;
        self.somemoreinfo=200;
        self.somethingmore=300;
        print("Constructor executed once again")
    def __init__(self,somethingmore_three):
        print("Constructor executed")
        self.someinfo_one = 'Sachin';
        self.somemoreinfo_two='Tendulkar';
        self.somethingmore_three='Centuries';
        print("Constructor executed once again")
test_obj=Test()
print(test_obj.someinfo)
print(test_ibj.somethingmore_three)'''

'''#@class method @static method
class Test:
    classname = "Python Programming"   #variable within the class
    print(classname)
    def __init__(self,parameter):
        count = 0
        self.parameter = parameter
        print("Second Constructor")
    @classmethod
    def getclassname(cls):
        print("Classname:", cls.classname) #within the method
    @staticmethod
    def findaverage(number_one, number_two):
        print("Average of two numbers are:", ((number_one+number_two)/2))
obj_test=Test(100)
obj_test.getclassname()
obj_test.findaverage(10,20)'''

#numpy
import numpy as np

array=np.array([1,2,3,4,5,6,])
print(type(array))
print(array)

#different dimensional arrays

array_zero=np.array(20)
print(array_zero)
array_one=np.array([1,2,3])
print(array_one)
array_two=np.array([[1,2,3],[4,5,6]])
print(array_two)
array_three=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(array_three)













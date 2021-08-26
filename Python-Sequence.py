#If statement

'''key word if <test_expression>:
    identation ---> by default 4 tab space
    identaton error'''

#value = input("Enter your name")

#I am going to enter name as Sachin
'''if(value == 'Sachin'): #Condition is true
    print("This is If block") #This gets executes
    print("Entered name is :", value)#This gets executes
print("I am from outside the if block")
print("And I am Global")'''

#Find the given number is even or odd
#any number who's reminder results 0 that number
#is even,and whose reminder is not 0 that no. odd

'''number=int(input("Enter a number to check even or odd:"))

if(number%2==0):
    print("Entered number is: ", number , "is even")
if(number%2==1):
    print("Entered number is: ", number , "is odd")'''
    
#if --- else statement
#number=int(input("Enter a number to check even or odd:"))
#this is valid for a single condition
'''if(number%2==0):
    print("Entered number is: ", number , "is even")

else:
    print("Entered number is: ", number , "is odd")'''




'''Working procedure of if statement

        if <any condition ---> true>:
            #This peice of code executes
        --> false
        #If block will not been considered'''

#For the muliple condition
#if ----> elif -----> else

'''currency =  input("Enter the currency")

if(currency == 'US'):
    print("The currency is in dolar")
elif(currency=='rs'):
    print("The currency is in INR")
elif(currency=='UN'):
    print("This is an unknown currency")    
else:
    print("None the currency matched")'''


'''watch = input("Enter your fevorate watch")

if(watch == 'Fastrack' or watch=='Celvin Kiein'):
    print("This is my first if block")
elif(watch == 'Sonata' or watch=='timex'):
    print("This is my second if block")
else:
    print(" You enter have entered watch brand is not listed")'''
    
'''number_one = int(input("Enter a number"))
number_two = int(input("Enter another number"))

if(number_one%number_two==0):
    print("The number is completely dividable")
else:
    print("The number is not completely dividable")'''


print("------------------------------------------------------------------------------------------")


#Python loops:---->

# for and while

#implementation of for loop
#syntax
'''<keyword for <anyenglishletter/word> <membeship operator> defined var :
    print(<anyenglishletter/word>)'''

val = 'sachin'
for i in val:
    print(i, end=" ")
#List of the numbers
numbers = [1,2,3,4,5,6,6,7,3,4,6,6]
#logic -- to find the sum of all the numbers present in list
#variable to store the sum
sum = 0
#Calling for loop to iterate one after the next number
for result in numbers:
    #print(result) #we end up with list numbers but no sum
    #print("----------------------------------------------------------")
    #Calculating the sum of all the numbers from list
    sum = sum+result
print("The sum is ", sum)

#for loop with range()

#range(10) 0-----------------> 9

print(list(range(10)))
print(list(range(20)))
print(list(range(0,10,2)))
print(list(range(1,10,3)))


#program to iterate through a list using indexing

music =[ 'pop','rock','jazz'] #list
#iterate over the list using index
for listen in range(len(music)):
    print("I like ", music[listen])#[] ---> index operator
#program to display employee salary from the record
print("------------------------------------------------------------------")
example = {}
set_name = {1,2,3} # this will decided on the elements with the {}
remind = ()
Print = []
print(type(Print))
print(type(remind))
print(type(example))
print(type(set_name))

#dictionary  ----> dict_name = {'name' : value (int, string)}
#set ----------------> set_name = {1,2,3,4,5,6}

employee_name ="sachin"
employee_salary = {'Sachin' : 1200, 'Sourav':1300, 'Atharv'  : 14000}
employee ={1,2,3,4,54}
print(type(employee_salary))
print(type(employee))

#for loop for iteration
for emp in employee_salary:
    if(emp == employee_name):
        print("Employee found with name : ",employee_name )
        print("And the salary is :", employee_salary[emp])
        break
    else:
        print("No entry with that name")
        
















    

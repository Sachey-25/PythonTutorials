#While loop in python

#while <test_expression>:
    #Body of while loop

    #---> First the condition 
#program to add first 10 natural numbers
number = 10;

#initialize sum and the iterator
result = 0
index = 1

#While loop
#Condtion check, This will work if and only if cond is true
while index <= number: 
    result = result + index #<------------Result getting stored 
    index = index+1  #<----------------  Update the iteration
#Printing the sum of first 10 natural numbers
print("The is sum is: ", result)

#While loop is also valid with else

count = 0
while count < 10:
    print("This is while looop body")
    #count = count + 1 #Assignment operator
    count += 1
else:
    print("This is else block")
#Handling infinite loop ----> Break
#Managing the loop working ----> Continue

'''for i in sequesnce:
    #Code inside the loop
    if condition:
        #Code of IF block <-------- making the loop infinite
        break
#Codes outside for loop

while test_expression:
    #Code inside the loop
    if condition:
        #code if block
        break
#Code outside loop'''

'''for value in "Cognizant":
    if(value =="i"):
        break
    print(value, end =" ")
print("End of the loop")


for value in "Cognizant":
    if(value =="i"):
        continue
    print(value, end=" ")
print("End of the loop")
print("--------------------------------------------------------")
freeup ="Meeting"
for open in freeup:
    if(open=="t"):
        break
    print(open, end=" ")
print("End of loop")

freeup ="Meeting"
for open in freeup:
    if(open=="t"):
        continue
    print(open, end=" ")
print("End of loop")

Program to have calculator : mod add sub mul divi dynamically
using if else statement and loops'''

print("Select Operation")
print("1. add")
print("2. sub")
print("3. mul")
print("4. div")
print("5. mod")
print("6. floor")
while True:
    #input form the user
    choice = input("Enter choice ( 1 / 2 / 3/ 4 / 5 /6) :")
    number_one=int(input("Enter first number"))
    number_two= int(input("Enter secon number"))
    if (choice ==  '1'):
        print("Addition of :", number_one, 'and' ,number_two, 'is:',
              number_one + number_two)
    elif(choice ==  '2'):
        print("subtraction of :", number_one, 'and' ,number_two, 'is:',
              number_one - number_two)
    elif(choice ==  '3'):
        print("multiply of :", number_one, 'and' ,number_two, 'is:',
              number_one * number_two)
    elif(choice ==  '4'):
        print("Division of :", number_one, 'and' ,number_two, 'is:',
              number_one / number_two)
    elif(choice ==  '5'):
        print("Mod of :", number_one, 'and' ,number_two, 'is:',
              number_one % number_two)
    elif(choice ==  '6'):
        print("FD of :", number_one, 'and' ,number_two, 'is:',
              number_one // number_two)
    else:
        print("Operation invalid")

print("-----------------END to basics ---------------------------")


    
    








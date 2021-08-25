#How we are suppose to take input dynamic

number_one=100
number_two=200
print(number_one+number_two)

'''number_one=int (input("Enter the first number"))
number_two=int(input("Enter another number"))
result = number_one+number_two
print('Additon of two numbers are : ', result)'''

'''Python Operators :
1. Arithamatic operator : + ,-, *,/, **, //
2.Logical operators
3. relational operator
4. bitwise operator
5. assignment operator
6. membership operator
7. identity operator'''

number_one=4
number_two=6
#Arithmetic operator
result = number_one+number_two
print('Additon of two numbers are : ', result)
result = number_one-number_two
print('Substraction of two numbers are : ', result)
result = number_one*number_two
print('Multiplication of two numbers are : ', result)
result = number_one/number_two
print('Division of two numbers are : ', result)
result = number_one**number_two
print('Exponentioal of two numbers are : ', result)
result = number_one//number_two
print('Floor division of two numbers are : ', result)

#divison --> reminder ---> decimal --> 3.123
#floor -----> only whole number --> no decimal --> 3

#Assignment operator : =
#=, +=, -=, *= , /=, **=, //=

#a += 10 ----> a= a+10 --> a= 10+10 ---> 20

value=10
value **=10 #---> value = value - 10 ---> 0

print("Value is getting changed due assignent ", value)


#Realtion Operators
# ==, != , < , > , <=, >=

fnum = int(input("Enter first number: "))
snum = int(input("Enter second number: "))

print(fnum == snum) #results into boolean : true or false
print("true if number is less result is :", (fnum<snum))
print("true if number is greater result is :", (fnum>snum))

#Logical Operators
#and , or, not ---------> && ||  !
#if the both operands are true results true - and
#if any one of the operand is true results true - or
#reverse of any operand - not
print("---------------------------------------------------------------")
print(fnum <= snum and fnum == snum)
print(fnum>= snum and fnum!=snum)
print('--------OR operator------------------------')
print(fnum <= snum or fnum == snum)
print(fnum >= snum or fnum!=snum)
print('---------Not operator------------------')

print(not (fnum <= snum) and fnum == snum)


#Identity ---> whether the elements is present or no
name='sachin'
Name='sachin'
print('-------------Identity operator-------------------')
print(name is Name)
print(not name is Name)
print(name is not Name) #pure identity Operator

#Membership operator --> In , not in
#Identity ---> whether the elements is present or no

print('-----------Membership Operator----------')
print('s' in name)
print('sac' not in Name)

























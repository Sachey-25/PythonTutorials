'''tuple = (1,2,3,4,5,6)
print(type(tuple))
print("********************")

random =(1,2,3,'lemon',('Onion','tomoto'),True,False)
#Change the tuple object/data
#random[1]=9
print(random)

#Iterate thorugh the tuple
for name in ('Sachin'):
    print("Hello", name)
tuple methods: 1. count 2. Index

result = random.count(1)
print(result)
print("**********************************")

Tuple = (0,1,(2,3),(2,3),1,[3,2],'Greet',(0))
convert = list(Tuple)
print(type(convert))
print("*************************************")
#Count apprerance of (2,3)
result = Tuple.count((2,3))
print("Count of (2,3) in Tuple is :", result)
result1=Tuple.count([3,2])
print("Count of [3,2] in Tuple is:",result1)

print("Tuple index")

success = Tuple.index([3,2]) #Value of tuple but not the index
print("Index possition of Tuple[1] is :", success)

Connect = (1,2,4,5,5,6,6,7,7,8,9,0)
freeup=Connect.index(6)
print(freeup)

#Note : We can convert any sequence to List, Tuple, Set and Dict
#Set = {}



random2=(1,2,3,('lemon','onion','tomoto'),True,[4,5,6])
success1 = random2.index([4,5,6])
print(success1)'''


'''print(type(sequence))
#No duplicates in the set
print(sequence)
#Sets are unordered, unchangable and no duplicate values
for i in sequence:
    print(i)

#I want to add the new elements to the set --> Yes !
sequence.add("cricket") # one parameter ()
sequence.add("football")
sequence.add("baseball")
#update () ----> to add the elements from another set to the current
games ={'Chess','Badminton','ludo'}
sequence.update(games)
print(sequence)
#remove() ----> wich takes one parameter i.e value but not index
sequence.remove('baseball')
sequence.remove(6)
sequence.remove('ghi')
print("Few elements are removed from the set")
print("now elements of the set is:", sequence)

#discard ---> Is also used to remove the element
sequence.discard("Sachin")
print(sequence)
print("----------------------------------------------------------------")
#pop() --> first elements of the set will be popped out
element=sequence.pop()
print(element)
print(sequence)'''
#Sets in the python
sequence={1,2,3,4,5,6,'abc','def','ghi',True, False}
print("Below is printing the cleared set and its going to be empty")
#clear() #del
sequence.clear()
print(sequence)
print("****************************************")

print("Below the set union performed")
#Set Joining union, intersection
set_one={'abc','def','ghi'}
set_two={10,20,30,40}
#we need to take third variable..
set_join=set_one.union(set_two)
set_join_result=set_two.union(set_one)
print("This is my second union set")
print(set_join_result)
print(set_join)

#intersection
inter={'Sachin','Shankar','Anand'}
section={'Cognizant','Wipro','Google'}
commondata ={'Sachin','Shankar','Anand'}
#applyting the insection concept python sets
#Third variable
result = inter.intersection(section)
result_data = inter.intersection(commondata)
print("Common data's are present")
print("Updated intersection set")
print(result_data)
print("first intersection applied")
print(result)


s1={1}
print(type(s1))
t1=(1)
print(type(t1))
t2=(1,2)
print(type(t2))






























    

#Regex
#findall, match, split

#compile() finditer()
import re

pattern = re.compile('python')
#This method is used for matching the pattern
print(type(pattern))

#finditer ---> Couting perpose --> iteration

#start()
#end()
#group()

#Given string --> 'aabbccdd'
#amtching -----> 'ab'

'''matches = re.finditer('ab','aabbccdd')
for find in matches:
    print(start(), '..........' , end() , '...........' , group())
print("Consider all possible matches")


#start(), '..........' , end() , '...........' , group()
#0 ....................... 2  .....................  ab'''


'''[abc] ===> a or b or c
[^abc] ===> except any other charecter
[0-9] ===> any digit
[a-z] ===> any lowercase
[A-Z] ===> any uppercase
[a-zA-Z0-9]==> Any aplhanumeric
[^a-zA-Z0-9]===> Except alphanumeric'''

'''count=0
pattern = re.compile('ab')
#where we need to seach
matchers = pattern.finditer('abaababa')
for match in matchers:
    count=count+1
    print("Match is available at start index:", match.start())
    print("macth is availale at end index:", match.end())
    print("match is available at group index", match.group())
    print("======================================")
print("Number of count:", count)


matcher = re.finditer('ab','abaababa')
for match in matcher:
    count=count+1
    print("Start:{},End:{}, Group:{}"
          .format(match.start(),match.end(),match.group()))
    print("Number of occurance at the indexplace  :", count)

print("****************************************************")

#Search for a or b or c

seacher = re.finditer('[abc]','a7bl#rt&98@k9zc')
for match in seacher:
    print(match.start(),'...............', match.group())

print("--------------------------------------------------------------------------------")
seacher = re.finditer('[^abc]','a7bl#rt&98@k9zc')
for match in seacher:
    print(match.start(),'...............', match.group())

print("--------------------------------------------------------------------------------")
seacher = re.finditer('[a-zA-Z]','a7bL#RT&98@k9zc')
for match in seacher:
    print(match.start(),'...............', match.group())

print("--------------------------------------------------------------------------------")
seacher = re.finditer('[0-9]','a7bL#RT&98@k9zc')
for match in seacher:
    print(match.start(),'...............', match.group())

print("--------------------------------------------------------------------------------")
seacher = re.finditer('[^a-zA-Z0-9]','a7bL#RT&98@k9zc')
for match in seacher:
    print(match.start(),'...............', match.group())'''

#Predefined regex
#'\s' ----> space charecter
'''  '\S' ---> Except space charecter
'\d'----> digit
'\D'---> Except
'\w'===> word chrecrecter
'\W'------> Special charecters
'.'------> any charecter which include alphanumeric, special chareter'''

#Qunatity Regrex
'ababababa'
'''a---> Exactly one match  ---> a
a+ ---> Atleast one match except no occurance --> 
a* ----> Anynumber of a's match including zero.
a? ---> atmost one match either one match or zero match'''
'''print("-------------------------------------------Regular expresion-----------------------------")
matchers = re.finditer('a','abaababa')
for match in matchers:
    print(match.start(),'........', match.end(), '.........', match.group())
print("atleast one match should be present'")

print("-------------------------------------------Regular expresion-----------------------------")
matchers = re.finditer('a+','abaababa')
for match in matchers:
    print(match.start(),'........', match.end(), '.........', match.group())
print("Consider all the possible matches")

print("-------------------------------------------Regular expresion-----------------------------")
matchers = re.finditer('a*','abaababa')
for match in matchers:
    print(match.start(),'........', match.end(), '.........', match.group())
print("Any number of a's including no match at the index also")

print("-------------------------------------------Regular expresion-----------------------------")
matchers = re.finditer('a?','abaababa')
for match in matchers:
    print(match.start(),'........', match.end(), '.........', match.group())
print("Atmost one match, either ine match or zero")

print("----------------Qunatity Regular expression---------------")
given_string = re.finditer('\s','Sac @ hin')
for found in given_string:
    print(found.start(),'...............', "Group matched : ", found.group())
print("This returns space present in the string")


print("----------------Qunatity Regular expression---------------")
given_string = re.finditer('\S','Sac @ hin')
for found in given_string:
    print(found.start(),'...............', "Group matched : ", found.group())
print("This returns non-space present in the string")

print("----------------Qunatity Regular expression---------------")
given_string = re.finditer('\w','Sac @ hin')
for found in given_string:
    print(found.start(),'...............', "Group matched : ", found.group())
print("This returns only words present in the string")
print("----------------Qunatity Regular expression---------------")
given_string = re.finditer('\W','Sac @ hin')
for found in given_string:
    print(found.start(),'...............', "Group matched : ", found.group())
print("This returns non-charecter words present in the string")

print("----------------Qunatity Regular expression---------------")
given_string = re.finditer('\d','Sac @ hin#25%10$92')
for found in given_string:
    print(found.start(),'...............', "Group matched : ", found.group())
print("This returns digits present in the string")

print("----------------Qunatity Regular expression---------------")
given_string = re.finditer('\D','Sac @ hin#25%10$92')
for found in given_string:
    print(found.start(),'...............', "Group matched : ", found.group())
print("This returns digits present in the string")'''

print("---------------------Findall Method-------------------------------")

pattern_match=re.findall('\s','a7 #@sfj &&8 90')
print(type(pattern_match))
print("Space charecters of thier index values are below")
print(pattern_match)
print("---------------------Findall Method-------------------------------")

pattern_match=re.findall('\S','a7 #@sfj &&8 90')
print(type(pattern_match))
print("Space charecters of thier index values are below")
print(pattern_match)

pattern_match=re.findall('\w','a7 #@sfj &&8 90')
print(type(pattern_match))
print("Space charecters of thier index values are below")
print(pattern_match)

pattern_match=re.findall('\W','a7 #@sfj &&8 90')
print(type(pattern_match))
print("Space charecters of thier index values are below")
print(pattern_match)

pattern_match=re.findall('\d','a7 #@sfj &&8 90')
print(type(pattern_match))
print("Space charecters of thier index values are below")
print(pattern_match)

pattern_match=re.findall('\D','a7 #@sfj &&8 90')
print(type(pattern_match))
print("Space charecters of thier index values are below")
print(pattern_match)

print("--------sub() --> Substituion or replacement-------")
#substitution = re.sub(regex,replacement, targetstring)
substitute = re.sub('\d','*','a7b9k59tk')   #a7b9k59tk --> digits
print(substitute)
#substitution = re.sub(regex,replacement, targetstring)
substitute_word = re.sub('\W','**','a7b$9k&5#9@tk')   #a7b9k59tk --> digits
print(substitute_word)

#substitution = re.sub(regex,replacement, targetstring)
substitute_word = re.sub('\w','*','Sachin')   #a7b9k59tk --> digits
print(substitute_word)

#subn ---> Number of times the replacement happened
#substitution = re.subn(regex,replacement, targetstring)
substitute_word = re.subn('\d','*','a7b9k59tk')   #a7b9k59tk --> digits
print(type(substitute_word))
print('the result string : ', substitute[0])
print(substitute_word)

#spilit()
split_string='need 15days:fifteen for recovery:2021'
matcher = '\d+'
result = re.split(matcher, split_string,1)
print(result)

split_another = re.split('-','sac-hin',1)
print("Split done", split_another)
split_another = re.split('-','10-20-30-40-50',1)
print("Split done", split_another)

split_another = re.split('-','10-20-30-40-50',2)
print("Split done", split_another)
split_another = re.split('-','10-20-30-40-50',3)
print("Split done", split_another)


#Search method in regex
match_string='Programming is fun'
result = re.search('Sachin',match_string)
if(result!= None):
    print("Target string contains 'fun' into it")
    print("String pattern matched.......!")
else:
    print("Target string doesnt contains 'fun' into it")

match_string='Learning python is very easy'
result = re.search('Learning',match_string)
if(result!= None):
    print("Target string starts with 'Learning' ")
    print("String pattern matched.......!")
else:
    print("Target string doesnt starts with 'Learning' ")
print("-----------------------------------------------------------------------------")
match_string='Learning python is very easy'
result = re.search('^Learning',match_string)
if(result!= None):
    print("Target string starts with 'Learning' ")
    print("String pattern matched.......!")
else:
    print("Target string doesnt starts with 'Learning' ")

print("--------------Regular expression is done---------------------")

#validate mobile number
phone_number=input("Enter mobile number: ")
#[6789][0-9][0-9][0-9][0-9]   6 ---> 10digits --> {9}
#[6-9]\d{9}
match = re.fullmatch('[+91]','[6-9]\d{9}', phone_number)
if(match!=None):
    print(match,"Entered number is valid")
else:
    print(match, "Entered number is invalid, Enter again!")

password validate!!!!
allowed charecters
digits
and * only
2. first charec should be lowercase, from a to k
3. second charecter should be divisible by 3, first 10 digits
4. the length of password should 4.






















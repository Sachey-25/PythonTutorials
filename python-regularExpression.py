#Python Regular Expressions
#Special Charecters

#[a-zA-Z0-9$] --> Set
#^[a-zA-Z0-9$] --> Except

#metacharecters : [] . $ + ? {} \ |
#[] --> set if everything inside the sqaure brackets
#[abc] -----> macth () , findall(), search()

'''expression        testing expression
[abc] ---->          string [a] ----> No match
                        [ab]
                        [abc] ---------> Exact match '''



'''[^abc] --> Excpet abc everything will be match
[0-9] ----> Any digit
[^a-zA-z0-9]  --> any special charecter.

. --> period ^
$ -- whether a certain string is ends with a specific
charecter
* -- whether we have zero or more occurance in the
pattern

+ -- whether we have one or more occurance

? macthes zero or one occurance.

{} --> atleast n and at most m
a{2,3}'''

import re
"""string_pattern = 'hello 12 hii 89. greet 21'
#\d ---> Checks for the digits
pattern = '\d+'
charecter ='\w'   #[a-zA-z]

result = re.findall(pattern, string_pattern) #takes two parameters
result_next = re.findall(charecter, string_pattern)
print(result)
print(result_next)


\s - matches where a string contains whitespace
\S - matches where a strinf contains any non-whitespace

\d - macthes decimal digit
\D matches non decimal digit

\A - Matches if the specified charecters

sentence = "The sky is blue"
pattern = '\AThe' """
print("***************************")
word = "Cookie"
sequence = "Cookiee"

password  = "Sachin@25"
password_check ="Sachin @25101992"



if (re.match(password_check,password)):
    print("Pattern matched")
else:
    print("Not a match")
print("***************************")
'''
Greet="GoodEvening"
if(re.search('Good', 'GoodEvening')):
    print("Searched and found")
else:
    print("Search is not found")

Greet_again="GoodEvening"
if(re.search('Greet', 'GoodEvening')):
    print("Searched and found")
else:
    print("Search is not found")

sentence = "I am readin a pythonbook"
find = re.findall("Java", sentence)
search = re.search("\s", sentence)
check = re.search("\S",sentence)
print("Whitespaces are present",search)
print("Non spaces",check)
print(find)'''


































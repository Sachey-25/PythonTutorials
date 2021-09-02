#Python Exceptions

#Error --> Real interuption of the code flow
#Exception --> bypass the error by user defined.

'''try ... except
try ... except .. else
try .. except ... finally'''
try:
    print('Enter  the net sales for')
    previous = float(input('- Prior time:' ))
    current = float(input('-Current time: '))
    #Calculate the change in percentage
    change = ((current - previous)*100/previous)
    #Show the result
    if( change > 0):
        result = f'Sales increase {abs(change)}%' #string formating
    else:
            result = f'Sales decrease {abs(change)}%'
    print(result)
except:
    print('Error! Please enter integers only' )

#i wanted handle multiple errors however every after a time
    #my interpreter should go that logic where exception
    #handled exactly
# alias -----> as
''' try:
        #Code of practice
    except <give the error name> as <name convention>:
        #code to handle the exceptio...... '''

try:
    print('Enter  the net sales for')
    previous = float(input('- Prior time:' ))
    current = float(input('-Current time: '))
    #Calculate the change in percentage
    change = ((current - previous)*100/previous)
    #Show the result
    if( change > 0):
        result = f'Sales increase {abs(change)}%' #string formating
    else:
            result = f'Sales decrease {abs(change)}%'
    print(result)
except ValueError as error:
    print('Error! Please enter integers only' )

'''try:
    pass
except:
    pass
except:
    pass
except:
    pass
except:
    pass'''


try:
    print('Enter  the net sales for')
    previous = float(input('- Prior time:' ))
    current = float(input('-Current time: '))
    #Calculate the change in percentage
    change = ((current - previous)*100/previous)
    #Show the result
    if( change > 0):
        result = f'Sales increase {abs(change)}%' #string formating
    else:
            result = f'Sales decrease {abs(change)}%'
    print(result)
    print(Sachin)
except ZeroDivisionError:
    print('Error! divison by 0 is not possible' )
except ValueError :
    print('Error! This is value Error' )
except NameError as nerr:
    print('Error! This is name Error' )
except TypeError:
    print('Error! This typeError' )



    

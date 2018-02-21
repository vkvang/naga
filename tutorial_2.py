

# ==== BOOLEANS ==== #

# Two possible values for boolean 'True' or 'False'
#	** case-sensitive

myBoolean = True;
print 'Value of myBoolean:' , myBoolean

# Use the '==' operand to test boolean statements
print 'Is \'hello\' and \'hella\' the same?','hello' == "hella" 
# Use the '!=' operand compare not-equal to statements
print 'Does 1 not-equal 2?' , 1 != 2, '\n'

# Using comparisons 'greater than' / 'less than'
#	same thing with '(greater/less) than or equal to'
print 'Compare 4 < 5 :', 4 < 5
print 'Compare 7 >= 9 :', 7 > 9

print 'Compare 7 == 7.0 :', 7 == 7.0
print

# ==== IF-ELSE STATEMENTS ==== #

# Using if-else statements
'''	

if expression:
	statements
else:
	statements

'''

# It is mandatory for there to be indentation in code!
#	Can also nest if statements by indenting more
if True:
	print '''False
  '2nd False'''
  	print 'Will this be printed?'
else:
	print '''Entered the else!
  'We did not get a True initially.'''

print 'Exited: Not in if statement!'

# The 'elif' statement is short-hand for else-if
num = 50
if num == 40:
	print num
elif num <= 30:
	print num, 'is less than equal to 30.'
elif num >= 30:
	print num, 'is greater than equal to 30.'
else:
	print 'Could not find an answer.'

# The 'or' command compares boolean logic w/ principle of "or"
print True or False

# The 'not' command compares boolean logic w/ principles of "not"
print not True

# *********************** #
# ORDER OF PRESEDENCE #
'''
# BASIC MATH OPS

# 	BITWISE COMPARE
# 	[<< >>] --> [&] --> [^] --> [|]
#		SHIFTS -- AND -- XOR -- OR

# 		[==/ < > / <= >= / !=] --> [not] --> [and] --> [or] 
'''
# *********************** #

print True and False or True
print not True and False or True

# ==== WHILE STATEMENTS ==== #

'''

while expression:
	statement

'''

myInt = 0

while myInt <=5:
	print myInt,
	myInt += 1

print 'Finished!'

# Use 'Ctrl-C' to exit out of infinite loops

# Use 'break' in order to end a loop pre-mature
# Use 'continue' in order to jump back to top of loop
myInt = 10
while True:
	print myInt
	myInt -= 2
	if myInt > 4:
		print 'Let\'s keep going!-',
		continue
	elif myInt == 2:
		print 'Taking a break!'
		break
	else:
		print 'Almost there!-',

print 'I finished now.'
print

# ==== ARRAYS & LISTS ==== #

# Lists are stored btween '[]' and entities separated by commas
wordlist = ['Red','Blue','Green']

print 'This is my word list: '
print wordlist[0], wordlist[1], wordlist[2]

# It is possible to store items of different types w/in a list
# You can also create nested lists
arr = [100, 250, [10, 20, 30], ['cats','dogs','fish'], ['the','and']]

print arr[4][0], arr[2][1], arr[3][2], arr[4][1] , arr[1], arr[3][0]

arr = 'Dragon'
print arr[3]

# LIST OPPERATIONS

del arr
arr = [1, 2, 3, 4, 5]
arr[3] = 7

# Print the whole list
print arr

# Lists can be added or multiplied just like strings
arr = [11, 12, 13]
print arr + [14, 15, 16]
print arr * 3

# Use the 'in' command to check if there is a specific element w/in list
print 'Is there an 11 in the list \'arr\':', 11 in arr
print 'Is there an 14 in the list \'arr\':', 14 in arr

# Use the 'not' command to check if element is not in list
print 'There is not a 15:', 15 not in arr
print

# LIST FUNCTIONS

# Use the 'append()' method to add to end of list
del arr

arr = ['cat','dog','fish']
arr.append('turtle')

print 'This is the contents of \'arr\':', arr

# Use the 'insert(index,element)' method to add to the index value
arr.insert(1,'parrot')
print 'This is the contents of \'arr\':', arr

# Use the 'index()' method to find the first instance of the element
print 'The index of \'dog\' is:', arr.index('dog')














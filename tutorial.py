# Enable forward compatibility with Python 3
from __future__ import division # Works for division w/ floats


# ===== COMMENTS ==== #

# The '#' is used to comment.
# This was a comment

# ===== MULTI-LINE COMMENTS ==== #

# use ''' in order to do a multi-line comment

# ===== PRINT STATEMENTS ==== #

# This is a print statement.
print("Hello World!\n");
#print "Hello World!\n";

# ===== VARIABLES AND SIMPLE MATH ==== #

# Variables are stored using the '=' sign

''' All variables are dynamic
		*In order to cast you use:
			* int() ; str() ; float()
'''

# Variable names consist of ONLY letters, numbers, underscores
#	CAN NOT start variable name with a number
#	It is case-sensitive, so 'case' and 'Case' are two different variables

# Use the 'del' command to delete a variable
#	Variables can be re-assigned and do not have specific type when assigned
#	Example: foo = 'bar' --> foo = 25 will result in foo being integer 25


# This is simple arithmetic
egg = 2 + 2;
spam = 2 * 3 - 5;
monty = 10 / (2 + 3);
monty2 = float(10 / 2);

# In order to print string + integer,
#	FORMAT: STRING , INTEGER
print "This is the result of 2 + 2 = ",  egg;

print "This is the result of 2 * 3 - 5 = ", spam;

print "This is the result of 10 / (2 + 3) = ", monty;

print "This is the result of (-8 + 4) * -3 = ", (-8 + 4) * -3;

# ALTERNATIVE WAY OF PRINTING TWO DIFF VARIABLE TYPES
#	WHERE EACH '{}' IS REPLACED BY TYPE IN '.format()'
print "{} and {}".format("String",1);

print

# Working with exponential numbers

exp = 2**10;

print "This is the result of 2**10 (or 2 raised to the 10th) = ", exp;

# In order to get the correct result, we must convert/type the '1/2' as the
# math of two floats manually

print "This is the result of 25**(1/2) (or square root of 25) = ", 25 ** ( 1.0/2.0 );

# Use the '//' to get the quotient
print "This is the quotient of 20/6 =", 20//6;

# Use the '%' to show the remainder or perform modulo
print "This is the remainder of 1.25/0.5 =", 1.25%0.5;

print 
# Division-by-zero Error
#print -12 / 0;

# ===== STRINGS STATEMENTS ==== #
print "This is a String.";

print 'This is another string.';

# Using ' """ ' will allow for any enters onto new line to be present in output
# we can use '\t' to tab and '\n' for new line
print """Dear So-and-so,
\tToday I would like to give thanks to all my supporters.
\tThis will show up on a new line.\n"""

# ===== SIMPLE INPUT & OUTPUT ==== #

# Use the 'raw_input()' command to prompt an input from user
# The 'input()' command is used in Python 3
myStr =  raw_input('Please, Enter a something: ')
print "This is what was entered by you: " + myStr
# The program will output the response as a string to user.

# You can concat strings by used the '+' sign
print "Spam"+'Eggs'

# Strings can be multiplied to create repeated concat Superstring
#	- Can't multiply by a float
#	- Can't multiply string by string
#	- Usually String goes first, but same result otherwise
print "Copy" * 4
print 4 * 'Cat'

# ===== IN-PLACE OPERATORS ==== #

ex = 5
ex *= 4
print ex
# The function 'ex++'' would not work for 'ex + 1'

ex = 'Hammer'
ex += 'shark'
print ex






from __future__ import division

total = 20

'''
# Trying an alternative for switch statements
def one():
	print "You typed one.\n"
	#total -= 1;

def two():
	print "You typed two.\n"
	#total -= 2;

def three():
	print "You typed three.\n"
	#total -= 3;
'''

def one(total):
	#print "You typed one.\n"
	total -= 1;
	print total;

def zero(total):
	print "You typed zero.\n"

options = { 
	0 : zero,

	1 : one,
	2 : 'two',
	3 : 'three',
}

# Map the options for inputs
'''def switcher(argument):

	options = {
		1 : one,
		2 : 'two',
		3 : 'three',
	}

	print options.get(argument,'Invalid Response')
'''

'''
while True:
	print 'There are', total, 'sticks left over.\n'
	opt = raw_input('Please enter a: \'1\' , \'2\' , or \'3\'.');

	if total <= 3:
		if total == 3:
			if opt == 3:
				options[3];

			elif opt == 2:
				options[2];
				print 'This player wins.'
				break

			elif opt == 1:
				options[1];
				print 'Other player wins'
				break

			else:
				continue;
		else:
			continue;
	else:
		options[opt];

print 'Game is over.'
'''

num = input('Please enter a 1, 2, or 3: ');
#switcher(num);

options[num](total);

print 'ENDED'
'''
print switcher(num);
print total, 'sticks'
'''









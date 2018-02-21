from __future__ import division
import random

'''
This 'special' program will simulate a game of stix that will
start with 50 sticks and slowly the two players will take away
sticks from the whole until the last stick is taken.

OBJECTIVE: 	The point of the game is to not be left with the last
stick. As the player that takes the last stick is the loser.
On each turn, 
	the player(s) can choose either: one, two, or three sticks
	the turn then alternates to the next player, and then back

'''

# VARIABLES #

# Holds the total amount of sticks left
sticks = random.randint(4,55);

# Holds a boolean value to determine if game is over
gameover = False;

# Holds the name of each player
player1 = None
player2 = None

# Holds the choice of number of sticks taken from pool
choice = 0;

# Prompt the user about the game!
print '''Hello Players!

This is the game of Stix. We will start out with a random number of sticks 
in the pool. Upon your turn, you may choose: one, two, or three sticks 
from the pool. The objective of the game is to not take the last stick 
from the pool.
'''

# Initialize Players.
player1 = raw_input('What is the name of player1? ');
print 'Welcome to the game, ' + player1 + '!'
player2 = raw_input('What is the name of player2? ');
print 'Welcome to the game, ' + player2 + '!'

# Coin-flip

'''
*** Need to impliment the coin flip and introduce variable to hold
the current caller.

*** Work out the integration of a heads or tails call
Alternate players

Use while loop to create cycle if common errors arise
'''


# Variable to hold whether it is a heads or tails
coin = None;
toss = random.randint(1,2);

# Simulate the coin toss
if toss == 1:
	coin = 'heads';
else:
	coin = 'tails';

# Variable to hold name of caller
caller = player1;

# Variable to hold the call of whether it's heads/tails
the_call = raw_input('What is your call, ' + str(caller) + '? \'heads or tails\' ');
# Holds the name of current player's turn
current_player = None;

if the_call == coin:
	current_player = caller;
else:
	# Give other player first pick
	if caller == player1:
		current_player = player2;
	else:
		current_player = player1;

# Initialize the Game.
while not gameover:
	if sticks >= 0:
		print 'There are ' + str(sticks) + ' leftover.\n'
		print 'It is currently, ' + str(current_player) + '\'s turn.';
	while True:
		try:
			choice = input('Would you like 1, 2, or 3 sticks? ')
			break
		except SyntaxError:
			print 'Please enter a valid number.\n'
			continue
		except NameError:
			print 'Please enter a number: 1, 2, or 3.\n'
			continue

	# Case: only a few sticks left
	if sticks <= 3:
		if choice > sticks:
			print 'INVALID RESPONSE, TOOK MORE THAN STICKS LEFTOVER.\n'
			continue;
		if sticks - choice == 0:
			print 'You Lose, ' + str(current_player) + '!\n';
			break

	# Case: Normal play
	if choice == 1 or choice == 2 or choice == 3:
		sticks -= choice;
	else:
		print 'INVALID RESPONSE!'
		continue

	# Change player
	if current_player == player1:
		current_player = player2;
	else:
		current_player = player1;


	# Set the winner
	winner = None;

	if current_player == player1:
		current_player = player2;
	else:
		current_player = player1;

	winner = current_player;

	# Thank you message! #
	print 'The winner is ' + str(winner) + '!'

	answ = True
	while answ:
		response = input('Would you like to play again? Y or N\n')
		if response == 'Y':
			gameover = False
			answ = False
		elif response == 'N':
			gameover = True
			answ = False
		else:
			continue

print 'Thank you for playing Stix! Please come play again!\n'













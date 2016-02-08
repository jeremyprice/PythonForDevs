
"""
Make the operator guess the correct number between 1 and 100
"""

from random import randrange
ran_num = randrange(1, 101)
attempts = 0
while True:
    temporary = raw_input('Enter your guess: ')
    guess = int(temporary)
    attempts += 1   # shorthand for attempts = attempts + 1
    if guess < ran_num:
        print 'Your guess is too low'
    elif guess > ran_num:
        print 'Your guess is too high'
    else:
        print 'Your guess is correct!'
        print 'You succeeded in {0} attempts.'.format(attempts)
        break

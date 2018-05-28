import random
import os

print('-----------------------------------')
print('     GET IT RIGHT, OR YOU DIE!     ')
print('-----------------------------------')
print()


def say_it(text):
    s = 'say "{}"'.format(text)
    os.system(s)


the_number = random.randint(0, 100)
guess = -1

tell_name = 'WELCOME TO THE FABULOUS AMAZING NUMBER GAME COMING TO EVERY CONSOLE ON THE MARKET.' \
            ' THE RULE IS SIMPLE, YOU SCREW UP YOU DIE. YOU MUST GUESS A NUMBER BETWEEN 1 AND 100.' \
            ' BUT FIRST, TYPE IN YOUR NAME...'

print(tell_name)
say_it(tell_name)

name = input('Enter your name:' )


while guess != the_number:
    guess_message = 'GUESS A NUMBER BETWEEN 0 and 100: '
    say_it(guess_message)
    guess_text = input(guess_message)
    guess = int(guess_text)

    if guess < the_number:
        low = "TOO BAD {}, YOUR GUESS OF {} WAS TO LOW, PIG. HA HA HA.".format(
            name, guess)
        print(low)
        say_it(low)
    elif guess > the_number:
        high = 'TOO BAD {}, YOUR GUESS OF {} WAS TO HIGH, HA YOU ARE A LOSER.'.format(name, guess)
        print(high)
        say_it(high)
    else:
        correct = 'Oh wow {}, you actually did it. I guess {} was right, cool.'.format(name, guess)
        print(correct)
        say_it(correct)
        
final = "You're done! Go outside, you fat potato!"
print()
print(final)
say_it(final)


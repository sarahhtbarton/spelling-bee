#!/usr/bin/python3
# This version sucks but I'm learning from my mistakes 
'''
This script requires word.txt which is a list of over 65,000 words.
You may find a better quality set of words (or dictionary) to use
as long as you name it words.txt and place it in the same directory as
spell_bee.py
'''

import random

letters_qty_prompt = "Enter letters per word..."
word_qty_prompt = "Please enter how many words you need..."
error_prompt = '''Are you sure you entered a number?, please try again...'''

# COMMENT ** I havn't figured out how to catch user input errors for integers which
# are too large for the words.txt  e.g. there are no 50 letter words
# and there may be less than 10 23 letters words.
# The program exits with an error if this happens


def user_input_check(prompt):  # asks for user input and checks for not integer
    global user_qty_entered
    while True:
        try:
            user_qty_entered = int(input(prompt))
        except ValueError:
            print(error_prompt)
            continue  # back to try loop
        else:
            break  # break while True loop


user_input_check(letters_qty_prompt)
letters_qty = user_qty_entered  # user input,How many letters?
user_input_check(word_qty_prompt)
word_qty = user_qty_entered  # How many words?
print('\nYou have asked for '+str(word_qty) + ' words')
print('containing '+str(letters_qty) + ' letters\n')

wait = input("Please press enter to continue....\n")

word_wl = []  # define a list so we can append to it later

with open('words.txt', 'r') as f:
    for lines in f:  # reads one line at a time (rather than store the whole of words.txt)
        line_contents = f.readline()
        words = line_contents.split()  # splits each line into words
        for word in words:  # stores all the "letters_qty" letter words in word
            if len(word) == letters_qty:
                word_wl.append(word)

last_word = len(word_wl)

for i in range(word_qty):  # to display the requested number of words
    rdm_word = random.randrange(0, last_word)
    # this is not working for numbers out of range (see above COMMENT **)
    # might have to re-think the whole thing
    print(word_wl[rdm_word])
#

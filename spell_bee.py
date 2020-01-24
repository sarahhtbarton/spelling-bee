#!/usr/bin/python3

import random

letters_qty_prompt = "Enter letters per word..."
word_qty_prompt = "Please enter how many words you need..."
error_prompt = "You must enter a number, please try again..."


def user_input_check(prompt):
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
letters_qty = user_qty_entered
user_input_check(word_qty_prompt)
word_qty = user_qty_entered
print('\nYou have asked for '+str(word_qty) + ' words')
print('containing '+str(letters_qty) + ' letters\n')

wait = input("Please press enter to continue....\n")

word_wl = []

with open('words.txt', 'r') as f:
    for lines in f:
        line_contents = f.readline()
        words = line_contents.split()
        # print(words)
        for word in words:
            if len(word) == letters_qty:
                word_wl.append(word)

wl_elem = len(word_wl)

for i in range(word_qty):
    rdm_word = random.randrange(0, wl_elem)
    print(word_wl[rdm_word])

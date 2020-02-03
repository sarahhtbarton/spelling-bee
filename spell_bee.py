#!/usr/bin/python3

'''
A script to find a specific number of random english (UK) words
of a specific number of letters for use in a spelling contest.

The words are displayed in the console and you have the option
of saving the words to a plain text file.  This file will be
stored in the ./your-words directory. If the directory does
not exist, it will be created for you.

Inpired by the game "spelling bee".

THIS SCRIPT REQUIRES 'word.txt' FILE. which is a list of over
65,000 words.


'''
import random
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
save_path = dir_path + '/your_words/'

print('this is the ' + save_path)

if not os.path.exists(save_path):
    os.makedirs(save_path)

while True:
    # main programm
    file_name = 'words.txt'
    num_letter_words = []

    # very simple - get user input
    def user_input(prompt):
        number = input(prompt)
        return number

    # to check that user input is a number and not a letter
    def is_num(number):
        try:
            int(number)
            return True
        except ValueError:
            print('Oops, you must enter a number, please try again.')
            return False

    # after checking we got a number, make sure it's a positive ( >0 )
    def positive_num(number):
        if number <= 0:
            print('Ooops, the number must be greater than zero, please try again.')
            return False
        else:
            return True

    def check_letter_qty(number, file_name):
        # num_letter_words = []
        with open(file_name, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) == int(number):
                        num_letter_words.append(word)
        if not len(num_letter_words):
            print('Oops, there are no ' + number + ' letter words available, please try again.')
            return False
        else:
            return True

    # check_letter_qty(letter_qty, file_name)

    def check_word_qty(number):
        word_qty = len(num_letter_words)
        # must be int or crash
        try:
            if int(number) > len(num_letter_words):
                print('There are a maximum of ' + str(word_qty) + ' ' + str(letter_qty) + ' letter words available, please try again.')
                return False
        except ValueError:
            return False
        else:
            return True

    print()  # print a line to keep tidy

    # loop to ask user for 2 x input (one for letters,and for words)
    for ask_twice in range(2):
        if ask_twice == 0:
            # variable for user input
            prompt = "How many letters?.... "
        if ask_twice == 1:
            # variable for user input
            prompt = "How many words?.... "

        #  Two boolean variables. Start each as "False" to get into the while loop
        # both need to be true to escape the while loop (user error checking)
        result = False
        check = False
        avail = False
        done = False

        while not result or not check or not avail or not done:

            # get user input
            qty_entered = user_input(prompt)

            # error check, must be integer
            result = is_num(qty_entered)

            # check for positive number
            # all this to not trip over a value error
            # (thers is probably a better way,but I'm a noob)
            if result:
                check = positive_num(int(qty_entered))
                if check:
                    check = True
                else:
                    check = False
            else:
                check = False
            if ask_twice == 0:
                letter_qty = qty_entered
                # print(letter_qty)
                # ^ now we know how many letters the user chose
                # call to check if letter_qty actually exist
                if check:
                    avail = check_letter_qty(letter_qty, file_name)
                    if not avail:
                        avail = False
                    else:
                        avail = True
                        done = True

            if ask_twice == 1:
                word_qty = qty_entered
                avail = True
                done = True
                done = check_word_qty(word_qty)
                # ^ now we know how many words the user chose
                # call to word_qty is out of scope
                # print('(inside loop) words = ' + word_qty)
    print()  # print a line to keep tidy
    random.shuffle(num_letter_words)
    out_words = []
    words = 0
    for x in range(int(word_qty)):
        print(num_letter_words[words])
        out_words.append(num_letter_words[words])
        words += 1
    print()  # print a line to keep tidy

    # write results to a file?

    while True:
        save_file_answer = input('would you like to save the words to a file? (y/n): ')
        if save_file_answer in ('y', 'n', 'Y', 'N'):
            break
        else:
            print("Please answer 'y' or 'n' or 'Y" or 'N')

    if save_file_answer == 'y' or save_file_answer == 'Y':
        save_file = save_path + letter_qty + '_letter_words.txt'
        with open(save_file, 'w') as f:
            for w in range(int(word_qty)):
                f.write(out_words[w] + '\n')
        print()  # print a line to keep tidy
        print('Your file has been saved in... ' + '\"' + save_file + '\"')

    print()  # print a line to keep tidy

    while True:
        re_run = input('Would you like more words? (y/n): ')
        if re_run in ('y', 'n', 'Y', 'N'):
            break
        print("Please re_run 'y' or 'n'")
    if re_run == 'y' or re_run == 'Y':
        continue
    else:
        print('\nGoodbye\n')
        break

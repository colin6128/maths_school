#!/usr/bin/env python3

import os
import random
import signal
import sys
import time

# Handling interface actions


def signal_handler(signal, frame):
    print('\n You pressed Ctrl-C. Exiting program. \n')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def welcome():
    os.system("clear")
    print('Welcome to the program.')
    time.sleep(1)
    print('Loading program\n')
    time.sleep(3)
    # os.system("cowsay.tux("Welcome to the program. Maths is fun!")")
    # time.sleep(5)


def menu():
    choice = '0'
    while choice == '0':
        print('Main Menu: Choose 1 of 5 choices')
        print('Choose 1 for number sentences')
        print('Choose 2 for number bonds')
        print('Choose 3 for word problems')
        print('Choose 4 for demonstartions')
        print('Choose 5 for reference tables')
        print('Choose 4 to request further functionality')
#        print("Choose 5 to go to another menu")
        print('Choose q to quit')

        choice = input("\nPlease make a choice: ").lower()

#        if choice == "5":
#            print("Go to another menu")
#            second_menu()
        if choice == "4":
            print("\nTell someone what you want the program to do.\n")
            time.sleep(5)
            menu()
        elif choice == "3":
            print("\nLoading word problems.... \n \n")
            word_probs_menu()
        elif choice == "2":
            print("\nYou have chosen to practice number bonds. \n")
            num_bond_menu()
        elif choice == "1":
            print("\nYou have chosen number sentences. \n")
            num_sen_menu()
        elif choice == "q":
            print("\nYou have chosen to quit.\n")
            sys.exit(0)
        else:
            print("\nI don't understand your choice. Please choose again\n")
            choice = '0'


def num_sen_menu():
    #    print("This is the second menu")
    #    print("Oh. But the second menu doesn't exist yet...")
    print("Choose 1 to review a times table")
    print("Choose 2 to practice times tables")
    print("Choose 'm' to go back to the main menu")

    choice = input("\nPlease make a choice: ")

    if choice == "1":
        ttprint()
    elif choice == "2":
        test_tt_ss()
#       test_tt_single()
    elif choice == 'm':
        menu()
    else:
        print("\nI don't understand your choice. Please choose again\n")
        choice = '0'


def num_bond_menu():
    print("This is the second menu")
    print("Oh. But the second menu doesn't exist yet...")
    time.sleep(3)
    menu()


def word_probs_menu():
    print("This is the second menu")
    print("Oh. But the second menu doesn't exist yet...")
    time.sleep(3)
    menu()

# children = ['Colin', 'Sophie', 'Poppy', 'Emma', 'Eleanor', 'Thomas', 'Jake', 'Sarah', 'Graham', 'Helen', 'Ken', 'Janet', 'Louise', 'Carmen', 'Flint', 'Heather', 'Richard']

# word_items = ['chocolate', 'sweet', 'apple', 'pear', 'banana', 'currant bun', 'raisin', 'grape',
# word_items deliberately has no 's' contained to define the plural. This will be added later.

# shared_items = ['apple pie', fruit crumble', 'loaf of bread', 'pizza', 'cake',
# single_items
#
#
#

# Math definitions


def ttprint():
    os.system("clear")
    n = int(input("Input a number for the times table you wish to display: "))
    # use for loop to iterate 12 times
    print('\n\nThe', n, 'times table:')
    for i in range(0, 13):
        print(n, 'x', i, '=', n * i)
    end = input("\nPress 'm' to return to the menu\n")
    if end == 'm':
        os.system("clear")
        menu()
    else:
        print("That makes no sense. I asked for an 'm'. I'm quitting.")


def test_tt_single():
    n = int(input("Input a number to test your times tables: "))
    os.system("clear")
    print('You have chosen the', n, 'times table. Good luck!')
    x = random.randint(0, 12)
    print(n, 'x', x, '= ')
    s = int(input())
    sol = int(n * x)
    if s == sol:
        os.system("clear")
        print('Correct!')
    else:
        print('Practice makes perfect')


def test_tt_ss():
    correct = 0
    wrong = 0
    questions = 10
    n = int(input("Input a number to test your times tables: "))
    os.system("clear")
    print('You have chosen the', n, 'times table. Good luck! \n')
    # print("Press 'q' to quit.")
    while questions > 0:
        x = random.randint(0, 12)
        print(n, 'x', x, '= ')
        s = int(input())
        sol = int(n * x)
        if s == sol:
            print('Correct! \n')
            correct += 1
        else:
            print('Practice makes perfect \n')
            wrong += 1
        questions -= 1

    print('Well done! You scored', correct, 'out of', correct + wrong, ' \n')
    time.sleep(5)
    menu()


def num_sent():
    os.system("clear")
    print("To be created")
    time.sleep(5)
    menu()


# The man program
welcome()
menu()

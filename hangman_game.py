# core concepts
'''
5. Hangman

The Goal: Despite the name, the actual “hangman” part isn’t necessary.
The main goal here is to create a sort of “guess the word” game. The user needs to be able to input letter guesses.
A limit should also be set on how many guesses they can use. This means you’ll need a way to grab a word to use for guessing.
(This can be grabbed from a pre-made list. No need to get too fancy.)
You will also need functions to check if the user has actually inputted a single letter,
to check if the inputted letter is in the hidden word (and if it is, how many times it appears), to print letters,
and a counter variable to limit guesses.
Concepts to keep in mind:

Random
Variables
Boolean
Input and Output
Integer
Char
String
Length
Print
'''

# pseudo code and definitions

'''
import random to select a random word from a tuple
create string variables with different body parts to call upon
create a tuple that can be read from and selected when called upon
create an integer variable to show the number of tries 
create a boolean to loop the program if the user wants to try again
create a while loop to loop the game and add a break if the user says no(add a print out)
create a boolean to determine if a word is guessed correctly
create another while loop to break out of when the word is guessed or if the tries are used up
in the 2nd while loop make sure to += 1 to the tries

'''


import random

import hangman_index

from hangman_index import words, hangman

rules = str(input("Hangman game"
      "Would you like to see the rules? (y/n)"))

if rules == "y":
    print("Rules: A random word is selected and you get to see how many characters there are in the word.\n"
      "       Guess a letter or the complete word and see if you got it right.\n"
      "       If you guess a letter and it is in the word, it will be added to the character line.\n"
      "       Also, if you guess wrong a portion of the hangman is drawn and you get to try again.\n"
      "       If you make 8 wrong guesses and the hung man is fully drawn, you lose!\n"
      "Okay! lets begin!")
else:
    print("Okay! lets begin!")




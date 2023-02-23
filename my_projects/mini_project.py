#!/usr/bin/env python3
import random
import os

def main():
    wordbank = ["python", "linux", "programming", "software", "engineer", "computer", "java", "javascript", "aws", "html", "css", "learning"]
    guesses = []
    turn = 15

    print("Welcome to secret word! Can you guess the secret word before time runs out?")
    input("To begin, hit enter!")

    clear_console()
    
    word = wordbank[random.randrange(len(wordbank))]
    win = len(word)

    while turn>0:
        if win == 0:
            input(f"Congratulations! You guessed the secret word {word}!")
            break
        print("Guesses remaining: ", turn)
        print("Secret Word: ")
        for letter in word:
            if letter in guesses:
                print(letter, end='')
            else:
                print("_", end='')

        print("\nLetters guessed so far: ")
        for letter in guesses:
            print(letter, end='')

        guess=input("\nGuess a letter: ")

        if testLetter(guess, word) == True:
            input(f"Correct! {guess} is in the secret word.")
            guesses.append(guess)
            for letter in word:
                if letter == guess:
                    win = win-1
        else:
            input(f"Sorry, {guess} is not in the secret word.")
            guesses.append(guess)
            
        turn=turn-1

        clear_console()
    if win>0:
        input(f"Sorry, you did not guess the secret word {word}.")

        
def testLetter(x, word):
    for letter in word:
        if letter == x:
            return True
    return False

def clear_console():
    os.system('clear')

main()

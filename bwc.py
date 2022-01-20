#!/usr/bin/env python3

"""
Brad's Wordle Clone
"""

import random
import string
from colorama import Fore, Back, Style

WORD_LENGTH = 5
TURN = 1
ALPHABET = list(string.ascii_uppercase)

def select_random_word():
    """Selects a random word."""
    while True:
        random_word = random.choice(WORDS)
        word = ''.join(filter(str.isalpha, random_word))
        if len(word) == WORD_LENGTH:
            return word.upper()

def enter_word_guess():
    """Take in a word guess and validate input."""
    while True:
        raw_input = input(f"[{TURN}] >>> ")
        word = ''.join(filter(str.isalpha, raw_input.lower()))
        if len(word) != WORD_LENGTH:
            print(f"{Fore.RED}Word must be {WORD_LENGTH} characters long.{Style.RESET_ALL}")
        elif word not in WORDS:
            print(f"{Fore.RED}Word not in dictionary.{Style.RESET_ALL}")
        else:
            return word.upper()

def analyze_guess():
    """Tests letters and letter positions."""
    result = []
    for position, (word, guess) in enumerate(zip(THE_WORD, THE_GUESS)):
        if guess == word:
            result.insert(position, f"{Style.BRIGHT}{Fore.WHITE}{Back.BLUE}{guess}{Style.RESET_ALL}")
        elif guess in THE_WORD:
            result.insert(position, f"{Style.BRIGHT}{Fore.WHITE}{Back.YELLOW}{guess}{Style.RESET_ALL}")
        else:
            letter = ALPHABET.index(guess)
            ALPHABET[letter] = f"{Style.BRIGHT}{Fore.WHITE}{Back.BLACK}{ALPHABET[letter]}{Style.RESET_ALL}"
            result.insert(position, guess)
    return result

with open("words", 'r') as word_list:
    WORDS = word_list.read().splitlines()

THE_WORD = select_random_word()

while True:
    THE_GUESS = enter_word_guess()
    if THE_GUESS == THE_WORD:
        print(f"{Style.BRIGHT}{Fore.WHITE}{Back.MAGENTA}CONGRATS!{Style.RESET_ALL}")
        break
    THE_ANALYSIS = analyze_guess()
    print("".join(THE_ANALYSIS))
    print("".join(ALPHABET))
    TURN = TURN + 1
    if TURN == 5:
        print(f"{Style.BRIGHT}{Fore.WHITE}{Back.RED}THE_WORD{Style.RESET_ALL}")
        break

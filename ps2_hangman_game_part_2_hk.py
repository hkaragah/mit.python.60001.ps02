# Hangman Game
# -----------------------------------

import random
import string

# -----------------------------------
# loading the word pool

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


# -----------------------------------
# choosing a random word from the word pool

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    for letter_of_secret in secret_word:
        found_common_letter = False
        for letter_of_guessed in letters_guessed:
            if letter_of_secret == letter_of_guessed:
                found_common_letter = True
                break
        if not (found_common_letter):
            return False
            break
    if found_common_letter:
        return True


def is_letter_guessed(letter, secret_word):
    '''
    :param letter: string, letter to be examined whether is in secret word
    :param secret_word: string, reference word to be used for 'letter' examination
    :return: boolean, True is 'letter' exists in 'secret word', otherwise is False
    '''

    letter_found = False
    for character in secret_word:
        if character == letter:
            letter_found = True
            break
    return letter_found



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    correctly_guessed = ''
    for letter_of_secret in secret_word:
        found_common_letter = False
        for letter_of_guessed in letters_guessed:
            if letter_of_secret == letter_of_guessed:
                found_common_letter = True
                correctly_guessed += letter_of_guessed
                break
        if not (found_common_letter):
            correctly_guessed += '_ '
    return correctly_guessed


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = string.ascii_lowercase
    for letter in letters_guessed:
        available_letters = available_letters.replace(letter, '')
    return available_letters


def already_guessed(letter, letters_guessed):
    '''
    letter: string, geussed letter by user

    letters_guessed: string, all available lowercase alphabets
    that has already been gueesed

    If the 'letter' has already been guessed, i.e.,
    is within the 'letters_guessed', returns True,
    otherwise return False

    '''
    letter_already_guessed = False
    for guess in letters_guessed:
        if letter == guess:
            letter_already_guessed = True
            break
    return letter_already_guessed


def a_vowel(letter):
    '''
    letter: string, geussed letter by user

    check whether guessed letter is a vowel, a, e, i, o, u.
    '''
    vowels = 'aeiou'
    is_vowel = False
    for vowel in vowels:
        if letter == vowel:
            is_vowel = True
            break
    return is_vowel


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    guesses_remaining = 6
    warnings_remaining = 3
    choose_word(wordlist)
    letters_guessed = []
    score = 0
    available_letters = string.ascii_lowercase

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
    print('---------------')

    while guesses_remaining > 0:

        print('You have ' + str(guesses_remaining) + ' guesses left.')
        print('Available letters: ' + available_letters)

        letter = input('Please guess a letter:')
        letter = str.lower(letter)

        # checking the guessed letter
        if not (str.isalpha(letter)):
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print('Oops! The input is not an alphabet. You now have ' + str(warnings_remaining) + ' warnings left.')
            else:
                guesses_remaining -= 1

        elif already_guessed(letter, letters_guessed):
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print('Oops! You\'ve already guessed that letter. You now have ' + str(
                    warnings_remaining) + ' warnings left.')
            else:
                guesses_remaining -= 1

        else:
            letters_guessed.append(letter)
            available_letters = get_available_letters(letters_guessed)
            if is_letter_guessed(letter,secret_word):
                print('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
                print('---------------')
            else:
                if a_vowel(letter):
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print('Oops! that letter is not in my word: ' + get_guessed_word(secret_word, letters_guessed))
                print('---------------')

        # checking the guessed word
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
            score += guesses_remaining * len(letters_guessed)
            print('Congradulations, you won!')
            print('Your total score for this game is: ' + str(score))
            break

    if score == 0:
        print('The secret word was ' + secret_word)
        print('It\'s very unfortunate, you lost!')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)

wanna_play_more = True
while wanna_play_more:
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    answer = input('Do you wanna play more (Y/N)? ')
    if answer != 'Y' or answer != 'y':
        wanna_play_more = False


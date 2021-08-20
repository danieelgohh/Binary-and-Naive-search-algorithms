import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly picks a word from the word list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # letters that the user has guessed

    lives = 6

    # user input
    while len(word_letters) > 0 and lives > 0:
        # notify letter used
        #' '.join(['a','b','cd']) => 'a b cd
        print('You have', lives, 'lives left and these letters are used: ', ' '.join(used_letters))

        # what the current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # if letter is wrong takes a life away
                print('Letter is not part of the word!')

        elif user_letter in used_letters:
            print('This alphabet has been used!')

        else:
            print('Invalid character, please try again!')

    # when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, the word was', word)
    else:
        print('Congratulations, you guessed the word', word,'.')
        
hangman()

import random
from words import words
import string

def get_valid_word(words):
    ''' what we are doing is basically trying to get a random word from the list of words
    in the file words.py '''
    word = random.choice(words) 

    ''' in here we are checking if our word contains spaces or underscores , in that case we 
    should keep on choosing a random word unless there is no space or _ '''
    while '_' in word or ' ' in word:
        word = random.choice(words) 
    

    return word

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word) # this will contain set of all the letters in the word
    alphabet = set(string.ascii_uppercase) #this will contain the set of uppercase alphabets
    used_letters = set() #this will contain the set of words the user has guessed

    while len(word_letters) > 0:
        #we will keep on repeating these tasks unless our set of word letters is empty
        #once the set of word letters is empty it tells that all letters have been guessed correctly

        #this statemnt to show the letters which we have used already
        print("You have used these letters:",' '.join(used_letters))

       

        user_letter = input('Guess a letter:').upper() #this will take a letter as input from the user
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You have already used that character.Please try again.")

        else:
            print("You typed an invalid character!")

         #what current word is
        word_list =[letter if letter in used_letters else '_' for letter in word]
        print('Current word:',' '.join(word_list))



hangman()




# Python Program to illustrate  
# Hangman Game 
import random 
from collections import Counter 
  
someWords = '''apple banana mango strawberry peach pear
jackfruit dragonfruit orange greengrape starfruit
pineapple apricot fig lemon coconut watermelon
blueberry blackgrape cherry papaya gooseberry
peach guava kiwi raspberry pomegranate lychee muskmelon'''
  
someWords = someWords.split(' ') 
# randomly choose a secret word from our "someWords" LIST. 
word = random.choice(someWords)          
  
if __name__ == '__main__': 
    print('Guess the word! HINT: word is a name of a fruit') 
      
    for i in word: 
         # For printing the empty spaces for letters of the word 
        print('_', end = ' ')         
    print() 
  
    playing = True
     # list for storing the letters guessed by the player 
    letterGuessed = ''                 
    chances = len(word) + 2
    correct = 0
    flag = 0
    try: 
        while (chances != 0) and flag == 0: #flag is updated when the word is correctly guessed  
            print() 
            chances -= 1
  
            try: 
                guess = str(input('Enter a letter to guess: ')) 
            except: 
                print('Enter only a letter!') 
                continue
  
            # Validation of the guess 
            if not guess.isalpha(): 
                print('Enter only a LETTER') 
                continue
            elif len(guess) > 1: 
                print('Enter only a SINGLE letter') 
                continue
            elif guess in letterGuessed: 
                print('You have already guessed that letter') 
                continue
  
  
            # If letter is guessed correctly 
            if guess in word: 
                k = word.count(guess) #k stores the number of times the guessed letter occurs in the word 
                for _ in range(k):     
                    letterGuessed += guess # The guess letter is added as many times as it occurs 
  
            # Print the word 
            for char in word: 
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): 
                    print(char, end = ' ') 
                    correct += 1
                # If user has guessed all the letters 
                elif (Counter(letterGuessed) == Counter(word)): # Once the correct word is guessed fully,  
                                                                # the game ends, even if chances remain 
                    print("The word is: ", end=' ') 
                    print(word) 
                    flag = 1
                    print('Congratulations, You won!') 
                    break # To break out of the for loop 
                    break # To break out of the while loop 
                else: 
                    print('_', end = ' ') 
  
              
  
        # If user has used all of his chances 
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)): 
            print() 
            print('You lost! Try again..') 
            print('The word was {}'.format(word)) 
  
    except KeyboardInterrupt: 
        print() 
        print('Bye! Try again.') 
        exit() 



someWords2 = '''pk 3idiots dhoom dabangg masaan endgame
dangal mardaani lagaan bodygaurd singham simmba joker commando
frozen gravity agneepath ishaqzaade aashiqui rockstar
naagin housefull kesari chandramukhi uri rustom war chhichhore
manikarnika bharat badla kalank junglee panipat baazigar
shehenshah darr pagalpanti don blank black baghban wanted sooryavansham
wanted heropanti holiday dhamaal sholay notebook fitoor malaal raees dilwale'''
  
someWords = someWords2.split(' ') 
# randomly choose a secret word from our "someWords" LIST. 
word2 = random.choice(someWords)          
  
if __name__ == '__main__': 
    print('Guess the word! HINT: word is a name of a movie') 
      
    for i in word2: 
         # For printing the empty spaces for letters of the word 
        print('_', end = ' ')         
    print() 
  
    playing = True
     # list for storing the letters guessed by the player 
    letterGuessed = ''                 
    chances = len(word2) + 2
    correct = 0
    flag = 0
    try: 
        while (chances != 0) and flag == 0: #flag is updated when the word is correctly guessed  
            print() 
            chances -= 1
  
            try: 
                guess = str(input('Enter a letter to guess: ')) 
            except: 
                print('Enter only a letter!') 
                continue
  
            # Validation of the guess 
            if not guess.isalpha(): 
                print('Enter only a LETTER') 
                continue
            elif len(guess) > 1: 
                print('Enter only a SINGLE letter') 
                continue
            elif guess in letterGuessed: 
                print('You have already guessed that letter') 
                continue
  
  
            # If letter is guessed correctly 
            if guess in word2: 
                k = word.count(guess) #k stores the number of times the guessed letter occurs in the word 
                for _ in range(k):     
                    letterGuessed += guess # The guess letter is added as many times as it occurs 
  
            # Print the word 
            for char in word2: 
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): 
                    print(char, end = ' ') 
                    correct += 1
                # If user has guessed all the letters 
                elif (Counter(letterGuessed) == Counter(word)): # Once the correct word is guessed fully,  
                                                                # the game ends, even if chances remain 
                    print("The word is: ", end=' ') 
                    print(word2) 
                    flag = 1
                    print('Congratulations, You won!') 
                    break # To break out of the for loop 
                    break # To break out of the while loop 
                else: 
                    print('_', end = ' ') 
  
              
  
        # If user has used all of his chances 
        if chances <= 0 and (Counter(letterGuessed) != Counter(word2)): 
            print() 
            print('You lost! Try again..') 
            print('The word was {}'.format(word2)) 
  
    except KeyboardInterrupt: 
        print() 
        print('Bye! Try again.') 
        exit() 




someWords3 = '''cyan blue black red orange magenta teal brown violet
indigo green yellow white purple golden silver grey olive
coral lime crimson pink maroon wine skin beige peach blush
fuscia henna neon hazel'''
  
someWords = someWords3.split(' ') 
# randomly choose a secret word from our "someWords" LIST. 
word3 = random.choice(someWords)          
  
if __name__ == '__main__': 
    print('Guess the word! HINT: word is a name of a colour') 
      
    for i in word3: 
         # For printing the empty spaces for letters of the word 
        print('_', end = ' ')         
    print() 
  
    playing = True
     # list for storing the letters guessed by the player 
    letterGuessed = ''                 
    chances = len(word3) + 2
    correct = 0
    flag = 0
    try: 
        while (chances != 0) and flag == 0: #flag is updated when the word is correctly guessed  
            print() 
            chances -= 1
  
            try: 
                guess = str(input('Enter a letter to guess: ')) 
            except: 
                print('Enter only a letter!') 
                continue
  
            # Validation of the guess 
            if not guess.isalpha(): 
                print('Enter only a LETTER') 
                continue
            elif len(guess) > 1: 
                print('Enter only a SINGLE letter') 
                continue
            elif guess in letterGuessed: 
                print('You have already guessed that letter') 
                continue
  
  
            # If letter is guessed correctly 
            if guess in word3: 
                k = word.count(guess) #k stores the number of times the guessed letter occurs in the word 
                for _ in range(k):     
                    letterGuessed += guess # The guess letter is added as many times as it occurs 
  
            # Print the word 
            for char in word3: 
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): 
                    print(char, end = ' ') 
                    correct += 1
                # If user has guessed all the letters 
                elif (Counter(letterGuessed) == Counter(word3)): # Once the correct word is guessed fully,  
                                                                # the game ends, even if chances remain 
                    print("The word is: ", end=' ') 
                    print(word3) 
                    flag = 1
                    print('Congratulations, You won!') 
                    break # To break out of the for loop 
                    break # To break out of the while loop 
                else: 
                    print('_', end = ' ') 
  
              
  
        # If user has used all of his chances 
        if chances <= 0 and (Counter(letterGuessed) != Counter(word2)): 
            print() 
            print('You lost! Try again..') 
            print('The word was {}'.format(word3)) 
  
    except KeyboardInterrupt: 
        print() 
        print('Bye! Try again.') 
        exit() 




someWords4 = '''cyan blue black red orange magenta teal brown violet
indigo green yellow white purple golden silver grey olive
coral lime crimson pink maroon wine skin beige peach blush
fuscia henna neon hazel'''
  
someWords = someWords4.split(' ') 
# randomly choose a secret word from our "someWords" LIST. 
word4 = random.choice(someWords)          
  
if __name__ == '__main__': 
    print('Guess the word! HINT: word is a name of an element of periodic table') 
      
    for i in word4: 
         # For printing the empty spaces for letters of the word 
        print('_', end = ' ')         
    print() 
  
    playing = True
     # list for storing the letters guessed by the player 
    letterGuessed = ''                 
    chances = len(word4) + 2
    correct = 0
    flag = 0
    try: 
        while (chances != 0) and flag == 0: #flag is updated when the word is correctly guessed  
            print() 
            chances -= 1
  
            try: 
                guess = str(input('Enter a letter to guess: ')) 
            except: 
                print('Enter only a letter!') 
                continue
  
            # Validation of the guess 
            if not guess.isalpha(): 
                print('Enter only a LETTER') 
                continue
            elif len(guess) > 1: 
                print('Enter only a SINGLE letter') 
                continue
            elif guess in letterGuessed: 
                print('You have already guessed that letter') 
                continue
  
  
            # If letter is guessed correctly 
            if guess in word4: 
                k = word.count(guess) #k stores the number of times the guessed letter occurs in the word 
                for _ in range(k):     
                    letterGuessed += guess # The guess letter is added as many times as it occurs 
  
            # Print the word 
            for char in word4: 
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): 
                    print(char, end = ' ') 
                    correct += 1
                # If user has guessed all the letters 
                elif (Counter(letterGuessed) == Counter(word3)): # Once the correct word is guessed fully,  
                                                                # the game ends, even if chances remain 
                    print("The word is: ", end=' ') 
                    print(word4) 
                    flag = 1
                    print('Congratulations, You won!') 
                    break # To break out of the for loop 
                    break # To break out of the while loop 
                else: 
                    print('_', end = ' ') 
  
              
  
        # If user has used all of his chances 
        if chances <= 0 and (Counter(letterGuessed) != Counter(word2)): 
            print() 
            print('You lost! Try again..') 
            print('The word was {}'.format(word4)) 
  
    except KeyboardInterrupt: 
        print() 
        print('Bye! Try again.') 
        exit() 

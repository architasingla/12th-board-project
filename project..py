
import random


while True:
    
    print("WELCOME TO GAMES!!!")
    print()
    print("Pick the game of your choice from the following:")
    print("1. Jumbled Words")
    print("2. Hangman")
    print("3. Tic Tac Toe")
    print()
    game=int(input("Enter the chosen game number: "))
    print()



    #---------Game 1---------



    if game==1:
        # Python program for jumbled words game. 

        welcome = ["Welcome to Jumbled Words!",
                  "This is a two player game. You will be given a jumbled set of letters of a fruit",
                  "and each player gets one chance to decode it. Enjoy!"
                    ]

        for line in welcome:
            print(line, sep='\n')
        print()
            
        # function for choosing random word. 
        def choose(): 
            # list of word 
            words = ['apple', 'banana', 'mango', 'strawberry', 'peach', 'pear',
                    'jackfruit', 'dragonfruit', 'orange', 'greengrape', 'starfruit',
                    'pineapple', 'apricot', 'fig', 'lemon', 'coconut', 'watermelon',
                    'blueberry', 'blackgrape', 'cherry', 'papaya', 'gooseberry',
                    'peach', 'guava', 'kiwi', 'raspberry', 'pomegranate', 'lychee', 'muskmelon'] 
      
             # choice() method randomly choose 
            # any word from the list. 
            pick = random.choice(words) 
            return pick 
      
            # Function for shuffling the 
            # characters of the chosen word. 
        def jumble(word): 
            # sample() method shuffling the characters of the word 
            random_word = random.sample(word, len(word)) 
      
            # join() method join the elements 
            # of the iterator(e.g. list) with particular character . 
            jumbled = ''.join(random_word) 
            return jumbled 
      
      
        # Function for showing final score. 
        def thank(p1n, p2n, p1, p2): 
            print(p1n, 'Your score is :', p1) 
            print(p2n, 'Your score is :', p2) 
      
            # check_win() function calling 
            check_win(p1n, p2n, p1, p2) 
      
            print('Thanks for playing...') 
      
      
        # Function for declaring winner 
        def check_win(player1, player2, p1score, p2score): 
            if p1score > p2score: 
                print("winner is :", player1) 
            elif p2score > p1score: 
                print("winner is :", player2) 
            else: 
                print("Draw..Well Played guys..") 
      
      
        # Function for playing the game. 
        def play(): 
            # enter player1 and player2 name 
            p1name = input("Player 1, please enter your name: ") 
            p2name = input("Player 2 , please enter your name: ") 
      
            # variable for counting score. 
            pp1 = 0
            pp2 = 0
      
            # variable for counting turn 
            turn = 0
      
            # keep looping 
            while True: 
      
                # choose() function calling 
                picked_word = choose() 
      
                # jumble() fucntion calling 
                qn = jumble(picked_word) 
                print("The jumbled word is: ", qn) 
      
                # checking turn is odd or even 
                if turn % 2 == 0: 
      
                    # if turn no. is even 
                    # player1 turn 
                    print(p1name, 'Your Turn.') 
      
                    ans = input("What is in your mind? ") 
      
                    # checking ans is equal to picked_word or not 
                    if ans == picked_word: 
      
                        # incremented by 1 
                        pp1 += 1
      
                        print('Your score is :', pp1) 
                        turn += 1
      
                    else: 
                        print("Better luck next time...") 
      
                        # player 2 turn 
                        print(p2name, 'Your turn.') 
      
                        ans = input('What is in your mind? ') 
      
                        if ans == picked_word: 
                            pp2 += 1
                            print("Your Score is: ", pp2) 
      
                        else: 
                            print("Better luck next time..."
                                  "The correct word is: ", picked_word) 
      
                        c = int(input("Press 1 to continue and 0 to quit: ")) 
      
                        # checking the c is equal to 0 or not 
                        # if c is equal to 0 then break out 
                        # of the while loop o/w keep looping. 
                        if c == 0: 
                            # thank() function calling 
                            thank(p1name, p2name, pp1, pp2) 
                            break
      
                else: 
      
                    # if turn no. is odd 
                    # player2 turn 
                    print(p2name, 'Your turn.') 
                    ans = input('What is in your mind? ') 
      
                    if ans == picked_word: 
                        pp2 += 1
                        print("Your Score is :", pp2) 
                        turn += 1
      
                    else: 
                        print("Better luck next time.. :") 
                        print(p1name, 'Your turn.') 
                        ans = input('What is in your mind? ') 
      
                        if ans == picked_word: 
                            pp1 += 1
                            print("Your Score is :", pp1) 
      
                        else: 
                            print("Better luck next time..."
                                  "The correct word is :", picked_word) 
      
                            c = int(input("Press 1 to continue and 0 to quit: ")) 
      
                            if c == 0: 
                                # thank() function calling 
                                thank(p1name, p2name, pp1, pp2) 
                                break
      
                    c = int(input("Press 1 to continue and 0 to quit: ")) 
                    if c == 0: 
                        # thank() function calling 
                        thank(p1name, p2name, pp1, pp2) 
                        break
      
      
        # Driver code 
        if __name__ == '__main__': 
          
            # play() function calling 
            play()



    #---------Game 2---------



    elif game==2:
        # Python program for Hangman Game.
        
        """ In a standard game of Hangman, a word is chosen at random from a list and the
        user must guess the word letter by letter before running out of attempts."""


        def main():
            welcome = ['Welcome to Hangman! A word will be chosen at random and',
                       'you must try to guess the word correctly letter by letter',
                       'before you run out of attempts. Good luck!',
                       'Here, the word will be a bollywood movie.'
                       ]

            for line in welcome:
                print(line, sep='\n')
            print()
            # setting up the play_again loop

            play_again = True

            while play_again:
                # set up the game loop

                words = ['pk', '3idiots', 'dhoom', 'dabangg', 'masaan', 'aakrosh', 'aarakshan',
                        'dangal', 'mardaani', 'lagaan', 'bodygaurd', 'singham', 'simmba', 'joker', 'commando',
                        'agneepath', 'ishaqzaade', 'aashiqui', 'rockstar',
                        'naagin', 'housefull', 'kesari', 'chandramukhi', 'uri', 'rustom', 'war', 'chhichhore',
                        'manikarnika', 'bharat', 'badla', 'kalank', 'junglee', 'panipat', 'baazigar',
                        'shehenshah', 'darr', 'pagalpanti', 'don', 'black', 'baghban', 'wanted', 'sooryavansham',
                        'wanted', 'heropanti', 'holiday', 'dhamaal', 'sholay', 'fitoor', 'malaal', 'raees', 'dilwale']

                chosen_word = random.choice(words).lower()
                player_guess = None # will hold the players guess
                guessed_letters = [] # a list of letters guessed so far
                word_guessed = []
                for letter in chosen_word:
                    word_guessed.append("-") # create an unguessed, blank version of the word
                joined_word = None # joins the words in the list word_guessed

                HANGMAN = (
        """
        -----
        |   |
        |
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        |  -+-
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  | 
        |  | 
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  | | 
        |  | 
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  | | 
        |  | | 
        |
        --------
        """)

                print(HANGMAN[0])
                attempts = len(HANGMAN) - 1


                while (attempts != 0 and "-" in word_guessed):
                    print(("\nYou have {} attempts remaining").format(attempts))
                    joined_word = "".join(word_guessed)
                    print(joined_word)

                    try:
                        player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
                    except: # check valid input
                        print("That is not valid input. Please try again.")
                        continue                
                    else: 
                        if not player_guess.isalpha(): # check the input is a letter. Also checks an input has been made.
                            print("That is not a letter. Please try again.")
                            continue
                        elif len(player_guess) > 1: # check the input is only one letter
                            print("That is more than one letter. Please try again.")
                            continue
                        elif player_guess in guessed_letters: # check it letter hasn't been guessed already
                            print("You have already guessed that letter. Please try again.")
                            continue
                        else:
                            pass

                    guessed_letters.append(player_guess)

                    for letter in range(len(chosen_word)):
                        if player_guess == chosen_word[letter]:
                            word_guessed[letter] = player_guess # replace all letters in the chosen word that match the players guess

                    if player_guess not in chosen_word:
                        attempts -= 1
                        print(HANGMAN[(len(HANGMAN) - 1) - attempts])

                if "-" not in word_guessed: # no blanks remaining
                    print(("\nCongratulations! {} was the word").format(chosen_word))
                else: # loop must have ended because attempts reached 0
                    print(("\nUnlucky! The word was {}.").format(chosen_word))

                print("\nWould you like to play again?")

                response = input("> ").lower()
                if response not in ("yes", "y"):
                    play_again = False

        if __name__ == "__main__":
            main()


    #---------Game 3---------



    elif game==3:
        # Tic Tac Toe

        def drawBoard(board):
            # This function prints out the board that it was passed.

            # "board" is a list of 10 strings representing the board (ignore index 0)
            print('   |   |')
            print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
            print('   |   |')

        def inputPlayerLetter():
            # Let's the player type which letter they want to be.
            # Returns a list with the player's letter as the first item, and the computer's letter as the second.
            letter = ''
            while not (letter == 'X' or letter == 'O'):
                print('Do you want to be X or O?')
                letter = input().upper()

            # the first element in the tuple is the player's letter, the second is the computer's letter.
            if letter == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']

        def whoGoesFirst():
            # Randomly choose the player who goes first.
            if random.randint(0, 1) == 0:
                return 'computer'
            else:
                return 'player'

        def playAgain():
            # This function returns True if the player wants to play again, otherwise it returns False.
            print('Do you want to play again? (yes or no)')
            return input().lower().startswith('y')

        def makeMove(board, letter, move):
            board[move] = letter

        def isWinner(bo, le):
            # Given a board and a player's letter, this function returns True if that player has won.
            # We use bo instead of board and le instead of letter so we don't have to type as much.
            return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

        def getBoardCopy(board):
            # Make a duplicate of the board list and return it the duplicate.
            dupeBoard = []

            for i in board:
                dupeBoard.append(i)

            return dupeBoard

        def isSpaceFree(board, move):
            # Return true if the passed move is free on the passed board.
            return board[move] == ' '

        def getPlayerMove(board):
            # Let the player type in his move.
            move = ' '
            while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
                print('What is your next move? (1-9)')
                move = input()
            return int(move)

        def chooseRandomMoveFromList(board, movesList):
            # Returns a valid move from the passed list on the passed board.
            # Returns None if there is no valid move.
            possibleMoves = []
            for i in movesList:
                if isSpaceFree(board, i):
                    possibleMoves.append(i)

            if len(possibleMoves) != 0:
                return random.choice(possibleMoves)
            else:
                return None

        def getComputerMove(board, computerLetter):
            # Given a board and the computer's letter, determine where to move and return that move.
            if computerLetter == 'X':
                playerLetter = 'O'
            else:
                playerLetter = 'X'

            # Here is our algorithm for our Tic Tac Toe AI:
            # First, check if we can win in the next move
            for i in range(1, 10):
                copy = getBoardCopy(board)
                if isSpaceFree(copy, i):
                    makeMove(copy, computerLetter, i)
                    if isWinner(copy, computerLetter):
                        return i

            # Check if the player could win on his next move, and block them.
            for i in range(1, 10):
                copy = getBoardCopy(board)
                if isSpaceFree(copy, i):
                    makeMove(copy, playerLetter, i)
                    if isWinner(copy, playerLetter):
                        return i

            # Try to take one of the corners, if they are free.
            move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
            if move != None:
                return move

            # Try to take the center, if it is free.
            if isSpaceFree(board, 5):
                return 5

            # Move on one of the sides.
            return chooseRandomMoveFromList(board, [2, 4, 6, 8])

        def isBoardFull(board):
            # Return True if every space on the board has been taken. Otherwise return False.
            for i in range(1, 10):
                if isSpaceFree(board, i):
                    return False
            return True


        print('Welcome to Tic Tac Toe!')

        while True:
            # Reset the board
            theBoard = [' '] * 10
            playerLetter, computerLetter = inputPlayerLetter()
            turn = whoGoesFirst()
            print('The ' + turn + ' will go first.')
            gameIsPlaying = True

            while gameIsPlaying:
                if turn == 'player':
                    # Player's turn.
                    drawBoard(theBoard)
                    move = getPlayerMove(theBoard)
                    makeMove(theBoard, playerLetter, move)

                    if isWinner(theBoard, playerLetter):
                        drawBoard(theBoard)
                        print('Hooray! You have won the game!')
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'computer'

                else:
                    # Computer's turn.
                    move = getComputerMove(theBoard, computerLetter)
                    makeMove(theBoard, computerLetter, move)

                    if isWinner(theBoard, computerLetter):
                        drawBoard(theBoard)
                        print('The computer has beaten you! You lose.')
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'player'

            if not playAgain():
                break



    else:
        print("Invalid Entry!"
              "Please enter a valid number (a number from 1 to 3)")
        
    print()
    a=int(input("Enter 1 to change the game and 0 to quit"))
    if a==0:
        break
    print()
        

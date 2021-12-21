from hangmanpics import HANGMANPICS

# Initalizaions

# Scores
number_of_wins = 0
number_of_loses = 0


def printScore():
    print("Wins: {}".format(number_of_wins))
    print("Loses: {}".format(number_of_loses))


def win():
    print("You Won!!! ")
    printScore()


def gameOver():
    print("Game Over")
    printScore()


def lose():
    print("You Lost")
    printScore()

def guess_letter_validation():
    while 1:
        guessed_letter = input("Enter your guess: ").lower()
        if guessed_letter.isalpha and len(guessed_letter) == 1:
            return guessed_letter
        else: 
            print("Invalid input. Try again.\n")

def guess_word_validation():
    while 1:
        guessed_word = input("Enter your guess: ").lower()
        if guessed_word.isalpha():
            return guessed_word
        else:
            print("Invalid input. Try again.\n")
            


# Start a game
def start():

    number_of_guesses = 7
    global number_of_wins
    global number_of_loses

    gameOn = True

    while gameOn:
        
        play_again = input("\nDo you want to start a new game (y/n)? ").lower()

        if play_again == 'n':
            gameOver()
            gameOn = False
            break;

        number_of_guesses = 7
        #- Randomly choose a word from the word_list and assign it to a variable called chosen_word.
        # chosen_word = random.choice(word_list)

        

        chosen_word = "wer".lower()
        #- Create an empty List called display.
        #For each letter in the chosen_word, add a "_" to 'display'.
        display = list(chosen_word)
        for i in range(len(display)):
            display[i] = '_'

        while '_' in display:
            
            

            if number_of_guesses == 0:
                print("\nYou are out of guesses.\nThe correct word was: {}".format(chosen_word))
                lose()
                break;
            
            print(HANGMANPICS[number_of_guesses-1])
            # display the word
            print(f"{' '.join(display)}")
           

            # ask user to choose letter or word
            letter_or_word = input("\nDo you want to guess a letter or a word (l/w)? ")
            if letter_or_word == 'l':
                # validate that the input is a single letter
                guessed_letter = guess_letter_validation()

                if guessed_letter not in chosen_word:
                    print("{} in not in the word".format(guessed_letter))
                    number_of_guesses -= 1
                
                else:
                    for i in range(len(chosen_word)):
                        if chosen_word[i] == guessed_letter:
                            display[i] = guessed_letter


            elif letter_or_word == 'w':
                guessed_word = guess_word_validation()

                if guessed_word == chosen_word:
                    number_of_wins += 1 
                    for i in range(len(chosen_word)):
                        display[i] = chosen_word[i]                    
                else:
                    number_of_guesses -= 1
                    print("Your guess was incorrect.")

            else:
                print('Invalid input. Try again.\n')
            
        else:
            win()
             # display the word
            print(f"{' '.join(display)}")



start()


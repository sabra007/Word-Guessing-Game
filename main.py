from hangmanpics import HANGMANPICS
import json
import random

# Setup

# Loading JSON file
# create a list from dict keys
with open('words_dictionary.json') as f:
    data = json.load(f)
    word_list = list(data.keys())

# Scores
number_of_wins = 0
number_of_loses = 0


def printScore():
    print("Wins: {}".format(number_of_wins))
    print("Loses: {}".format(number_of_loses))


def win():
    global number_of_wins
    number_of_wins += 1
    print("You Won!!! ")
    printScore()

def lose():
    global number_of_loses
    number_of_loses += 1
    print("You Lost")
    printScore()

def gameOver():
    print("Game Over")
    printScore()


def guess_letter_validation():
    while 1:
        guessed_letter = input("Enter your guess: ")
        if guessed_letter.isalpha() and len(guessed_letter) == 1:
            return guessed_letter.lower()
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

    previous_words_list = []
    guessed_letters_list = []
    number_of_guesses = 7
    gameOn = True

    while gameOn:
        
        play_again = input("\nDo you want to start a new game (y/n)?").lower()

        if play_again == 'n':
            gameOver()
            gameOn = False
            break;

        elif play_again == 'y':
            number_of_guesses = 7
            guessed_letters_list.clear()
            
            # Randomly choose a word from the word_list if it hadn't been chosen already.
            found_new_word = False
            while not found_new_word:
                chosen_word = random.choice(word_list)
                if chosen_word not in previous_words_list:
                    found_new_word = True


            # For each letter in the chosen_word, add a "_" to display.
            display = list(chosen_word)
            for i in range(len(display)):
                display[i] = '_'

            # while the word is not fully guessed 
            while '_' in display:

                if number_of_guesses == 0:
                    print("\nYou are out of guesses.\nThe correct word was: {}".format(chosen_word))
                    lose()
                    break;
                
                print(HANGMANPICS[number_of_guesses-1])

                print(f"Previous guesses: {' '.join(guessed_letters_list)}")
                # display the word
                print(f"{' '.join(display)}")
            

                # ask user to choose letter or word
                letter_or_word = input("\nDo you want to guess a letter or a word (l/w)? ")
                if letter_or_word == 'l':
                    # validate that the input is a single letter
                    guessed_letter = guess_letter_validation()
                    # show previously guessed letters
                    guessed_letters_list.append(guessed_letter)

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
                        for i in range(len(chosen_word)):
                            display[i] = chosen_word[i]                    
                    else:
                        number_of_guesses -= 1
                        print("Your guess was incorrect.")

                # letter or word invalid choice
                else:
                    print('Invalid input. Try again.\n')
            
            # while '_'
            else:
                win()

                print(f"{' '.join(display)}")

        # play_again invalid choice
        else: 
            print("Invalid Input. Try again.")


start()


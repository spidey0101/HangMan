#import random
#import time

p1 = input("Enter name of the player to share the word!!")
p2 = input("Enter name of the player to reveal the word !!")
print(f"Welcome {p1} and {p2}!!! Let's play...")

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    word = input("Player 1, enter the word to be guessed: ").lower()
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("Do you want to play again? (y/n): ").lower()
    while play_game not in ["y", "n"]:
        play_game = input("Invalid input. Do you want to play again? (y/n): ").lower()
    if play_game == "y":
        main()
        hangman()
    else:
        print("Thanks for playing! See you next time.")
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5

    print("\nLet the guessing begin!")
    while count != limit:
        print_hangman(count, limit)
        print("Word to guess: " + display)
        print("Letters guessed so far: " + ', '.join(already_guessed))
        guess = input("Enter your guess: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in already_guessed:
            print("You have already guessed this letter. Try another one.")
            continue

        already_guessed.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display = display[:i] + guess + display[i+1:]
            print("Correct guess!")
            if display == word:
                print("Congratulations! You guessed the word:", word)
                play_loop()
        else:
            count += 1
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

    print("Sorry, you are HANGED! The word was:", word)
    play_loop()

def print_hangman(count, limit):
    stages = [  # Final stage: Head, body, both arms, and both legs
                """
                   _____
                  |     |
                  |     O
                  |    /|\\
                  |    / \\
                  |
                __|__
                """,
                # Head, body, both arms, and one leg
                """
                   _____
                  |     |
                  |     O
                  |    /|\\
                  |    /
                  |
                __|__
                """,
                # Head, body, and both arms
                """
                   _____
                  |     |
                  |     O
                  |    /|\\
                  |
                  |
                __|__
                """,
                # Head, body, and one arm
                """
                   _____
                  |     |
                  |     O
                  |    /|
                  |
                  |
                __|__
                """,
                # Head and body
                """
                   _____
                  |     |
                  |     O
                  |
                  |
                  |
                __|__
                """,
                # Head
                """
                   _____
                  |     |
                  |     O
                  |
                  |
                  |
                __|__
                """,
                # Initial empty stage
                """
                   _____
                  |     
                  |     
                  |
                  |
                  |
                __|__
                """
            ]
    print(stages[limit - count])

if __name__ == "__main__":
    main()
    hangman()

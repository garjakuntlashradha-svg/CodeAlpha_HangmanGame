
import random

# Five predefined words for the game
words = ["python", "apple", "school", "coding", "laptop"]

# Select a random word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=" * 35)
print("       WELCOME TO HANGMAN!")
print("=" * 35)
print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect guesses available.")

# Continue until the player wins or runs out of guesses
while wrong_guesses < max_wrong_guesses:
    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check whether the player has guessed the whole word
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        print("You won the game!")
        break

    # Ask the player to enter a letter
    guess = input("Enter one letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single letter.")
        continue

    # Check whether the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try another.")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess! Try again.")

else:
    print("\nGame over! You ran out of guesses.")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")

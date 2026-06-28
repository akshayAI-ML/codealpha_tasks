import random  # Used to select a random word

# List of predefined words
words = ["python", "apple", "planet", "laptop", "school"]

# Randomly choose one word
word = random.choice(words)

# Create blanks (_) equal to the length of the word
guessed_word = ["_"] * len(word)

# Store letters already guessed by the player
guessed_letters = []

# Maximum incorrect guesses allowed
wrong_guesses = 0
max_wrong_guesses = 6

print("===== Hangman Game =====")

# Continue until the player wins or loses
while wrong_guesses < max_wrong_guesses and "_" in guessed_word:

    # Display current progress
    print("\nWord:", " ".join(guessed_word))
    print("Wrong Guesses Left:", max_wrong_guesses - wrong_guesses)

    # Take one letter as input and convert it to lowercase
    guess = input("Enter a letter: ").lower()

    # Check for valid single-letter input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    # Save the guessed letter
    guessed_letters.append(guess)

    # Check if the guessed letter exists in the word
    if guess in word:
        # Reveal all matching letters
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct Guess!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")

# Check final result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The correct word was:", word)

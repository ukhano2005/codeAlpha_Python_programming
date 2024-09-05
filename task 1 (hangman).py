import random

def hangman():
    # List of words to choose from
    words = ['apple', 'banana', 'grape', 'orange', 'pear']
    word = random.choice(words).lower()

    # Variables to track progress
    guessed_word = ['_'] * len(word)
    tries = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    # Main game loop
    while tries > 0:
        print("\nCurrent word:", " ".join(guessed_word))
        guess = input("Guess a letter: ").lower()

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print(f"Good guess! '{guess}' is in the word.")
        else:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")

        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame over! The word was:", word)

# Run the game
hangman()

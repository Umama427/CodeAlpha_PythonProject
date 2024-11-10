import random

def hangman():
    # List of words to choose from
    words = ["python", "hangman", "programming", "development", "function", "variable", "algorithm"]
    word = random.choice(words).lower()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        # Display current state of the word
        current_state = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print(f"Current word: {current_state}")
        
        # Check if the player has guessed the word
        if current_state == word:
            print("Congratulations! You've guessed the word!")
            break
        
        guess = input("Guess a letter: ").lower()
        
        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
        
        # Display guessed letters
        print(f"Guessed letters: {', '.join(guessed_letters)}")

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Sorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    hangman()

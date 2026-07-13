import random

# List of words (You can include more words accordingly.)
words = [ "python", "computer", "programming", "developer", "hangman", "keyboard", "internet", "science", "artificial", "intelligence", "algorithm", "database" ,"python", "computer", "keyboard", "monitor", "internet", "software", "hardware", "database", "network", "algorithm", "variable", "function", "compiler", "debugger", "terminal", "browser", "website", "program", "developer", "technology", "artificial", "intelligence", "machine", "learning", "automation", "processor", "graphics", "memory", "storage", "security", "encryption", "firewall", "cloud", "server", "client", "framework", "library", "application", "interface", "protocol", "repository", "version", "coding", "binary", "digital", "android", "windows", "linux", "javascript", "java" ]

# Hangman all stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


def play_game():
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_attempts = 6

    print("\n======= HANGMAN GAME =======\n")

    while True:
        # Display the current hangman stage
        print(hangman_stages[wrong_guesses])

        # Display the guessed word
        display_word = ""
        completed = True

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                completed = False

        print("Word:", display_word)
        print("Guessed Letters:", " ".join(sorted(guessed_letters)))

        # Win check
        if completed:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break

        # Lose check
        if wrong_guesses == max_attempts:
            print("\n💀 Game Over! 💀")
            print("The correct word was:", word)
            break

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            print("❌ Wrong!")
            wrong_guesses += 1


while True:
    play_game()

    play = input("\nDo you want to play again? (y/n): ").lower()
    if play != "y":
        print("\n👋 Thanks for playing Hangman!")
        break
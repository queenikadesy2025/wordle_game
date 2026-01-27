# ASSESSMENT_TASK3
#
# Author: DESY_RIKAYANTI
# Student ID: 20154398
#
# Course: CERTIFICATE IV WEBSITE DEVELOPMENT
# Lecturer: INGRID_ALDUM

# Add Import statements (if needed)
import random

# Variables and Constants
# Define Constants
DEBUG = False
max_guesses = 6

# Define Variables 


# Application Functions
# Score Guess Function
def score_guess(target, guess):
    """Scores a guess word against a target word in a Wordle-style game.
    
    Arguments
    ---------
    target (str): The target word to match against.
    guess (str): The word guessed by the player.
    
    Returns
    -------
    list: A list of integers representing the score for each letter position.
    
    Examples
    --------
    >>> score = score_guess("hello", "hello")
    >>> print(score)
    [2, 2, 2, 2, 2]
    
    >>> score = score_guess("hello", "world")
    >>> print(score)
    [0, 1, 0, 2, 0]
    """

    #initialise Score as a list of 0s of length of Target Word
    score = []
    for counter in range(len(target)):
        score.append(0)

    #check if Guess word position matches Target word:
    for position in range(len(target)):
        if guess[position] == target[position]:
            score[position] = 2

    #check for misplaced letters (correct letter in wrong position):
    for position in range(len(target)):
        if score[position] != 2:
            if guess[position] in target:
                score[position] = 1
    return score

# Read File Into Word List Function
def read_words_from_file(filename):
    """Reads words from a text file and returns them as a list.
    
    Arguments
    ---------
    filename (str): The name of the file to read words from.
    
    Returns
    -------
    list: A list of words read from the file, with each word as a separate entry.
    
    Examples
    --------
    >>> word_list = read_words_from_file("target_words.txt")
    >>> print(word_list)
    ['apple', 'brave', 'chair', 'dance', 'eagle']
    """
    
    # Set list of words to be an empty list
    word_list = []
    
    # Open word file for reading
    with open(filename, 'r') as file:
        
        # While more words in file
        for line in file:
            # Read word from file
            word = line.strip()
            
            # Add word to list of words
            word_list.append(word)
    
    # Return the list of words
    return word_list


# Get random word
def random_target_word(word_list):
    """Selects and returns a random word to the word list.
    
    Arguments
    ---------
    word_list (list): A list of words to choose from.
    
    Returns
    -------
    str: A randomly selected word from the word list
    
    Examples
    --------
    >>> words = ['apple', 'brave', 'chair', 'dance', 'eagle']
    >>> selected = random_target_word(words)
    >>> print(selected)
    brave
    """  
    # Select a random number between 0 and the number of words in the list
    random_word = random.choice(word_list)


    # Return the word at the random number's position
    return random_word


# Set score output equal to ""
def display_score(score, guess_word):
    score_output = ""

    # Set word output to ""
    word_output = ""

    # For count in range 1 to length of score:
    for count in range(len(score)):
        
        # If score at position count is 0 then:
        if score[count] == 0:

            # Add "-" to the  score output
            score_output += "- "
            
        # If score at position count is 1 then:
        elif score[count] == 1:
        
            # Add "?" to the  score output
            score_output += "? "
        
        # If score at position count is 2 then:
        elif score[count] == 2:  
            
            # Add "X" to the  score output
            score_output += "X "
            
    # For count in range 1 to length of score:
    for count in range(len(score)):
        
        # Add guest word letter at position count to word output
        word_output += guess_word[count]
        
        # Add a space to word output
        word_output += " "
        

    # Display score output
    print(score_output)
        
    # Display word output
    print(word_output.upper())

# Display Greeting Function
def show_greeting():
    print("=" * 40)
    print("         WELCOME TO WORDLE GAME")
    print("=" * 40)

# Display Instructions Function
def show_instructions():
    print("Instruction:")
    print("\nHow to play:")
    print("- Guess the 5-letter word in 6 tries")
    print("- X = correct letter in correct position")
    print("- ? = correct letter in wrong  prosition")
    print("- - = letter not in word.\n")

# Any Optional Additional Functions 
def get_player_name():
    """Asks for and returns the player's name.

    Returns
    -------
    str: The player's name.
    """
    
    name = input("Please enter your name: ").strip()
    if name == "":
        return "Unknown"
    return name

# Validate Guess
def validate_guess(guess, allowed_words, target_word):
    """Validates if a guess is acceptable."""

    #Aplhabetic check
    if not guess.isalpha():
        return False, "Guess must contain letters only."

    # Check if word is too short
    if len(guess) < len(target_word):
        return False, "Word is too short! Must be "+str(len(target_word))+ " letters."


    # Check if word is too long
    if len(guess) > len(target_word):
        return False, "Word is too long! Must be "+str(len(target_word))+ " letters."

    #Dictionary check
    if guess not in allowed_words:
        return False, "Word not in allowed words list."

    return True, ""
    
# Save Game Result
def save_game_result(name, target_word, guesses_used, success):
    """Saves the game result to a file.
    
    Arguments
    ---------
    player_name (str): The name of the player.
    target_word (str): The target word for this game.
    guesses_used (int): Number of guesses used.
    success (bool): Whether the player won or not.
    """
    # Open file in append mode (creates file if it doesn't exist)
    with open("game_results.txt", "a") as file:
        
        # Format: Name, Target Word, Guesses Used, Success/Fail
        status = "Success" if success else "Failed"
        file.write("{},{},{},{}\n".format(name, target_word, guesses_used, status))

# Print Game Results 
def print_game_results():
    """Reads and displays all game results from the file."""
    try:
        with open("game_results.txt", "r") as file:
            print("\n" + "=" * 50)
            print("           GAME RESULTS HISTORY")
            print("=" * 50)
            print("{:<15} {:<12} {:<10} {:<10}".format("Player", "Word", "Guesses", "Result"))
            print("-" * 50)
            
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    player, word, guesses, result = parts
                    print("{:<15} {:<12} {:<10} {:<10}".format(player, word, guesses, result))
            
            print("=" * 50)
    except FileNotFoundError:
        print("\nNo game results found yet. Play some games first!")

# Play game function
def play_game():

    show_greeting()
    

    # Get player name
    name = get_player_name()
    print("\nHello", name.capitalize()+"! Let's play Wordle!\n")

    show_instructions()
    
    
    # Read Target Words into Target Word List
    target_words = read_words_from_file("target_words.txt")
   
    # Read All Words into All Word List
    allowed_words = read_words_from_file("all_words.txt")
    target_word = random_target_word(target_words) 

    # Set Target Word to a Random Word from Target Word List
    target_word = random_target_word(target_words)

    if DEBUG:
        print("DEBUG: Target word is",target_word)
    
    # Set guesses to 6
    guesses_remaining = max_guesses
    guesses_used = 0
    game_won = False
    
    
    # Game loop
    while guesses_remaining > 0:
        print("\nGuesses remaining: ",guesses_remaining)
              
        # Get guess word from User 
        guess = input("\nWhat is your guess? ").lower()
        #guess = guess.lower()

        # Validate guess
        is_valid, error_message = validate_guess(guess, allowed_words, target_word)
        
        if not is_valid:
            print("ERROR:", error_message)
            continue  #Skip counting invalid guess
        
        # Increment guesses used
        guesses_used += 1
        
        # Score word
        score = score_guess(target_word, guess)
        
        # Display score to player
        display_score(score, guess)
        
        # Check if player guessed the target
        if guess == target_word:
            print("\nDisplay End of Game Message")
            game_won = True
            break #Exit loop since game is won
        
        # Decrement remaining guesses 
        guesses_remaining -= 1
        
        # Out of guesses
        if guesses_remaining == 0:
            print("\nSorry",name.capitalize()+", you are unsuccessful. The word was", target_word.upper()+"!")

# Save game result to file
    save_game_result(name, target_word, guesses_used, game_won)
    print("\nYour game result has been saved!")

# Ask if player wants to view results
    view_results = input("\nWould you like to view game results? (yes/no): ").lower()
    if view_results == "yes" or view_results == "y":
        print_game_results()
    
    print("\nThanks for playing!")  

# Testing Function
def test_game():
    #"""Function to hold all test cases for independent testing."""
    # Test Case 1
    ## Arrange
    guess_word = "hello"
    target_word = "train"

    ## Act
    score = score_guess(guess_word, target_word)

    ## Assert
    #print("Score:", score, "Expected:", [0, 0, 0, 0, 0])

    # Test Case 2
    ## Arrange
    guess_word = "hello"
    target_word = "hello"

    ## Act
    score = score_guess(guess_word, target_word)

    ## Assert
    #print("Score:", score, "Expected:", [2, 2, 2, 2, 2])

    # Test Case 3
    # Set guess word to "world"
    guess_word = "world"

    # TODO: set target word to "hello"
    target_word = "hello"

    # Set score to score guess (guess word and target word)
    ## Act
    score = score_guess(guess_word, target_word)

    # Display the score
    ## Assert
    #print("Score:", score, "Expected:", [0, 1, 0, 2, 0])

    # Test Case 4
    ## Arrange
    all_word_filename = "all_words.txt"

    ## Act
    all_word_list = read_words_from_file(all_word_filename)

    ## Assert
    #print("Got:", all_word_list[:5], "Expected:", ['aahed', 'aalii', 'aargh', 'aarti', 'abaca'])

    # Test Case 5
    ## Arrange
    target_word_filename = "target_words.txt"

    ## Act
    target_word_list = read_words_from_file(target_word_filename)

    ## Assert
    #print("Got:", target_word_list[-5:], "Expected:", ['young', 'youth', 'zebra', 'zesty', 'zonal'])

    # Test Case 6
    word_list = ["apple", "banana", "cherry"]

    # Call random word with the list of words
    random_word = random_target_word(word_list)

    # Display the randomly selected word
    #print(random_word)

    # Test Case 7
    game_result = score_guess(target, guess)
    print(game_result)
    display_score(game_result, guess_word)
             
# Main Program   
if DEBUG:
    test_game()
else:
    play_game()

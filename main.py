import random
import ascii_art, words
import os, platform

# Check the platform and clear console
def clear_console():
  if platform.system() == 'Linux':
    os.system('clear')
  else:
    os.system('cls')

# Init variables, load word_list
word_list = words.word_list

chosen_word = random.choice(word_list)
current_guess = "_ " * len(chosen_word)
previous_guesses = ""
lives = len(ascii_art.HANGMANPICS)
message = "Hey! I have a word in my mind, do you care to guess it?"

# Draw current hangman state
def print_hangman_info():
  clear_console()
  print(ascii_art.HANGMAN_LOGO)
  print()
  print(message)
  # -lives, since pics are backwards
  print(ascii_art.HANGMANPICS[-lives])
  print(current_guess)
  if previous_guesses != "":
    print(f"Previous guesses: {previous_guesses}")

# While game still goes
while "_" in current_guess and lives > 1:
  # Print current state and get the input
  print_hangman_info()
  guess = input("Guess the letter: ").lower()
  
  # Check that input is good
  if len(guess) != 1 or not (ord(guess) >= ord('a') and ord(guess) <= ord('z')):
    message = "Dude, what are you trying to pull? Make a normal guess!"
    continue

  # Check if input is new
  if guess in previous_guesses:
    message = f"You have guessed '{guess}' previously!"
    continue
  # Remember input
  previous_guesses += guess

  # If guess is correct
  if guess in chosen_word:
    # Replace every _ with guessed letter
    for i in range(len(chosen_word)):
      if chosen_word[i] == guess:
        current_guess = current_guess[:2*i] + guess + current_guess[2 * i + 1:]
    message = f"YAY! There is '{guess}' in the word!!!"
  # Else lose a live
  else:
    lives -= 1
    message = "Oh wow, you missed that one. Try another!"

# Check why the game has ended
if lives <= 1:
  message = f"You lost! What a loser! It was '{chosen_word}' all along!"
else:
  message = "OMG, YOU DID IT!!!!"
# Final print
print_hangman_info()

#Step 1 

import random
import ascii_art, words
import os, platform

def clear_console():
  if platform.system() == 'Linux':
    os.system('clear')
  else:
    os.system('cls')

word_list = words.word_list

chosen_word = random.choice(word_list)
current_guess = "_ " * len(chosen_word)
previous_guesses = ""
lives = len(ascii_art.HANGMANPICS)
message = "Hey! I have a word in my mind, do you care to guess it?"

def print_hangman_info():
  clear_console()
  print(ascii_art.HANGMAN_LOGO)
  print()
  print(message)
  print(ascii_art.HANGMANPICS[-lives])
  print(current_guess)
  if previous_guesses != "":
    print(f"Previous guesses: {previous_guesses}")


while "_" in current_guess and lives > 1:
  print_hangman_info()
  guess = input("Guess the letter: ").lower()
  
  if len(guess) != 1 or not (ord(guess) >= ord('a') and ord(guess) <= ord('z')):
    message = "Dude, what are you trying to pull? Make a normal guess!"
    continue

  if guess in previous_guesses:
    message = f"You have guessed '{guess}' previously!"
    continue
  
  previous_guesses += guess

  if guess in chosen_word:
    for i in range(len(chosen_word)):
      if chosen_word[i] == guess:
        current_guess = current_guess[:2*i] + guess + current_guess[2 * i + 1:]
    message = f"YAY! There is '{guess}' in the word!!!"
  else:
    lives -= 1
    message = "Oh wow, you missed that one. Try another!"

if lives <= 1:
  message = f"You lost! What a loser! It was '{chosen_word}' all along!"
else:
  message = "OMG, YOU DID IT!!!!"

print_hangman_info()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

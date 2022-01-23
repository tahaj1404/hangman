import random
from hangman_words import word_list
from hangman_art import stages, logo
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

print(logo)

chosen_word = random.choice(word_list)

#print(f'The solution is {chosen_word}.')

display = []
for i in chosen_word:
  display.append("_")

end_of_game = False
lives = 6
while not end_of_game:
  guess = input("Guess a letter: ").lower()

  clearConsole()
  
  if guess in display:
    print(f"You have already guessed \'{guess}\'")

  w = 0
  for i in chosen_word:
      if i == guess:
          display[w] = guess
      w += 1

  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed \'{guess}\', that is not in the word.\nYou loose a life")
    if lives == 0:
      end_of_game = True
      print("You loose")

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You have won")
  
  print(stages[lives])

print(f"The word was \'{chosen_word}\'")
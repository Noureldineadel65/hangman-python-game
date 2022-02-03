import random
import hangman_art
from word_list import word_list
random_word = word_list[random.randint(0, len(word_list) - 1)]
random_word_list = list(random_word)
guessed = ['_'] * len(random_word_list)
lives = len(hangman_art.stages)
print(hangman_art.logo)
print("WELCOME TO HANGMAN!")

while not "".join(guessed) == random_word and lives > 0:
    guess_letter = input("Guess a letter: ")
    if guess_letter in random_word:
        if guess_letter not in "".join(guessed):
            num_of_occ = random_word_list.count(guess_letter)
            for i in range(num_of_occ):
                index_of_guessed = random_word_list.index(guess_letter)
                guessed[index_of_guessed] = guess_letter
                random_word_list[index_of_guessed] = "_"
            print(" ".join(guessed))
        else:
            print("You already used that letter.")
    else:
        lives -= 1
        print(hangman_art.stages[lives])
        print(f"Wrong Guess. You have {lives} tries left")
else:
    if lives > 0:
        print("You WONN!")
    else:
        print("You lose.")

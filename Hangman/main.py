import random
import hangman_words
import hangman_art


word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guessed_letters = []

logo = hangman_art.logo
stages = hangman_art.stages
print(logo)
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"Guessed letters: {guessed_letters}")
        print("You have already guessed this letter")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word and guess not in guessed_letters:
        print(guess)
        print("This letter is not in the word")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")
    if guess not in guessed_letters:
        guessed_letters += guess
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")

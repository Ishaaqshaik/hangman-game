import random
words = ["apple", "table", "chair", "river", "plant"]

word = random.choice(words)
guessed_letters = []          
incorrect_guesses = 0
max_incorrect = 6


print("Welcome to Hangman!")
print("_ " * len(word))       

while incorrect_guesses < max_incorrect:
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        print("Wrong!")
        incorrect_guesses += 1

    
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display.strip())

    
    if all(letter in guessed_letters for letter in word):
        print("🎉 You guessed the word! It was:", word)
        break

else:
    print("😢 You ran out of guesses. The word was:", word)

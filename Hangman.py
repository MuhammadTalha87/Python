import random
continents = ("Asia", "Europe", "Oceania", "North America", "South America", "Africa", "Antartica")
secret_word = random.choice(continents)
guesses_avaialble = 3
losing_number = 0

word = "Word: "+ "_ " * len(secret_word)
print(word)

while guesses_avaialble > losing_number:
    guess = input("Enter the word : ").title()
    guesses_avaialble -=1
    if guess == secret_word:
        print("You won the game")
        break
    elif guess != secret_word:
        print("Your guess was wrong")
        print(f"(Lives left :{guesses_avaialble})")
else:
    print("You lost the game")
    print(f"(correct word was : {secret_word})")


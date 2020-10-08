import random
import string


words = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(words)
letters = set(random_word)
user_letters = set()
hint = ""
lives = 8

def main_loop():
    while True:
        print()
        word_reveal()
        if "-" not in hint:
            print("You guessed the word!")
            print("You survived!")
            print()
            break
        user_action()
        if lives == 0:
            print("You lost!")
            print()
            break

def word_reveal():
    global hint
    hint = ""
    for char in random_word:
        if char in user_letters:
            hint += char
        else:
            hint += "-"
    print(hint)

def user_action():
    global lives
    global user_letters
    user_input = input("Input a letter: ")
    if user_input in user_letters:
        print("You already typed this letter")
    elif len(user_input) != 1:
        print("You should input a single letter")
    elif user_input not in string.ascii_lowercase:
        print("It is not an ASCII lowercase letter")
    elif user_input not in letters:
        print("No such letter in the word")
        lives -= 1
        user_letters.add(user_input)
    else:
        user_letters.add(user_input)


print("H A N G M A N")

while True:
    menu_input = input('Type "play" to play the game, "exit" to quit: ')
    if menu_input == "play":
        main_loop()
    elif menu_input == "exit":
        break

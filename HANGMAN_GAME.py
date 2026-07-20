import random
from worldlist import words


# Dictionary of keys:()
Hangman_art = {
    0: ("     \n"
        "     \n"
        "     "),
    1: ("  o  \n"
        "     \n"
        "     "),
    2: ("  o  \n"
        "  |  \n"
        "     "),
    3: ("  o  \n"
        " /|  \n"
        "     "),
    4: ("  o  \n"
        " /|\\ \n"
        "     "),
    5: ("  o  \n"
        " /|\\ \n"
        " /   "),
    6: ("  o  \n"
        " /|\\ \n"
        " / \\ ")
}

def display_man(wrong_guesses):
    print("**********")
    print(Hangman_art[wrong_guesses])
    print("**********")

def display_hint(hint):
    print(" ".join(hint))

def display_ans(answer):
    print(answer)


def main():
    answer = random.choice(words)
    hint= ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        
        print(f"Lives Left: {6 - wrong_guesses}")
        
        if "_" not in hint:
            display_man(wrong_guesses)
            display_ans(answer)
            print("YOU WIN")

        elif wrong_guesses == len(Hangman_art) - 1:
            display_man(wrong_guesses)
            print("YOU LOSE")
            print("Correct answer is ",end = "")

            display_ans(answer)
        
        play_again = input("Play again? (y/n): ").lower()
        
        if play_again != "y":
            is_running = False

    
if __name__ == "__main__":
    main()
import random
import os
import termcolor
from .words import ANSWERS, WORDS

STATUS_TO_COLOR = {
    "correct": "green",
    "absent": "white",
    "present": "yellow",
}

STATUS_TO_EMOJI = {
    "correct": "🟩",
    "absent": "⬛",
    "present": "🟨",
}


def print_title(index):
    os.system("cls" if os.name == "nt" else "clear")
    print(termcolor.colored(f"WORDLE {index}/6", "green", attrs=["reverse"]))


def print_error(error=None):
    if error is None:
        print()
    else:
        print(termcolor.colored(error, "red"))


def print_results(results):
    for result in results:
        print("".join([termcolor.colored(g, STATUS_TO_COLOR[s]) for (g, s) in result]))
    for _ in range(7 - len(results)):
        print()


def print_keyboard(results):
    first_row = "qwertyuiop"
    second_row = "asdfghjkl "
    third_row = " zxcvbnm  "
    color_keyboard(first_row, results)
    color_keyboard(second_row, results)
    color_keyboard(third_row, results)
    print()


def color_keyboard(row, results):
    absent_chars = [g for result in results for (g, s) in result if s == "absent"]
    present_chars = [g for result in results for (g, s) in result if s == "present"]
    correct_chars = [g for result in results for (g, s) in result if s == "correct"]
    for r in row:
        if r in correct_chars:
            print(termcolor.colored(r, "green"), end="")
        elif r in present_chars:
            print(termcolor.colored(r, "yellow"), end="")
        elif r in absent_chars:
            print(termcolor.colored(r, "grey"), end="")
        else:
            print(termcolor.colored(r, "white"), end="")
    print()


def play():

    # get answer for this game
    answer = list(random.choice(ANSWERS))

    # get all valid words
    valid_words = set(WORDS).union(set(ANSWERS))

    results = []
    print_title(len(results))
    print()
    print_results(results)
    print_keyboard(results)

    # loop until game is over
    while True:

        # loop until valid user input
        while True:

            # get user input
            guess = input("Guess: ").lower()

            # handle case when guess is not five letters
            if len(guess) != 5:
                print_title(len(results))
                print_error("Guesses need to be five letters!")
                print_results(results)
                print_keyboard(results)

            # handle case when guess is not a valid word
            elif guess not in valid_words:
                print_title(len(results))
                print_error(f"{guess} is not a valid word!")
                print_results(results)
                print_keyboard(results)
            else:
                break

        # parse guess into list and initialize variables
        guess = list(guess)
        statuses = ["absent"] * 5
        found_chars = set()

        # check each letter in guess into correct/absent
        for i, (a, g) in enumerate(zip(answer, guess)):
            if a == g:
                statuses[i] = "correct"
                found_chars.add(g)
            if g not in answer:
                statuses[i] = "absent"

        # handle cases where letter is in answer but not in correct position
        for i, g in enumerate(guess):
            if g in answer and g not in found_chars:
                statuses[i] = "present"
                found_chars.add(g)

        # add result to list of results
        result = list(zip(guess, statuses))
        results.append(result)

        # display results
        print_title(len(results))
        print()
        print_results(results)
        print_keyboard(results)

        # handle case where guess is correct answer
        if guess == answer:
            print(f"Wordle {len(results)}/6")
            for result in results:
                print(f"{''.join([STATUS_TO_EMOJI[status] for _, status in result])}")
            print()
            break

        # handle case where number of guesses is exceeded
        if len(results) > 5:
            print(f"ANSWER: {''.join(answer)}")
            break

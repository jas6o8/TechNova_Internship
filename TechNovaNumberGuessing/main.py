print("Welcome to the Number Guessing Game!")
import random

def play_round(maxnum, maxtries,):
    number = random.randint(1, maxnum)
    for attempt in range(1, maxtries + 1):
        raw = input(f"Guess 1– {maxnum} (or 'q' to quit): ").strip().lower()
        if raw == 'q':
            return 'quit', number
        try:
            guess = int(raw)
        except ValueError:
            print("Whole numbers only.")
            continue
        if guess == number:
            return attempt, number
        print("Too low!" if guess < number else "Too high!")
    return None, number   # ran out of tries


def main():
    maxnum = 100
    maxtries = 10
    
    
    while True:
        result, number = play_round(maxnum, maxtries)
        if result == 'quit':
            print(f"Bye! The number was {number}.")
            break
        elif result is None:
            print(f"Out of guesses. The number was {number}.")
            break
        else:
            print(f"Correct in {result} tries! Difficulty up.")
            maxnum += 100

if __name__ == "__main__":
    main()
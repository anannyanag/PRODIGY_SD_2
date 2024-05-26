import random

def game():
    count = 0
    while True:
        count += 1
        n = random.randint(1, 10)
        x = int(input("Enter your guess: "))
        if x == n:
            print(f"Congratulations! You won the game in {count} attempts.")
            break
        elif x < n:
            print("Too Low")
        else:
            print("Too High")

game()

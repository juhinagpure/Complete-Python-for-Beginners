import random 

n = random.randint(1, 100)
a = -1
guesses = 0

while a != n:
    guesses += 1
    a = int(input("Guess the number: "))
    if a > n:
        print("Lower number please\n")
    elif a < n:
        print("Higher number please\n")
    else:
        print(f"\n🎉 Congratulations! You guessed the number {n} in {guesses} guesses.")
        print("✅ Game Over")

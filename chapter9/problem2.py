import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 62)

    # Fetch the hiscore from the file
    try:
        with open("chapter9/hiscore.txt", "r") as f:
            hiscore = f.read()
            hiscore = int(hiscore) if hiscore.strip() != "" else 0
    except FileNotFoundError:
        hiscore = 0

    print(f"Your score: {score}")

    if score > hiscore:
        print("New high score!")
        # Write this hiscore to the file
        with open("chapter9/hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()

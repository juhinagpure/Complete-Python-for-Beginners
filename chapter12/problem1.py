try:
    with open("chapter12/1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("chapter12/2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("chapter12/3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thank you")

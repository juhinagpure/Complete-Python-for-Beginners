word = "Donkey"

with open("chapter9/donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("chapter9/donkey.txt", "w") as f:
    f.write(contentNew)

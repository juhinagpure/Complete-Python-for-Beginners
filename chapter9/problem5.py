words = ["Donkey","bad","ganda"]

with open("chapter9/donkey.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("chapter9/donkey.txt", "w") as f:
    f.write(content)

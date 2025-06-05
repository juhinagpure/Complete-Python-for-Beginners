with open("old.txt") as f:
    content=f.read()

with open("chapter9/renamed_by_python.txt","w") as f:
    f.write(content)
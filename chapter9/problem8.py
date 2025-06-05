with open("chapter9/this.txt") as f:
    content = f.read()

with open("chapter9/this_copy.txt","w")as f:
    f.write(content)
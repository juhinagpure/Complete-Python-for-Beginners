line=1

with open("chapter9/donkey.txt", "r") as f:
    lines= f.readline()

lineno=1
for line in lines:
    if ("python" in line):
        print("yes python is present .Line no : {line}")
        lineno+=1
    else:
        print("No python is not present")
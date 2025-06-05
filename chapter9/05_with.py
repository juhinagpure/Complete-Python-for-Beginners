f=open("chapter9/myfile.txt", "r")

print(f.read())

f.close()

# The same can be written using with statement as follows:
with open("chapter9/myfile.txt") as f:
    print(f.read())
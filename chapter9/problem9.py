with open("chapter9/file.txt") as f:
    content1= f.read()
with open("chapter9/poem.txt") as f:
    content2= f.read()
if content1 == content2:
    print("Both files are same")
else:
    print("Files are not same")

# with open("chapter9/this.txt") as f:
#     content1= f.read()
# with open("chapter9/this_copy.txt") as f:
#     content2= f.read()
# if content1 == content2:
#     print("Both files are same")
# else:
#     print("Files are not same")
    
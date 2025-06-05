f=open("chapter9/poem.txt")
content=f.read()
if("twinkle" in content):
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()
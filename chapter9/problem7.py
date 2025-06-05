with open("chapter9/log.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line.lower():  # optional: .lower() for case-insensitive
        print(f"Yes, 'python' is present. Line no: {lineno}")
        break
    lineno += 1
else:
    print("No, 'python' is not present.")

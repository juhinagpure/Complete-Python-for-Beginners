# write a python program to print the contents of a directory using to Os  module.search online for the function which does that

import os

# specify the directory you want to list
directory_path='/New folder'

# List all files and directories in the specified directory
contents = os.listdir(directory_path)

# print each file and directory name
for item in contents:
    print(item)
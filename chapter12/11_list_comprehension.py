myList=[1,2,5,9,3,5,5]

# squaredList = []
# for item in myList:
#     squaredList.append(item**2)

# Using list comprehension to create a new list with squared values
squaredList=[i*i for i in myList]

print(squaredList)
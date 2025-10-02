



# LIST COMPREHENSION
# List comprehension is a short and elegant way to create a new list by applying an expression to each item in an existing iterable (like list, tuple, or string).

# It replaces writing a loop + append() with a single line.
# [expression for item in iterable if condition]

# expression → operation or value to include in the new list
#
# item → current element from iterable
#
# iterable → list, tuple, string, etc.
#
# condition (optional) → filter elements

# list_1 = [1,2,3,4]
# list_2 = [2* i for i in list_1]
# print(list_2)

# -- Using functions
# words = ["hello", "python", "world"]
# upppercased = [w.upper() for w in words]
# print(upppercased)







# # Negative step (reverse)
# nums = [10, 20, 30, 40, 50]
# # print(nums[::-1]) # Reverse list → [50, 40, 30, 20, 10]
#
# print(nums[::-1])

# Negative indices
# nums = [10, 20, 30, 40, 50]
# print(nums[-3:]) # Last 3 elements → [30, 40, 50]
# print(nums[:-2]) # All except last 2 → [10, 20, 30]

# Using step
# nums = [10, 20, 30, 40, 50]
# print(nums[:2])
# print(nums[2:])


# Using step
nums = "method"
print(nums[:3])
print(nums[2:])




# Omitting start or end
# nums = [10, 20, 30, 40, 50]
# print(nums[:3])   # From beginning to index 2 → [10, 20, 30]
# print(nums[2:])   # From index 2 to end → [30, 40, 50]





# # HOW TO SLICE A LIST IN PYTHON:- A python list can be sliced with the ":" symbol
# names = ["Jack", "Jill", "Harvey", "Bill", "Joseph", "Agatha"]
# print(names[1:5])


# # Using a list membership:
# names = ["Jack", "Jill", "Harvey", "Mike"]
# for i in names:
#     print(i)



# # Simple way with the use of for loop
# names = ["Jack", "Jill", "Harvey", "Mike"]
# for i in range(0,len(names)):
#     print(names[i])



#HOW TO FIND AN ELEMENT IN PYTHON LISTS : in and not in
# names = ["Jack", "Jill", "Harvey", "Mike"]
# print('Mike' in names)
# print('natasha'not in names)


#LISTS INSIDE LISTS
# matrix = [1,[2,3,4],[5,6],[7,8,9]]
# print(matrix)


# ADD AND DELETE ELEMENTS IN A LIST: append and remove are pre-defined functions
# name = ['john', 'tommi', 'nick']
# name.append('mike')
# print(name)
# name.remove('mike')
# print(name)

# CAN WE USE A NEGATIVE INDEX IN PYTHON LISTS?---> YES

#How to implement a list in Python?
#Empty list [] and list with elements names =  ["Jack", "Jill"]


# name = ['john', 'tommi', 'nick']
# print(name)
# print(name[2])
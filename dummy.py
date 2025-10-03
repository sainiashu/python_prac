





# Check if Two Strings are Anagrams
# def are_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)
#
# print(are_anagram('silent','listen'))
# print(are_anagram('silent','tester'))





# Reverse Array
# def reverseArray(arr):
#     return  arr[::-1]
#
# print(reverseArray('testing'))

# manual loop reverse array
# def reverse_array_loop(arr):
#     reverse_arr = []
#
#     for i in  range(len(arr)-1,-1,-1):
#         reverse_arr.append(arr[i])
#     return reverse_arr
#
# print(reverse_array_loop([1,2,3,4]))





# First Non-Repeating Character
# def first_non_repeating(s):
#     char_count = {}
#
#     for char in s:
#         char_count[char] = char_count.get(char, 0) +1
#     for char in s:
#         if char_count[char] == 1:
#             return  char
#     return  None
#
# print(first_non_repeating("tester"))



# Reverse a String
# def reverse_String(s):
#     reverse_str =  ""
#     for char in s:
#         reverse_str = char + reverse_str
#     return reverse_str
#
# print(reverse_String("tester"))



# def reverse_String(s):
#     revs = ""
#     for i in range(len(s)-1,-1,-1):
#         revs += s[i]
#     return  revs
# print(reverse_String("hello"))

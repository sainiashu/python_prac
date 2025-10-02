


# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
#
#
# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'


# def string_bits(str):
#     result =""
#
#     for i in range(len(str)):
#         if i % 2 == 0:
#             result = result + str[i]
#     return result
#
#
#
# if __name__ == '__main__':
#     print(string_bits('chocolate'))


# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
#
#
# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'



    # def front_times(str, n):
    #     front_len= 3
    #     if front_len > len(str):
    #         front_len = len(str)
    #     front = str[: front_len]
    #
    #     result = ""
    #     for i in range(n):
    #         result  = result + front
    #
    #     return result
    #
    #
    #
    # if __name__ == '__main__':
    #     print(front_times('chocolate',3))





# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
#
#
# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'


# def string_times(str, n):
#   if len(str) >0:
#     return str *n
#
#
# if __name__ == '__main__':
#     print(string_times('Java',4))



# Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'

# #
# def front3(str):
#     front_end = 3
#     if len(str) < front_end:
#         front_end = len(str)
#     front = str[:front_end]
#     return front + front + front
#
#
# if __name__ == '__main__':
#     print(front3('Java'))

# ==========================================
# Given a string, return a new string where the first and last chars have been exchanged.

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

# def front_back(str):
#     if len(str)<=1:
#         return str
#     mid = str[1:len(str)-1]
#
#     return str[len(str)-1] + mid + str[0]
#
# if __name__== '__main__':
#     print(front_back('method'))

# ==========================================
# def missing_char(str, n):
#   return str[:n]+ str[n+1:]
#   # # return str[:n]
#   # return str[n+1:]
#
#
# if __name__== '__main__':
#     print(missing_char('method', 2))



# ==========================================
# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'

# def not_string(str):
#     if str.startswith('not'):
#         return  str
#     else:
#         return  'not ' + str
#
#
# if __name__ == '__main__':
#     print(not_string('not test'))
# ==========================================
# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
#
# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

# def near_hundred(n):
#   return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
#
#
# if __name__=='__main__':
#     print(near_hundred(99))


# ==========================================
# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

# def makes10(a,b):
#     if ((a== 10 or b == 10) or (a+b == 10)):
#         return  True
#     else:
#         return False
#
# if __name__=='__main__':
#     print(makes10(6,4))

# ==========================================
# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False


# def parrot_trouble(talking, hour):
#     if (talking and (hour<7 or hour>20)):
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#     print(parrot_trouble(True,18))

# ==========================================

# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

# def diff(n):
#     if n <= 21:
#         num = 21 -n
#     else:
#         num = (n-21) * 2
#     return num
#
#
# if __name__ == '__main__':
#     print(diff(24))


# ==========================================
# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

# def sum_double(a, b):
#     sum = a+b
#
#     if a == b:
#         sum = sum * 2
#     return sum
#
# if __name__== '__main__':
#     print(sum_double(2,2))

# ==========================================
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

# def monkey_trouble(a_smile, b_smile):
#     if a_smile and b_smile:
#         return  True
#     if not a_smile and not b_smile:
#         return True
#     return False
#
# if __name__== '__main__':
#     print(monkey_trouble(True, True))

# ==========================================
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#  sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

# def sleep_in(weekday, vacation):
#     if not weekday or vacation:
#         return True
#     else:
#         return False
#
# if __name__=='__main__':
#     print(sleep_in(True, False))





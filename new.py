# print("Hello world!")
# print(5)

# This is a comment
# In python, comments are written with the hash symbol (#) and are ignored by the interpreter. They are used to explain the code and make it more readable for humans.

# Escape sequences are special characters that are used to represent certain characters in strings. For example, the newline character (\n) is used to create a new line in a string, and the tab character (\t) is used to create a tab space.
# print("This is a string with a newline character.\nThis is the second line.")

# a = 10
# b = True
# c = "Hello"
# d = None
# print("The type of a is:", type(a))
# print("The type of a is:", type(b))
# print("The type of a is:", type(c))
# print("The type of a is:", type(d))

# list1 = [1, 2, True, "Hello", None]
# tuple = [1, 2, True, "Hello", [10, 20]]

# print(15 + 6)
# print(15 - 6)
# print(15 * 6)
# print(15 / 6)
# print(15 // 6)
# print(15 % 6)
# print(15 ** 6)

# def add(a, b):
#     return a + b

# def dele(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     return a / b

# result = add(5, 3)
# print(result)

# a = "1"
# b = "2"

# print(a + b)  # This will concatenate the strings and print "12"
# print(int(a) + int(b)) # This will convert the strings to integers and print 3

# a = input("Enter a first number: ")
# b = input("Enter a second number: ")
# print("You entered:", a)
# print("addition of two numbers is:", int(a) + int(b))

# name = "Divyesh"
# print("Hello " + name + "!")  # This will print "Hello Divyesh!"

# para = """This is a multi-line string.
# It can span multiple lines and is enclosed in triple quotes."""

# print(para)  # This will print the multi-line string as it is.
# print(para.upper())  # This will print the multi-line string in uppercase.
# print(para)  # This will print the multi-line string in uppercase.
# print(para.lower())  # This will print the multi-line string in lowercase.
# print(para.title())  # This will print the multi-line string in title case.
# print(para.strip())  # This will print the multi-line string with leading and trailing whitespace removed.
# print(para.replace("multi-line", "single-line"))  # This will replace "multi-line" with "single-line" in the string.
# print(para.split())  # This will split the multi-line string into a list of words.
# print(para.split("a"))  # This will split the multi-line string into a list of words.
# print(para.find("multi-line"))  # This will return the index of the first occurrence of "multi-line" in the string.
# print(para.count("multi-line"))  # This will return the number of occurrences of "multi-line" in the string.
# print(para.startswith("This"))  # This will return True if the string starts with "This", otherwise False.
# print(para.endswith("quotes."))  # This will return True if the string ends with "quotes.", otherwise False.
# print(para.isalpha())  # This will return True if all characters in the string are alphabetic, otherwise False.
# print(para.isdigit())  # This will return True if all characters in the string are digits, otherwise False.
# print(para.isalnum())  # This will return True if all characters in the string are alphanumeric, otherwise False.
# a = "Hello"
# print(a.isalpha())  # This will return True if all characters in the string are alphabetic, otherwise False.


# print(para[0:4])  # This will print the first four characters of the multi-line string.
# print(para[1:4])  # This will print characters from index 1 to 3.
# print(para[:5])  # This will print the first five characters of the multi-line string.
# print(para[:-3])  # print(para[:len(para)-3]) This will print the multi-line string excluding the last three characters.

#print(para[-4:-2])  # This will print the characters from index -4 to -3 of the multi-line string.

# a = int(input("Enter a number: "))
# if a > 0:
#     print("The number is positive.")
# else:
#     print("The number is negative or zero.")

import time
timestamp = time.time()
print("Current timestamp:", timestamp)  # This will print the current timestamp in seconds since the epoch (January 1, 1970).
timestamp1 = time.localtime(timestamp)
print("Current local time:", timestamp1)  # This will print the current local time as
timestamp2 = time.strftime("%Y-%m-%d %H:%M:%S", timestamp1)
print("Current local time in formatted string:", timestamp2)  # This will print the current
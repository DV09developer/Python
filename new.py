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

# import time
# timestamp = time.time()
# print("Current timestamp:", timestamp)  # This will print the current timestamp in seconds since the epoch (January 1, 1970).
# timestamp1 = time.localtime(timestamp)
# print("Current local time:", timestamp1)  # This will print the current local time as
# timestamp2 = time.strftime("%Y-%m-%d %H:%M:%S", timestamp1)
# print("Current local time in formatted string:", timestamp2)  # This will print the current

# x = 10

# match x:
#     case 1:
#         print("x is 1")
#     case 2:
#         print("x is 2")
#     case 10:
#         print("x is 10")
#     case _:
#         print("x is something else")

# for i in range(5):
#     print(i)  # This will print the numbers from 0 to 4.

# for i in para:
#     print(i)  # This will print each character in the multi-line string on a new line.

# i = 0
# while(i < 3):
#     print(i)  # This will print the numbers from 0 to 2.
    # i += 1

# while True:
#     user_input = input("Enter 'exit' to quit: ")
#     if user_input.lower() == 'exit':
#         break  # This will exit the loop if the user enters 'exit'.
#     else:
#         print("You entered:", user_input)  # This will print whatever the user entered.
# else:
#     print("This will not be printed because the loop was exited with a break statement.")

# for i in range(12):
#     if i == 10:
#         break
#     print("Current number:", i + 1)  # This will print the numbers from 1 to 10.

# print("\n\nLoop has been exited.\n\n")  # This will print after the loop has been exited.

# for i in range(12):
#     if i == 10:
#         continue
#     print("Current number:", i + 1)  # This will print the numbers from 1 to 12, skipping 11.

# def calculateGmean(a, b):
#     mean = (a * b) / (a + b)
#     print("The geometric mean of", a, "and", b, "is:", mean)
#     return mean

# a = 10
# b = 20
# result = calculateGmean(a, b)  # This will call the function and print the

# def functionName(a, b):
#     pass  # This is a placeholder for the function body. It does nothing and is used to indicate that the function is not yet implemented.

# def average(a = 10, b = 20):
#     print("The average of", a, "and", b, "is:", (a + b) / 2)

# average(10, 20)  # This will call the function and print the average of 10 and 20.
# average()  # This will call the function with default values and print the average of 10 and 20.
# average(b = 20 , a = 10)  # This will call the function with keyword arguments and print the average of 10 and 20.

# def average(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     print("The average of", numbers, "is:", total / len(numbers))
#     return total / len(numbers)

# average(10, 20, 30)  # This will call the function and print the average of 10, 20, and 30.
# c = average(10, 20, 30)  # This will call the function and print the average of 10, 20, and 30.
# print("The average is:", c)  # This will print the average returned by the function.

# def average(**kwargs):
#     total = 0
#     for key, value in kwargs.items():
#         total += value
#     print("The average of", kwargs, "is:", total / len(kwargs))

# average(a=10, b=20, c=30)  # This will call the function and print the average of 10, 20, and 30.

# l = [3, 5, 6, 7, 8, 9]
# # print(l)
# # print(type(l))
# print(l[-3])  # This will print the first element of the list, which is 3.
# print(l[len(l) - 3])  # This will also print the first element of the list, which is 3.
# print(l[3-3]) # This will also print the first element of the list, which is 3.
# print(l[0])  # This will also print the first element of the list, which is 3.
# print(l[:])
# print(l[1:2])  # This will print the second element of the list, which is 5.
# print(l[1:6:2])  # This will print the second element of the list, which is 5.

# if 5 in l:
#     print("5 is in the list")  # This will print because 5 is in the list.
# # same thing can be done with strings, tuples, and dictionaries. For example:
# s = "Hello"
# if "H" in s:
#     print("H is in the string")  # This will print because H is in the string.


lst = [i for i in range(10)]
print(lst)  # This will print the list of numbers from 0 to 9.
lst = [i for i in range(10) if i % 2 == 0]
print(lst)  # This will print the list of numbers from 0 to 9.
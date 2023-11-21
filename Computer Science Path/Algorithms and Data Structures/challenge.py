# Recursive
# runtime: Linear - O(N)
def factorial(n):
    if n < 0:
        return ValueError("Inputs 0 or greater only")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Iterative
def factorial(n):
    if n < 0:
        return
    value = 1
    for i in range(1, n+1):
        value *= i
    return value


print("\nFactorial")
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)


# Iterative
# Linear - O(N), where "N" is the number of digits in the number
def sum_digits(n):
    if n < 0:
        ValueError("Inputs 0 or greater only!")
    result = 0
    while n != 0:
        result += n % 10
        n = n // 10
    return result + n


# Recursive
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n//10)


# test cases
print("\nSum digits")
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)


# Iterative
def find_min(my_list):
    min = None
    for element in my_list:
        if not min or (element < min):
            min = element
    return min


# Recursive
def find_min(my_list, min=None):
    if len(my_list) == 0:
        return min
    else:
        if min == None or min > my_list[0]:
            min = my_list[0]
            my_list.remove(min)
        else:
            my_list.remove(my_list[0])
    return find_min(my_list, min)


print("\nFind min in list")
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)


# Iterative
# def is_palindrome(my_string):
#     while len(my_string) > 1:
#         if my_string[0] != my_string[-1]:
#             return False
#         my_string = my_string[1:-1]
#     return True


# More efficient
# Linear - O(N)
# def is_palindrome(my_string):
#     string_length = len(my_string)
#     middle_index = string_length // 2
#     for index in range(0, middle_index):
#         opposite_character_index = string_length - index - 1
#         if my_string[index] != my_string[opposite_character_index]:
#             return False
#     return True

# # Recursive


# Less efficient
def is_palindrome(my_string, flip=""):
    if len(my_string) < 2:
        return True
    else:
        flip = my_string[-1]
        my_string_first = my_string[0]
        if flip[0] != my_string_first:
            return False
        else:
            my_string = my_string.removesuffix(my_string[0])
            if len(my_string) != 0:
                my_string = my_string.removeprefix(my_string[0])
            return is_palindrome(my_string, flip)


# Efficient Recursive
def is_palindrome(my_string):
    if len(my_string) < 2:
        return True
    if my_string[0] != my_string[-1]:
        return False
    else:
        return is_palindrome(my_string[1:-1])


# test cases
print("\nPalindrome")
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)


def multiplication(num_1, num_2):
    result = 0
    for count in range(0, num_2):
        result += num_1
    return result


def multiplication(num_1, num_2):
    if num_1 == 0 or num_2 == 0:
        return 0
    else:
        num_2 -= 1
        return num_1 + multiplication(num_1, num_2)


# test cases
print("\nMultiplication")
print(multiplication(3, 7))
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)

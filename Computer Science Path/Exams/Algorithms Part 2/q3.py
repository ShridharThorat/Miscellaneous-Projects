# Recursive
# function fib(n)
#   if n is 1 or 0
#     return n
#   else
#     return fib(n - 1) + fib(n - 2)


memo = {}
def memo_fibonacci(number):
    ans = None
    if number in memo:
        ans = memo[number]
    elif number == 0 or number == 1:
        ans = number
    # Add your code here:
    elif memo.get(number):
        ans = memo.get(number)
    else:
        ans = memo_fibonacci(number-1) + memo_fibonacci(number-2)
        memo[number] = ans

    return ans


# Leave this so we can test your code:
print(memo_fibonacci(20))
print(memo_fibonacci(100))

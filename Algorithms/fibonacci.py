import time


def fibonacci_recursive(n):
    if n <= 2:
        result = 1
    else:
        result = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    return result


def fibonacci_list(n):
    sequence = [1, 1]
    for i in range(0, n):
        next = sequence[i] + sequence[i+1]
        sequence.insert(i+2, next)

    print(f"{n}th term is: {sequence[n-1]}")  # Since indexing starts at 0
    return sequence[n-1]


def fibonacci_three(n):
    first = 1
    second = 1
    third = 0

    for i in range(2, n):
        third = first + second
        first = second
        second = third

    print(f"{n}th term is: {third}")
    return third


def fibonacci(n):
    memo = [1, 1, 1]

    for i in range(2, n):
        memo[2] = memo[0] + memo[1]
        memo[0] = memo[1]
        memo[1] = memo[2]
    print(f"{n}th term is: {memo[2]}")
    return memo[2]

memo = {}
def fibonacci_memo(num):
    if num <= 2:
        return 1
    if memo.get(num, -1) != -1:
        return memo[num]
    else:
        answer = fibonacci(num-1) + fibonacci(num-2)
        memo[num] = answer
        
    return answer

function_calls = []
memo = {}
def fibonacci_memo_2(num, memo):
  function_calls.append(1)
  if num < 0:
    print("Not a valid number")
    return None
  if num <= 1:
    return num
  elif memo.get(num):
    return memo.get(num)
  else:
    memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo)
    return memo[num]

# print("")
# n = 40
# start = time.time()
# result = fibonacci_recursive(n)
# print(f"{n}th term is: {result}")
# end = time.time()
# # print time in seconds
# print("Time: ", round((end - start)*100000,2), "microseconds")


start = time.time()
value = fibonacci_list(4000)
end = time.time()
print("Time: ", round((end - start)*100000, 2), "microseconds")
print("")

start = time.time()
value = fibonacci_three(4000)
end = time.time()
print("Time: ", round((end - start)*100000, 2), "microseconds")
print("")

start = time.time()
value = fibonacci(4000)
end = time.time()
print("Time: ", round((end - start)*100000, 2), "microseconds")
print("")


# start = time.time()
# value = fibonacci_memo(4000)
# end = time.time()
# print(f"{4000}th term is: {value}")
# print("Time: ", round((end - start)*100000, 2), "microseconds")
# print("")
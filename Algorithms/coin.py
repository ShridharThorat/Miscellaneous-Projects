# Given a set of coin values coins = {c1, c2, ..., ck} and a target sum of money m,
# what's the minimum number of coins that form the sum m?


def coin(coins, target):
    sorted_coins = sorted(coins)
    coins_dict = {}  # key = coin, value = amount

    for coin in sorted_coins:
        coins_dict[coin] = 0

    # Quick exit if the target is in the set
    if target in coins:
        coins_dict[target] = 1

    base = 10
    i = len(str(target)) # The number of digits in the target
    while target != 0:
        largest_coin = sorted_coins[-1]
        if largest_coin > target:
            sorted_coins.pop(sorted_coins.index(largest_coin))
            continue
        this_base = pow(base, i-1)
        moded_target = target - (target % this_base)

        amount_of_count = moded_target // largest_coin
        coins_dict[largest_coin] = amount_of_count

        sorted_coins.pop(sorted_coins.index(largest_coin)) # Remove the largest coin
        
        # Update the new target
        target -= largest_coin*amount_of_count
        i = len(str(target))

    included = {}
    for coin, amount in coins_dict.items():
        if amount != 0:
            included[coin] = amount

    return included

def min_ignore_none(a,b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a,b)

def minimum_coins(coins,target):
    if target == 0:
        return 0    
    else:
        answer = None
        for coin in coins:
            sub_problem = target - coin
            if sub_problem < 0:
                continue
            else:
                answer = min_ignore_none(
                    answer,
                    minimum_coins(coins,sub_problem)+1)
                
    return answer

memo = {}

def minimum_coins_memo(coins,target):
    if target in memo:
        return memo[target] 
    if target == 0:
        return 0    
    else:
        answer = None
        for coin in coins:
            sub_problem = target - coin
            if sub_problem < 0:
                continue
            else:
                answer = min_ignore_none(
                    answer,
                    minimum_coins(coins,sub_problem)+1)
    memo[target] = answer
    return answer

# coins = {0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200}
coins = [1,4,5]
target = 13

print(minimum_coins(coins, target))

# def ways(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return ways(n - 1) + ways(n - 2)


# print(ways(5))

#this is a O(2n) algorithm, because as the n size grows, the amount of work grows by double


# Naive recursive version — recomputes the same sub-answers over and
# over. ways(2) alone gets recalculated from scratch every time it's
# needed, and that duplication compounds at every level of recursion.
# Each call branches into 2 more calls, so the call tree grows
# exponentially with n -> O(2^n).
# because this is a recursive version, it will keep calling the previously called before base case, leading to high amount of computation, compared with the memorization, the amount of calls are drastically decreased, because of not having to call previously called ways.


call_count = 0

def ways_naive(n):
    global call_count
    call_count += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return ways_naive(n - 1) + ways_naive(n - 2)

def ways_memo(n, memo):
    global call_count
    call_count += 1
    if n in memo:  #save the already computed 
        return memo[n]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        result = ways_memo(n - 1, memo) + ways_memo(n - 2, memo)
        memo[n] = result #save it before returning
        return result


call_count = 0
print(ways_naive(20), "naive calls:" , call_count)


call_count = 0
print(ways_memo(30, {}), "memo calls:" , call_count)



# normal fibonacci
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# memoized fibonacci
def fib_memo(n, memo):
    if n <= 1:
        return n
    elif memo[n] != None:
        return memo[n]
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]


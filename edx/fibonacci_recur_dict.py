def fib(x, d):
    if x in d:
        return d[x]
    else:
        ans = fib(x-1, d) + fib(x-2, d)
        d[x] = ans
        return ans
fib_dict = {0:1, 1:1}

print(fib(8, fib_dict))

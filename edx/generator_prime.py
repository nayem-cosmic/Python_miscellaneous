def genPrimes():
    x = 1
    while True:
        x += 1
        if x == 2:
            yield x
        else:
            isPrime = True
            for i in range(2, int(x**0.5)+1):
                if x%i==0:
                    isPrime = False
                    break

            if isPrime:
                yield x

gen = genPrimes()
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

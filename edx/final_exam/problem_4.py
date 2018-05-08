'''

Write a Python function that creates and returns a list of prime
numbers between 2 and N, inclusive, sorted in increasing order.
A prime number is a number that is divisible only by 1 and itself.
This function takes in an integer and returns a list of integers
'''

def primes_list(N):
    '''
    N: an integer
    '''
    iniPlist = [i for i in range(2, N+1) if i%2!=0 or i==2]
    pList = []

    for i in iniPlist:
        isPrime = True
        for j in range(3, int(i**0.5)+1):
            if i%j==0:
                isPrime = False
                break
        if isPrime:
            pList.append(i)

    return len(pList)

print(primes_list(1000000))

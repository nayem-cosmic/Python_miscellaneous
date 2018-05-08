def fac_recr(n):
    if n == 1:
        return 1 # base case
    else:
        return n*fac_recr(n-1) # recursive step

print(fac_recr(4))

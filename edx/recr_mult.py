def mult_recr(a, b):
    if b == 1:
        return a
    else:
        return a + mult_recr(a, b-1)

print(mult_recr(5, 3))

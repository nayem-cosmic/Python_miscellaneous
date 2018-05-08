def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def f(x):
        polySum = 0
        polyLen = len(L)
        for i, n in enumerate(L):
            polySum += n*x**(polyLen-i-1)
        return polySum
    return f

print(general_poly([1, 2, 3])(2))

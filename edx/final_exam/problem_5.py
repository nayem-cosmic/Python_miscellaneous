def f(a, b):
    return a+b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    interDict = {}
    diffDict = {}

    for k in d1:
        for m in d2:
            if k == m:
                interDict[k] = f(d1[k], d2[k])

    for k in d1:
        if k not in interDict:
            diffDict[k] = d1[k]

    for k in d2:
        if k not in interDict:
            diffDict[k] = d2[k]

    return (interDict, diffDict)

print(dict_interdiff({1:20, 2:30}, {1:10, 6:70}))

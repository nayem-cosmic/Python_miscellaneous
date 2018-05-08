# bubble sorting algorithm
def bubble_sort(L):
    sort = False
    while not sort:
        sort = True
        for j in range(1, len(L)):
            print(j)
            if L[j-1] > L[j]:
                sort = False
                (L[j-1], L[j]) = (L[j], L[j-1])
                print(L)
    return L

l = [3,45,7,2,3,4]
print(bubble_sort(l))

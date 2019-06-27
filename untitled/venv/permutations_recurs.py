def perm(a, i):
    if i == len(a):
        print(a)
    else:
        for j in range(i, len(a)):
            a[i], a[j] = a[j], a[i]
            perm(a, i + 1)
            a[i], a[j] = a[j], a[i]


lst = [1, 2, 3, 4]
perm(lst, 0)

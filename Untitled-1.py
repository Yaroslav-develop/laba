def g():
    return int(input())
def f(x):
    main = []
    for i in range(0, x):
        for j in range(0, x^2):
            main[i, j] = g()
    return main
print(f(10))
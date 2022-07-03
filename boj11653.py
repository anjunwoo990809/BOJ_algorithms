N = int(input())

def Factorization(n):
    divider = 2
    while divider <= n:
        if n % divider == 0:
            print(divider)
            n = int(n/divider)
        else:
            divider += 1

Factorization(N)
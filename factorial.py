def fac(n):
    k = 1
    while n>0:
        k = k*n
        n = n-1
    return k

if __name__ == '__main__':

    n = int(input('Enter a number:'))
    k = fac(n)
    print(n,'factorial is',k)


def prime(k):
    i = 1
    n = 1
    for i in range(k,1,-1):
        if k%i==0:
            n = n+1
        if n>2:
            return 0
    return 1


if __name__ == '__main__':
    k = int(input('Enter a number:'))
    l = prime(k)
    if l==0:
        print(k,'is a composite number')
    else:
        print(k,'is a prime number')

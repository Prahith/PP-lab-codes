def arms(k):
    l = 0
    while k:
        n = k%10
        l = l + n**3
        k = int(k / 10)
    return l

if __name__ == '__main__':
    k = int(input('Enter a number:'))
    l = arms(k)
    if l==k:
        print(k,'is an armstrong number')
    else:
        print(k,'is not an armstrong number')
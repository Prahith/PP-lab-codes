def palin(k):
    l = k[::-1]
    if l==k:
        return 1
    else:
        return 0

if __name__ == '__main__':
    k = input('Enter a string or a number:')
    n = palin(k)
    if n==0:
        print(k,'is not a palindrome')
    else:
        print(k,'is a palindrome')
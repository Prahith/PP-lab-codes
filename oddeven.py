def oddev(n):
    if n%2==0:
        return 1
    else:
        return 0


if __name__ == '__main__':

    k = int(input('Enter a number:'))
    i = oddev(k)
    if i==0:
        print(k,'is an odd number')
    else:
        print(k,'is an even number')

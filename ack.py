def ackermann(m, n):
    if m == 0:
        return n+1
    elif m > 0:
        if n == 0:
            return ackermann(m-1, 1)
        elif n > 0:
            return ackermann(m-1, ackermann(m, n-1))
    print 'invalid input'

if __name__ == '__main__':
    print ackermann(3, 4)
    print ackermann(-1, 2)

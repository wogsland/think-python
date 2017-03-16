def countdown(n):
    if n <= 0:
        print 'Blastoff!'
    else:
        print n
        countdown(n-1)

if __name__ == '__main__':
    countdown(32)

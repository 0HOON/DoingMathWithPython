def is_factor(a,b):
    if b % a == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    a = int(input('Is '))
    b = int(input('factor of '))

    print (is_factor(a,b))

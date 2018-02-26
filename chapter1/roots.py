def roots(a, b, c):
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/2*a
    x_2 = (-b - D)/2*a
    print('{0} or {1}'.format(x_1,x_2))

if __name__ == '__main__':
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    roots(float(a),float(b),float(c))
## It can transfer more units

def printMenu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')
    print('5. C to F')
    print('6. F to C')

def kmToMiles(a):
    result = a / 1.609
    print(result)
def milesToKm(a):
    result = a * 1.609
    print(result)
def kgToLb(a):
    result = a * 2.205
    print(result)
def lbToKg(a):
    result = a * 0.454
    print(result)
def CToF(a):
    result = a * 9/5 + 32
    print(result)
def FToC(a):
    result = (a-32) * 5/9
    print(result)

if __name__ == '__main__':
    printMenu()
    choice = input('Your choice : ')
    value = float(input('Enter a value : '))
    if(choice == '1'):
        kmToMiles(value)
    elif(choice == '2'):
        milesToKm(value)
    elif(choice == '3'):
        kgToLb(value)
    elif(choice == '4'):
        lbToKg(value)
    elif(choice == '5'):
        CToF(value)
    elif(choice == '6'):
        FToC(value)
    else:
        print('Please try again')
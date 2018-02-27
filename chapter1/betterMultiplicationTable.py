## It'll multiply your first number and 1,2,3 ... your second number , then it'll print the results

number_1 = input('your first number : ')
number_2 = input('your second number : ')

try:
    anumber_1 = int(number_1)
    anumber_2 = int(number_2)

    for i in range (1, anumber_2 + 1 ):
        print('{0} X {1} = {2}'.format(anumber_1, i , anumber_1 * i))

except ValueError:
    print('Please enter integers')
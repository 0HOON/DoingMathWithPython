##Check whether the input number is an odd number or not
##And then, if the input number is an odd number, print next 5 odd numbers
##else, print next 5 even numbers

run = True
print('Type "break" if you want to stop')

while(run):
    userInput  = input('Your number : ')
    
    if(userInput == 'break'):
        run = False

    try:

        input_num = float(userInput)

        if(input_num.is_integer()):
            if(input_num % 2 == 0):
                print('It is an even number')
                for i in range(2,11,2):
                    print(input_num + i)
                
            else:
                print('It is an odd number')
                for i in range(2,11,2):
                    print(input_num + i)
        else:
            
            print('Please enter an integer')
    
    except ValueError:
        print('Please enter an integer')

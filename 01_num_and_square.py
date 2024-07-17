
try:
    num = int(input('Enter a number : '))

    square = num **2

    print(f'Square of the number given is {square}')

except Exception as e:
    print(f'Program failed with exception {e}')
else:
    print('Program executed sucessfully')
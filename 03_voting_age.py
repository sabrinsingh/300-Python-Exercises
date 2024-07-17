def user_input():
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    return name, age

def user_rslt(name, age):
    if age < 18:
        print(f'Hello {name}! You are ineligible to vote. You can cast vote in {18-age} years. Thanks')
    else:
        print(f'Hello {name}! You are eligible to vote. Thanks')
name, age = user_input()
user_rslt(name, age)



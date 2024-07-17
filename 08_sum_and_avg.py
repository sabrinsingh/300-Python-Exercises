# WAP to ask marks for 6 subjects, add them and find the average. 
# Given that 100 is the full marks find the percentage also

print('Enter the marks for 6 subjects : ')
full_marks = 600
total_marks = 0
for i in range(1,7):
    mark = float(input(f'Marks for subject{i} : '))
    total_marks += mark

print(f'Total marks is {total_marks} and the average marks is {total_marks/6}')
print(f'The percentage is {total_marks/full_marks * 100} %')
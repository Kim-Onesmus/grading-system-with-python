school = input('Enter the name of your School: ')
name = input('Enter your full name: ')
reg = input('Enter your Registration number: ')
units = int(input('Enter the number of units: '))

average=0
total=0
uni = ''
grade = chr
for i in range(units):
    unit = input('Enter the name of the Unit: ')
    score = int(input('Enter the marks you scored: '))
    uni += unit
    total = total+score
    average = (total/units)

    if average >= 70:
        grade = 'A'
    if average >= 60 and average < 70:
        grade = 'B'
    if average >= 50 and average < 60:
        grade = 'C'
    if average >= 40 and average < 50:
        grade = 'D'
    if average < 40:
        grade = 'E'

print('*'*20)

print('Name of the School: ',school)
print('Your name: ',name)
print('Registration number: ',reg)
print('Number of units: ',units)
print('Name of units: ',uni)
print('Total marks: ',total)
print('Average marks: ',average)
print('Your grade: ',grade)

print('*'*20)

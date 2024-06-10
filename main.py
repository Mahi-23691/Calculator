#Variables
first_number = int(input('Enter your firstnumber: '))
second_number = int(input('\nEnter your second number: '))
operator = input('\nChoose an opertaion\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n\n')

#Loops
#Addition
if 'Addition' in operator or 'addition' in operator or '1' in operator or 'ADDITION' in operator:
  print(f'\nThe resut is {first_number + second_number}')

#Subtraction
elif 'Subtraction' in operator or 'subtraction' in operator or '2' in operator or 'SUBTRACTION' in operator:
  print(f'\nThe resut is {first_number - second_number}')

#Multiplication
elif 'Multiplication' in operator or 'multiplication' in operator or '3' in operator or 'MULTIPLICATION' in operator:
  print(f'\nThe resut is {first_number * second_number}')

#Divison
elif 'Division' in operator or 'division' in operator or '4' in operator or 'DIVISION' in operator:
 if second_number != 0:
  print(f'\nThe resut is {first_number / second_number}')
 else: #You can't divide a number with 0
  print('\nYou cant divide by 0')

#If you choose a wrong operator
else:
  print('\nInvalid Input')


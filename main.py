#Variables
first_number = int(input('Enter your firstnumber: '))
second_number = int(input('\nEnter your second number: '))
operator = input('\nChoose an opertaion\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n\n')

#Loops
if 'Addition' in operator or 'addition' in operator or '1' in operator or 'ADDITION' in operator:
  print(f'\nThe resut is {first_number + second_number}')
  
elif 'Subtraction' in operator or 'subtraction' in operator or '2' in operator or 'SUBTRACTION' in operator:
  print(f'\nThe resut is {first_number - second_number}')
  
elif 'Multiplication' in operator or 'multiplication' in operator or '3' in operator or 'MULTIPLICATION' in operator:
  print(f'\nThe resut is {first_number * second_number}')
  
elif 'Division' in operator or 'division' in operator or '4' in operator or 'DIVISION' in operator:
 if second_number != 0:
  print(f'\nThe resut is {first_number / second_number}')
 else:
  print('\nYou cant divide by 0')
  
else:
  print('\nInvalid Input')


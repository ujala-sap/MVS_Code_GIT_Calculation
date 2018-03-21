# This is a python program to perform mathematical calculation on 2 numbers based on user input

# Enter the 1st value
value1  = int(input('Enter the 1st Value : '))
# Enter the 2nd value
value2 = int(input('Enter the 2nd value: '))
# Enter the operand
op_list  = ['+', '-', '*', '/', '%', '**']
op = input('Enter the arithmetic operator : ')

return_data = op in op_list
if return_data == True:
    if op == '+':
        result = value1 + value2
    elif op == '-':
        result = value1 - value2
    elif op == '*':
        result = value1 * value2
    elif op == '/':
        result = value1 / value2
    elif op == '%':
        result = value1 % value2
    elif op == '**':
        result = value1 ** value2
    else:
        result = 0
else:
    print('The entered operand is not available in the list {}'.format(op_list))
    result = 0

print('The result for {} and {} is {}'.format(value1,value2,result))

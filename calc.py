'''
We have to create a calculator which will take 3 parameters

    variable A
    variable B
    Opeartor op

It will perform +, -, *, / operation.
And return the resultant value.
'''

def calculator(a, b, op):

    if (op == '+'):
        c = a + b
    elif (op == '-'):
        c = a - b
    elif op == 'x':
        c = a * b
    elif op == '/':
        c = a / b
    else:
        c = 'Operator is not valid!'

    return c

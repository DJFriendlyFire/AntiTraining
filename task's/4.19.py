def calculator(num1, num2, char):
    if char == '+':
        return num1 + num2
    elif char == '-':
        return num1 - num2
    elif char == '*':
        return num1 * num2
    elif char == '/':
        if num2 == 0:
            print('Деление на 0 невозможно')
            return 0
        return num1 / num2

result = calculator(10, 5, '+')
print(result)
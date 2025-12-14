def string_analysis(string):
    count = {'letters': 0, 'digits': 0, 'spaces': 0, 'another': 0}
    for char in string:
        if char.isalpha():
            count['letters'] += 1
        elif char.isdigit():
            count['digits'] += 1
        elif char == ' ':
            count['spaces'] += 1
        else:
            count['another'] += 1

    return count

result = string_analysis('Hello World 123!')
print(result)

def inch_to_cm(inch):
    return inch * 2.54


inch_value = int(input('Enter the value in inch: '))

print('{}″ = {}cm'.format(inch_value, inch_to_cm(inch_value)))
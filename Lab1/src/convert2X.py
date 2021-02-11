import sys

hex_mapping = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}


def base_converter(num, base):
    if base <= 0:
        print('Incorrect base: ', base)
        exit()

    if num == 0:
        return '0'

    result = ''
    while num > 0:
        next_val = num % base
        num = int(num / base)
        next_digit = hex_mapping[next_val]
        result = next_digit + result
    return result


def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


number_of_arguments = len(sys.argv)

if number_of_arguments < 2:
    print('There are no argument.')
    exit()

arg0 = sys.argv[1]

if number_of_arguments > 2:
    print('More than one argument passed, using only the first one:', arg0)

if not is_int(arg0):
    print('The submitted value ', arg0, ' is not a number, try again.')
    exit()

number = int(arg0)

if number < 0:
    print('The number ', number, 'is negative. You must pass a non negative integer.')
    exit()

binary_number = base_converter(number, 2)
hex_number = base_converter(number, 16)

print('Decimal: ', number)
print('Binary: ', binary_number)
print('Hexadecimal: ', hex_number)

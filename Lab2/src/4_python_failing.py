num_string_arr = ['0','1','2','3','4','5','6','7','8','9']

def int_to_str(number):
  if number < 0:
    return 'Not allowing negative numbers'

  if number == 0:
    return '0'

  num_str = ''
  while number > 0:
    digit = number % 10
    number = int(number / 10)
    num_str =  num_string_arr[digit] + num_str

  return num_str

def str_to_int(string_number):
  number = 0
  for character in string_number:
      number = number * 10
      digit = num_string_arr.index(character)
      number = number + digit

  return number

int_test_values = [-1, 0, 1, 5, 12345, 98765, 4116, 6622, 999, 15]

print('int_to_str Test Cases ({0}):'.format(len(int_test_values)))
print('')

index = 0
for value in int_test_values:
  index = index + 1
  result = int_to_str(value)
  print('Test {0}: Value {1} converted in string: {2}'.format(index, value, result))

print('')

str_test_values = ['0', '1', '26', '536', '000452', '2626', '17771', '12677772234', '0101010', '999999']
print('str_to_int Test Cases ({0}):'.format(len(int_test_values)))
print('')


index = 0
for value in str_test_values:
  index = index + 1
  result = str_to_int(value)
  print('Test {0}: Value {1} converted to int: {2}'.format(index, value, result))

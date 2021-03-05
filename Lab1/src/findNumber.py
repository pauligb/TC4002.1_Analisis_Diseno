import random


def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


file_name = "GuessingSteps.txt"
output_file = open("GuessingSteps.txt", "w")

max_value = 30
random_number = random.randrange(max_value - 1) + 1


def printAll(file_descriptor, text):
    file_descriptor.write(text + "\n")
    print(text)


printAll(output_file, "A random number between 1-30 was generated")

while True:
    printAll(output_file, "")
    input_value = input("Input between 1-30: ")
    output_file.write("Input between 1-30: " + input_value + "\n")

    if input_value == "exit":
        printAll(output_file, "Exiting program")
        break

    if not is_int(input_value):
        printAll(output_file, str(input_value) + "Is not a number.")
        continue

    input_int = int(input_value)
    if input_int < random_number:
        printAll(output_file, "Input value is smaller than the number to guess.")
    elif input_int > random_number:
        printAll(output_file, "Input value is bigger than the number to guess.")
    else:
        printAll(
            output_file, "You guess right!, the random number was " + str(random_number)
        )
        break

print("\nWritting history in " + file_name + " file")
output_file.close()

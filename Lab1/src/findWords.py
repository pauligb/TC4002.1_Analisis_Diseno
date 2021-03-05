from os import path
import re
import sys


def remove_special_characters(text):
    return re.sub(r"\W+", " ", text)


def count_words(text, words):
    word_count = {}
    for word in words:
        word_count[word] = 0

    clean_text = remove_special_characters(text)
    text_words = clean_text.split()

    for word in text_words:
        if word in word_count:
            word_count[word] += 1

    return word_count


number_of_arguments = len(sys.argv)

if number_of_arguments < 2:
    print("There are no argument.")
    exit()

file_path = sys.argv[1]
words_to_search = sys.argv[2:]

if not path.exists(file_path):
    print("File: ", file_path, " does not exist.")
    exit()

file = open(file_path, "r")
file_text = file.read()
file.close()

result = count_words(file_text, words_to_search)
print(result)

# List comprehension lessons

# ==========

# number = [1, 2, 3]
# new_list = [n + 1 for n in number]

# print(new_list)

# name = "Pedro Henrique"
# letters = [letter for letter in name]

# print(name)

# print([2 * n for n in range(1, 5)])

# names = ["Pedro", "Henrique", "Marcos", "Paulo", "Luís", "Felipe"]

# print([name for name in names if len(name) <= 5])

# ==========
# File exercise
# ==========

# with open("file1.txt", "r") as file1:
#     file1_numbers = [int(num) for num in file1]
# with open("file2.txt", "r") as file2:
#     file2_numbers = [int(num) for num in file2]
#
# common_numbers = [num for num in file1_numbers if num in file2_numbers]
#
# print(common_numbers)


# Dictionary Comprehension

# ==========

# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor"]
#
# students_scores = {student: random.randint(1, 100) for student in names}
# passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
#
# print(students_scores, passed_students)

# ===========

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# length_words = {sentence: len(sentence) for sentence in sentence.split(" ")}
#
# print(length_words)

# ===========
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: (temperature * 9/5) + 32 for (day, temperature) in weather_c.items()}
#
# print(weather_f)

# ===========
# my way:
#
# with open("nato_phonetic_alphabet.csv", "r") as nato_file:
#     nato_list = [line for line in nato_file]
#
# nato_dict = {elto.split(",")[0]: elto.split(",")[1][:-1] for elto in nato_list}
#
# user_input = input("Enter a word: ")
# user_input_letters = [letter.upper() for letter in user_input]
#
# result = {word for (letter, word) in nato_dict.items() if letter in user_input_letters}
#
# print(result)
# print(nato_dict)

# =========
# smart way

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]

print(output_list)



import csv
# import pandas
# # # #TODO 1 - DONE. Create a dictionary in this format:
# # # {"A": "Alfa", "B": "Bravo"}
#
# #ВАРИАНТ 2
phonetic_dict = {}
with open("nato_phonetic_alphabet.csv") as file:
    data = csv.reader(file)
    print(data)
    for row in data:
        # print(row)
        phonetic_dict[f"{row[0]}"] = row[1]
    print(phonetic_dict)

# #ВАРИАНТ 3
# # phonetic_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
# # print(phonetic_dict.to_dict())
#
# #ВАРИАНТ 4
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
# print(phonetic_dict)
# # # #TODO 2 - DONE. Create a list of the phonetic code words from a word that the user
#
# word = input("Enter a word:").upper()
# #ВАРИАНТ 2
# # phonetic_list = [phonetic_dict[char.upper()] for char  in word ]
# #
#
#
# #ВАРИАНТ 3
# # for (index, row) in phonetic_dict.iterrows():
# #     for char in word:
# #         if char == row.letter:
# #             print(row.code)
#
# # ВАРИАНТ 4
# phonetic_list = [phonetic_dict[char] for char in word]
#
# print(phonetic_list)
#
#
#
#

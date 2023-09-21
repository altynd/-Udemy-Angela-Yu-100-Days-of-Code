import csv

# #TODO 1 - DONE. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {}
with open("nato_phonetic_alphabet.csv") as file:
    data = csv.reader(file)
    for row in data:
        phonetic_dict[f"{row[0]}"] = row[1]

# #TODO 2 - DONE. Create a list of the phonetic code words from a word that the user

word = input("Enter a word:")

# phonetic_list = []
# for char in word:
#     for key in phonetic_dict:
#         if char.upper() == key:
#             phonetic_list.append(phonetic_dict[key])

#the same that above but shoter
phonetic_list = [phonetic_dict[char.upper()] for char  in word ]

print(phonetic_list)

# Turns user's desired word into a code with the NATO alphabet

import pandas

abc = pandas.read_csv("nato_phonetic_alphabet.csv")

# dict = {}
# for (index, row) in abc.iterrows():
#     dict[row.letter] = row.code
# print(dict)
abc_dict = {row.letter:row.code for (index,row) in abc.iterrows()}
print(abc_dict)

word = input("Type a word: ").upper()
letter_list = [letter for letter in word]

output = []
for letter in letter_list:
    for (key, value) in abc_dict.items():
        if key == letter:
            output.append(value)

print(output)




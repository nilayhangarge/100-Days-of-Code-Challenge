# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

# Reads csv file and converts it into dataframe
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())
# The dict is not in required format

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# Creating dict in required format using dict_comprehension
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
word_list = [phonetic_dict[letter] for letter in word]
print(word_list)

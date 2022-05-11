import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def valid_entry():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except:
        print("Sorry, only letters in the alphabet please.")
        return False
    else:
        print(output_list)
        return True


while not valid_entry():
    continue

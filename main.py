import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
#todo create a dictionary with key and his code
dict={row.letter:row.code for (index,row) in data.iterrows()}

#todo crete a list from dictionry  of code any user input name
def generate_phontic():

    word=input("enter a word:").upper()
    try:
     list=[dict[letter] for letter in word]
    except KeyError:
        print("Soory only alphabat ")
        generate_phontic()
    else:
        print(list)

generate_phontic()
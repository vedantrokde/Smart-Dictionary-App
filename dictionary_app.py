from json import load
from difflib import get_close_matches


# loading the dataset of word dictionary
data = load(open(file="data.json"))

# displaying welcome/instructions message
print("\n\nWord Dictionary")
print("="*30)
print("Enter the word you want to know meaning of below.")
print("To exit enter exit or press Ctrl+C at prompt.")

# function to display word meaning


def disp(word, meanings):
    print("Word Meaning of ", word, " is: ")
    for (index, meaning) in enumerate(meanings):
        print(str(index+1)+".", meaning)


# running loop for multiple instances
while(True):
    query = input("\nInput: ").lower()

    # checking for quitting query
    if(query == 'exit'):
        break


    # calculating similarities
    alternative = get_close_matches(query, data.keys(), cutoff=0.8)

    # program logic
    if(query in data):
        disp(query, data[query])
    # checking for corner cases of title case
    elif query.title() in data:
        disp(query.title(), data[query.title()])
    # checking for corner cases of upper case
    elif query.upper() in data:
        disp(query.upper(), data[query.upper()])

    elif len(alternative) > 0:
        print("Did you mean ", alternative[0], "? ")
        choice = input("Enter Y if Yes: ").lower()
        if choice=='y':
            disp(alternative[0], data[alternative[0]])
    else:
        print("The word doesn't exist. Please try again...")

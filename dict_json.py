import json
from difflib import get_close_matches


def retrive_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])

        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return ("The word doesn't exist, yet.")
        else:
            return ("We don't understand your entry. Apologies.")


def print_word(output):
    if type(output) == list:
        for item in output:
            print("-", item)

    else:
        print("-----", output)


if __name__ == '__main__':
    data = json.load(open("data.json"))
    while True:
        word_user = input("Enter a word: ")
        if word_user:
            output = retrive_definition(word_user)
            print_word(output)
        else:
            break


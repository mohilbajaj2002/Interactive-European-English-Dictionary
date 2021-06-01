# contains all the support functions to run the app

import json
from difflib import get_close_matches

def OpeningMessage():
    print(" ")
    print("Welcome to the Interactive European English Dictionary!")
    print("We process the following languages (for now)- ENG, FRA, ITA, SPA")
    print("To close the program, enter /end")
    word = input ("Please enter a word: ")
    return word


def FileReader(filename):

    filename = "Data/" + filename

    if (filename[-5:] == ".json"):
        text = json.load(open(filename, "r"))
    else:
        with open (filename, "r", encoding='utf-8') as eurolanguage:
            text = eurolanguage.read()

    return text


def WordProcessor(word):

    euro_language_files = ["data.json", "fra-eng.dict", "ita-eng.dict", "spa-eng.dict"]

    # to check if a meaning was found in any language
    count = 0

    #resolving the upper/lower casing issue
    word = word.lower()
    for file in euro_language_files:
        text = FileReader(file)
        if (file[-5:] == ".json"):
            try:
                meaning = text[word]
                print(f"This is an ENG word. Meaning: {meaning[0]}")
                count = 1

            except:
                if (len(get_close_matches(word, text.keys(), cutoff = 0.8))) > 0:
                    yn = input(f"Did you mean {get_close_matches(word, text.keys(), cutoff = 0.8)[0]} instead? Enter Y/N: ")
                    if yn == "Y":
                        print(f"This is an ENG word. Meaning: {text[get_close_matches(word, text.keys(), cutoff = 0.8)[0]]}")
                        count = 1
                    elif yn == "N":
                        print("The word doesn't exist. Please double check it.")
                    else:
                        print("We didn't understand your entry.")
                        count = 1

        # splitting the text into lines and then checking the line's first word for the user word
        else:
            lang = file[:3].upper()
            lines = text.splitlines()

            for i in range(len(lines)):
                if(lines[i].find(word) != -1):
                    split_line = lines[i].split("/")
                    if(split_line[0].strip() == word):
                        meaning = lines[i+1]
                        print(f"This is an {lang} word. Meaning: {meaning}")
                        count = 1
                        break


    if(count == 0):
        print("The word is either incorrect or not part of our data list. Please try another one! ")

    word = input ("Please enter another word: ")
    return word

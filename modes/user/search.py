import functions.UI.load_languages
from document.languages_words import langs, list_lang
from functions.filtering.word_filtering import filtering
from functions.translate.translate import *
def user_mode():
    modes = functions.UI.load_languages.load_languages(list(list_lang))
    breaking = False
    while True:
        
        counter = 1
        for mode in modes:
            print(f"{counter}-{mode[0]} to {mode[1]} ")
            counter += 1
        print("Insert 0 to stop")
        #ask for the mode
        translate_number = int(input())
        if not(translate_number):
            break
        while not(0 < translate_number <= counter):
            if not(translate_number):
                breaking = True
                break 
            print("Please enter a number within a certain interval")
            translate_number = int(input())
        if breaking:
            break 

        word = input()
        origin,destination = modes[translate_number -1][0],modes[translate_number-1][1]
        result = translate(filtering(word), langs[origin], langs[destination])
        return result, origin, word, langs
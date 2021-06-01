# main file
# app runs till "/end" is encountered

import json
import support_functions as sf


def main():

    main_word = " "
    count = 0

    while (main_word != "/end"):
        if(count == 0):
            main_word = sf.OpeningMessage()
            main_word = sf.WordProcessor(main_word)
            count = 1
        else:
            main_word = sf.WordProcessor(main_word)



if __name__ == "__main__":
    main()

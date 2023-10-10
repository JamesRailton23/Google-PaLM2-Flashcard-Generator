import os
import sys
import google.generativeai as palm
#api key
palm.configure(api_key="here")
model = palm.get_model("models/text-bison")
prompt = ("Create a set of flashcards in question-and-answer format from the provided notes, using simple and "
          "easy-to-remember language, and formatting the flashcards into a table with two columns: one for the "
          "question and one for the answer.")

def generateflashcard():
    create_flashcards = int(input("Generate flashcards?: 1 for yes and 0 for exit: "))
    if create_flashcards:
        with open("input.txt") as input_file:
            file = input_file.read()
            print(file)
    else:
        sys.exit()


generateflashcard()

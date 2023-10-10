import os
import sys
import google.generativeai as palm
#api key
palm.configure(api_key="here")
aimodel = palm.get_model("models/text-bison")
prompt = ("Create a set of flashcards in question-and-answer format from the provided notes below the colon, "
          "using simple and easy-to-remember language, and formatting the flashcards into a table with two columns "
          "one for the"
          " question and one for the answer: ")

def generateflashcard():
    with open("input.txt") as input_file:
        file = input_file.read()
        flashcards = str(palm.generate_text(model=aimodel, prompt=prompt+file))
    with open("ouput.txt","w") as output_file:
        output_file.write(flashcards)
        output_file.read()
    if int(input("Re-generate?: 1 for yes or 0 for no: ")):
        generateflashcard()
    else:
        sys.exit()


if int(input("Generate flashcards?: 1 for yes and 0 for exit: ")):
    generateflashcard()
else:
    sys.exit()

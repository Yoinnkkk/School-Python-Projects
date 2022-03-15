from ASCIICompressor import compress
from ASCIIDecompressor import decompress
import time as t
def inputconfiged(string):
    return input(string + "\n:::   ")

def wait(time):
    t.sleep(time)

def menu():
    Question = inputconfiged("Choose an option from the ones below:\nCompress\nDecompress\nDisplay\nQuit")

    if Question.lower() == "compress":
        Question = inputconfiged("What is the name of the object you would like to compress? ")
        Question2 = inputconfiged("What is the file you would like to output to? ")
        compress(Question, Question2)
        menu()
    elif Question.lower() == "decompress":
        Question = inputconfiged("What is the name of the object you would like to decompress? ")
        Question2 = inputconfiged("What is the file you would like to output to? ")
        decompress(Question, Question2)
        menu()
    elif Question.lower() == "display":
        print(open("Projects/ASCIICompressor/ASCIIArt.txt", "r").read())
        wait(2)
        menu()
    else:
        print("Unknown choice or quit found.")
        wait(1)
        quit()
menu()
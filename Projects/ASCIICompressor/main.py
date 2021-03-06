from ASCIICompressor import compress
from ASCIIDecompressor import decompress
import os
import time as t

def inputconfiged(string):
    return input(string + "\n:::   ")

def wait(time):
    t.sleep(time)

def enterRLE():
    path, rleline, Question = "Projects/ASCIICompressor/", [], int(inputconfiged("How many lines?"))
    while Question < 2:
        print("Please enter more than 2 lines!")
    for i in range(Question):
        rleline.append(inputconfiged("Please input line "+ str(i+1)))
    rleline = ''.join(rleline)
    with open(path + "Compressedtemp.txt", "w") as f1, open(path + "Decompressedtemp.txt", "r") as f2:
        f1.write(rleline)
        decompress("Compressedtemp.txt", "Decompressedtemp.txt")
        os.remove(path + "Compressedtemp.txt")
        file = f2.read()
        print(file)
        os.remove(path + "Decompressedtemp.txt")
    return

def menu():
    Question = inputconfiged("Choose an option from the ones below:\nEnter RLE\nCompress\nDecompress\nDisplay\nQuit")
    if Question.lower() == "enter rle":
        enterRLE()
    elif Question.lower() == "compress":
        Question = inputconfiged("What is the name of the object you would like to compress? ")
        Question2 = inputconfiged("What is the file you would like to output to? ")
        compress(Question, Question2)
        wait(1)
    elif Question.lower() == "decompress":
        Question = inputconfiged("What is the name of the object you would like to decompress? ")
        Question2 = inputconfiged("What is the file you would like to output to? ")
        decompress(Question, Question2)
        wait(1)
    elif Question.lower() == "display":
        with open("Projects/ASCIICompressor/ASCIIArt.txt", "r") as f1:
            print(f1.read())
        wait(2)
    else:
        print("Unknown choice or quit found.")
        wait(1)
        quit()
while True:        
    menu()
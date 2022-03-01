from ASCIICompressor import compress
from ASCIIDecompressor import decompress
def menu():
    Question = input("Choose an option from the ones below:\nCompress\nDecompress\nDisplay\nQuit\n:::   ")

    if Question.lower() == "compress":
        Question = input("What is the name of the object you would like to compress? ")
        Question2 = input("What is the file you would like to output to? ")
        compress(Question, Question2)
        menu()
    elif Question.lower() == "decompress":
        Question = input("What is the name of the object you would like to decompress? ")
        Question2 = input("What is the file you would like to output to? ")
        decompress(Question, Question2)
        menu()
    elif Question.lower() == "display":
        print(open("Projects/ASCIICompressor/ASCIIArt.txt", "r").read())
        menu()
    else:
        print("Unknown choice or quit found.")
        quit()
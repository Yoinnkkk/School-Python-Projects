from ASCIICompressor import compress
from ASCIIDecompressor import decompress

Question = input("Would you like to compress or decompress? ")

if Question.lower() == "compress":
    Question = input("What is the name of the object you would like to compress? ")
    Question2 = input("What is the file you would like to output to? ")
    compress(Question, Question2)
else:
    Question = input("What is the name of the object you would like to decompress? ")
    Question2 = input("What is the file you would like to output to? ")
    decompress(Question, Question2)
from ASCIICompressor import compress
from ASCIIDecompressor import decompress

Question = input("Would you like to compress or decompress? ")

if Question.lower() == "compress":
    Question = input("What is the name of the object you would like to compress? ")
    compress(Question)
else:
    Question = input("What is the name of the object you would like to decompress? ")
    decompress(Question)
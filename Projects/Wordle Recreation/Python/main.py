from word import tword

def inputc(string):
    return input(string + "\n:::   ")


class Canvas:
    def __init__(self, length, tries):
        self.length = length
        self.tries = tries
        self.triesused = 0
        self.usedwords = []
        self.tiles = []
        self.correct = False
        while len(self.tiles) != tries:
            self.tiles.append([])
            
#first array in tiles defines tries
#second array inside tiles defines word
# e.g length = 5, tries = 2
# [] [] [] [] [] - Try 1
# [] [] [] [] [] - Try 2
# overall has 5 letters in one
# def display(canvas):
#     x=0
#     while x < len(canvas.tiles):
#         print(canvas.tiles)
#         x+=1
#     return

def inputChecker():
    with open("Projects/Wordle Recreation/Python/dictionary.txt", "r", errors='ignore', encoding="utf8") as f1:
        dictionary = f1.read()
        wordInput = ""
        while wordInput not in dictionary:
            wordInput = inputc("Please input a word: ")
    return wordInput

def main(l, t):
    canvas = Canvas(l, t)
    while canvas.correct != True:
        # display(canvas)
        inputChecker()
    return

while True:
    options = [inputc("How long would you like the words to be? (default:5)") or 5, inputc("How many tries at guessing would you like to have? (default:6)") or 6]
    main(options[0],options[1])
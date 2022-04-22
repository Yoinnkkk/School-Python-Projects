from word import tword

def inputc(string):
    return input(string + "\n:::   ")


class Canvas:
    def __init__(self, length, tries):
        self.length = length
        self.tries = tries
        self.triesused = 0
        self.usedwords = []
        self.newword = ""
        self.tiles = []
        self.correct = False
        while len(self.tiles) < tries:
            self.tiles.append([])
            
#first array in tiles defines tries
#second array inside tiles defines word
# e.g length = 5, tries = 2
# [] [] [] [] [] - Try 1
# [] [] [] [] [] - Try 2
# overall has 5 letters in one
def display(canvas):
    x, currentword=0,""
    if canvas.usedwords != [] and canvas.newword != canvas.usedwords[canvas.triesused - 1]:
        currentword = canvas.usedwords[canvas.triesused - 1]
        for c in currentword:
            canvas.tiles[canvas.triesused - 1].append(c)
    while x < len(canvas.tiles):
        print(canvas.tiles[x])
        x+=1
    return

def inputChecker(dict, canvas):
        #while wordInput not in dictionary:
        wordInput = inputc("Please input a word: ")
        with open("Projects/Wordle Recreation/Python/dictionaries/dict"+str(dict)+".txt", "r") as f1:
            read = f1.readlines()
            dict = []
            for c in read:
                c = c.rstrip()
                dict.append(c)
            while wordInput not in dict:
                wordInput = inputc("Please input a correct word: ")
                display(canvas)
        return wordInput

def main(l, t):
    canvas = Canvas(l, t)
    while canvas.correct != True:
        display(canvas)
        input = inputChecker(l, canvas)
        canvas.usedwords.append(input)
        canvas.triesused+=1
        if input == tword:
            print("Well Done!")
            canvas.correct == True
            return
        if canvas.triesused == canvas.tries:
            print("No more tries left")
            return
    return

while True:
    options = [inputc("How long would you like the words to be? (default:5)") or 5, inputc("How many tries at guessing would you like to have? (default:6)") or 6]
    main(options[0],options[1])
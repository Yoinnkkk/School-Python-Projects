from wordlibrary import randomWord
def inputc(string):
    return input(string + "\n:::   ")


class Canvas:
    def __init__(self, length, tries):
        self.length = length
        self.tries = tries
        self.triesused = 0
        self.usedwords = []
        self.correctword = randomWord(length)
        self.tiles = []
        self.correct = False
        x=0
        while len(self.tiles) < tries:
            self.tiles.append([])
            while len(self.tiles[x]) < length:
                self.tiles[x].append([])
            x+=1
            
#first array in tiles defines tries
#second array inside tiles defines word
# e.g length = 5, tries = 2
# [] [] [] [] [] - Try 1
# [] [] [] [] [] - Try 2
# overall has 5 letters in one

def display(canvas):
    x, currentword=0,""
    if canvas.usedwords != []:
        currentword = canvas.usedwords[canvas.triesused - 1]
        i=0
        for d in canvas.correctword:       # get every character in the correct word
            for character in currentword:      # get every character in word used
                if character == d:       # if the character is the same
                    print("same character")
                    break
                if character in canvas.correctword and character != d:
                    print("wrong place character")
            canvas.tiles[canvas.triesused - 1][i].append(character)
            i+=1
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
        print(canvas.correctword)
        display(canvas)
        word = inputChecker(l, canvas)
        canvas.usedwords.append(word)
        canvas.newword = word
        canvas.triesused+=1
        print(canvas.correctword)
        if canvas.correctword == word:
            display(canvas)
            print("Well Done!")
            canvas.correct == True
            return
        if canvas.triesused == canvas.tries:
            display(canvas)
            print("No more tries left")
            return
    return

while True:
    options = [inputc("How long would you like the words to be? (default:5)") or 5, inputc("How many tries at guessing would you like to have? (default:6)") or 6]
    main(int(options[0]),int(options[1]))
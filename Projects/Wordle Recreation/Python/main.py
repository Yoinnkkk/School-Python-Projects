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
            print(self.tiles)
            
#first array in tiles defines tries
#second array inside tiles defines word
def display():
    x=0
    while x < len(canvas.tiles):
        print(canvas.tiles)
        x+=1

def main(l, t):
    canvas = Canvas(l, t)
    while canvas.correct != True:
        display()
        
    return

while True:
    options = [inputc("How long would you like the words to be? (default:5)") or 5, inputc("How many tries at guessing would you like to have? (default:6)") or 6]
    main(options[0],options[1])
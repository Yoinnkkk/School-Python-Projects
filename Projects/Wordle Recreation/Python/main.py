def inputc(string):
    return input(string + "\n:::   ")


class Canvas:
    def __init__(self, length, tries):
        self.length = length
        self.tries = tries
        self.triesused = 0
        self.usedwords = []
        self.tiles = list(list())


def start(l, t):
    canvas = Canvas(l, t)
    print(canvas.tries)
    return 


while True:
    options = [inputc("How long would you like the words to be? (default:5)") or 5, inputc("How many tries would you like to have? (default:6)") or 6]
    start(options[0],options[1])
import random as r
def randomWord(length):
    word = ""
    with open("Projects/Wordle Recreation/Python/dictionaries/dict"+str(length)+".txt", "r", errors="ignore") as f1:
        read = f1.readlines()
        word = read[r.randint(0, len(read))]
    return word
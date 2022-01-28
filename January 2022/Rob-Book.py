codingGurus = [
    "Adam",
    "Billy",
    "Charlie",
    "Dan",
    "Ethan",
    "Frank",
    "Garfield",
    "Juliet",
    "Robbie",
    "Tommy"
]
name = input("What is your name? ")
global match

def binarySearch(name):
    match = False
    bottom = 0
    top = len(codingGurus)-1
    while bottom <= top and match != True:
        middle = (bottom+top)//2
        if codingGurus[middle] == name:
            match = True
        elif codingGurus[middle] < name:
            bottom = middle - 1
        else:
            top = middle - 1
    return match

print(binarySearch(name))
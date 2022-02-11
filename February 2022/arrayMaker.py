import random as rand
def makeArray(amount, smallest, largest):
    array = []
    i=0
    while i < amount:
        number = rand.randint(smallest, largest)
        array.append(number)
        i+=1
    return array
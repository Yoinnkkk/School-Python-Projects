#Bubble sort lesson 04022022
array = [92,55,84,48,72,90,87,54,67,75]
def bubbleSort(array):
    swap = True
    amount = len(array)
    while swap == True:
        swap = False
        for i in range(1, amount-1):
            if array[i-1] > array[i]: #change operand for descending or ascending e.g. < to > and vice versa.
                temp = array[i]
                array[i] = array[i-1]
                array[i-1] = temp
                swap = True
        amount-1
    return "finished swapping"
print(array)
print(bubbleSort(array))
print(array)
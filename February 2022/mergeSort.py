#import custom array maker
import arrayMaker as am
#work on 11/02/2022
def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)
        a=0
        b=0
        c=0

        while a<len(left) and b<len(right):
            if left[a]<right[b]:
                array[c]=left[a]
                a+=1
            else:
                array[c]=right[b]
                b+=1
            c+=1
        while a<len(left):
            array[c]=left[a]
            a+=1
            c+=1
        while b<len(right):
            array[c]=right[b]
            b+=1
            c+=1
#input variables
inputs = [
    int(input("What size would you like the array to be? ")), 
    int(input("Whats the minimum limit? ")), 
    int(input("Whats the maximum limit? ")), 
    int(input("What number would you like to search for? "))
]

array=am.makeArray(inputs[0], inputs[1], inputs[2])
mergeSort(array)
print(array)

if inputs[3] in array:
    amountFound = 0
    numberIndex = []
    grammar = ""
    while inputs[3] in array:
        numberIndex.append(array.index(inputs[3])+amountFound)
        amountFound+=1
        array.pop(array.index(inputs[3]))
    if len(numberIndex) > 1:
        grammar = "'s "
    else:
        grammar = " "
    print("Your number (",inputs[3],") has been found at index"+grammar+"", numberIndex,", this happened", amountFound, " times.")
else:
    print("Your number (",inputs[3],") has not been found.")
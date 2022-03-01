# main function
def decompress(input, output):
    input = open("Projects/ASCIICompressor/"+input+".txt", "r").read()
    decodedarray = []
    counter = 0
    open("Projects/ASCIICompressor/" + output+".txt", "w").close()
    finishedproduct = open("Projects/ASCIICompressor/" + output+".txt", "a")
    for string in input:
        decodedarray.append(string)
    def recall(counter):
        if len(decodedarray) == 0:
            return
        
        if decodedarray[0].isdigit() == True and decodedarray[1].isdigit() == False:
            counter = int(decodedarray[0])
            decodedarray.pop(0)
            recall(counter)
        decodedarray[0] = decodedarray[0] = decodedarray[0] + decodedarray[1]
        decodedarray.pop(1)
        else:
            while counter != 0:
                finishedproduct.write(decodedarray[0])
                counter-= 1
            decodedarray.pop(0)
            counter = 0
            recall(counter)
    recall(counter)
    return 

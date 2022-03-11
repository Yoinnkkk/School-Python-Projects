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
        while len(decodedarray) > 0:
            if decodedarray[0].isdigit() == True and decodedarray[1].isdigit() == True and counter == 0:
                decodedarray[0] = decodedarray[0] + decodedarray[1]
                decodedarray.pop(1)
                counter = int(decodedarray[0])
                decodedarray.pop(0)
            while counter != 0:
                finishedproduct.write(decodedarray[0])
                counter-= 1
            decodedarray.pop(0)
            counter = 0
    recall(counter)
    return
decompress("a", "art")

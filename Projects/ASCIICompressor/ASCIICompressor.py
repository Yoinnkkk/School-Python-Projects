# main function

def compress(input, output):
    #make file extension work 
    input = input.split(".")[0]
    output = output.split(".")[0]
    input = open("Projects/ASCIICompressor/"+input+".txt", "r").read()
    open("Projects/ASCIICompressor/"+output+".txt", "w").close()
    finishedproduct = open("Projects/ASCIICompressor/"+output+".txt", "a")
    encodedarray = []
    counter = 0
    #seperates ascii art into array
    for string in input:
        if len(string) > 0:
            encodedarray.append(string)
    #counter for all ascii characters
    currentchar = encodedarray[0]
    def recall(counter, currentchar):
        while len(encodedarray) > 0:
            if currentchar != encodedarray[0] and not counter > 99:
                if counter >= 10:
                    finishedproduct.write(str(counter) + currentchar)
                else:
                    finishedproduct.write("0" + str(counter) + currentchar)
                currentchar = encodedarray[0]
                counter = 0
                if len(encodedarray) == 1:
                    finishedproduct.write(str(1) + encodedarray[0])
                    return
            if currentchar == encodedarray[0]: 
                encodedarray.pop(0)
                counter+=1
    recall(counter, currentchar)
    return encodedarray

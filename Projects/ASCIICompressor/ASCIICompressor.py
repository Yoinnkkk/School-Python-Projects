# main function

def compress(input, output):
    #make file extension work 
    input = input.split(".")[0]
    output = output.split(".")[0]
    with open("Projects/ASCIICompressor/"+input+".txt", "r").read() as f1, open("Projects/ASCIICompressor/"+output+".txt", "a") as f2:
        #variable line
        input, encodedarray, counter = f1.read(), [], 0
        open("Projects/ASCIICompressor/"+output+".txt", "w").close()
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
                        f2.write(str(counter) + currentchar)
                    else:
                        f2.write("0" + str(counter) + currentchar)
                    currentchar, counter = encodedarray[0], 0
                    if len(encodedarray) == 1:
                        f2.write(str(0) + str(1) + encodedarray[0])
                        f2.write(str(1))
                        return
                if currentchar == encodedarray[0]: 
                    encodedarray.pop(0)
                    counter+=1
        recall(counter, currentchar)
    return encodedarray

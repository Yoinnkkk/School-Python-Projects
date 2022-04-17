# main function
def decompress(input, output):
    input = input.split(".")[0]
    output = output.split(".")[0]
    #automatic with close 
    with open("Projects/ASCIICompressor/"+input+".txt", "r") as f1, open("Projects/ASCIICompressor/"+output+".txt", "a") as f2:
        #variable line
        input, decodedarray, counter = f1.read(), [], 0
        open("Projects/ASCIICompressor/" + output+".txt", "w").close()
        #char splitter
        for string in input:
            decodedarray.append(string)
        while len(decodedarray) > 0:
            if decodedarray[0].isdigit() == True and decodedarray[1].isdigit() == True and counter == 0:
                decodedarray[0] = decodedarray[0] + decodedarray[1]
                decodedarray.pop(1)
                counter = int(decodedarray[0])
                decodedarray.pop(0)
            while counter != 0:
                f2.write(decodedarray[0])
                counter-= 1
            decodedarray.pop(0)
            counter = 0
    return
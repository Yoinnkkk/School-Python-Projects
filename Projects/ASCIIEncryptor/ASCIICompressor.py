# main function

def compress(input, output):
    input = open("Projects/ASCIIEncryptor/"+input+".txt", "r").read()
    open("Projects/ASCIIEncryptor/"+output+".txt", "w").close()
    finishedproduct = open("Projects/ASCIIEncryptor/"+output+".txt", "a")
    encodedarray = []
    counter = 0
    #seperates ascii art into array
    for string in input:
        if len(string) > 0:
            encodedarray.append(string)
    #counter for all ascii characters
    currentchar = encodedarray[0]
    def recall(counter, currentchar):
#        if len(encodedarray) == 0:
#            return
        if currentchar != encodedarray[0]:
            finishedproduct.write(str(counter) + currentchar)
            currentchar = encodedarray[0]
            counter = 0
            if len(encodedarray) == 1:
                finishedproduct.write(str(1) + encodedarray[0])
                return
            recall(counter, currentchar)
        if currentchar == encodedarray[0]: 
            encodedarray.pop(0)
            counter+=1
            recall(counter, currentchar)
    recall(counter, currentchar)
    return encodedarray

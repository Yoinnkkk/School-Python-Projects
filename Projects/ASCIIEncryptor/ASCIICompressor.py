# main function

def compress(object):
    object = open(object, "r").read()
    encryptedarray = []
    counter = 0
    #seperates ascii art into array
    for string in object:
        if len(string) > 0:
            encryptedarray.append(string)
    #counter for all ascii characters
    currentchar = encryptedarray[0]
    def recall(counter, currentchar):
            while currentchar == encryptedarray[0]: 
                encryptedarray.pop(0)
                counter+=1
            if currentchar != encryptedarray[0]:
                open("Projects/ASCIIEncryptor/ASCIICompressed.txt", "a").write(str(counter) + currentchar)
                currentchar = encryptedarray[0]
                counter = 0
                if len(encryptedarray) == 1:
                    open("Projects/ASCIIEncryptor/ASCIICompressed.txt", "a").write(str(1) + encryptedarray[0])
                recall(counter, currentchar)
    recall(counter, currentchar)
    return encryptedarray

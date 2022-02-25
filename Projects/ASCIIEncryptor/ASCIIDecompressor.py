
# main function
def decompress(object):
    object = open(object, "r").read()
    decodedarray = []
    counter = 0
    finishedproduct = open("Projects/ASCIIEncryptor/ASCIIDecompressed.txt", "a")
    for string in object:
        decodedarray.append(string)
    def recall(counter):
        if decodedarray[0] == '0' or decodedarray[0] == '1' or decodedarray[0] == '2' or decodedarray[0] == '3' or decodedarray[0] == '4' or decodedarray[0] == '5' or decodedarray[0] == '6' or decodedarray[0] == '7' or decodedarray[0] == '8' or decodedarray[0] == '9':
            if decodedarray[1] == '0' or decodedarray[1] == '1' or decodedarray[1] == '2' or decodedarray[1] == '3' or decodedarray[1] == '4' or decodedarray[1] == '5' or decodedarray[1] == '6' or decodedarray[1] == '7' or decodedarray[1] == '8' or decodedarray[1] == '9':
                counter = int(decodedarray[0] + decodedarray[1])
                decodedarray.pop(0)
                decodedarray.pop(0)
                recall(counter)
            else:
                counter = int(decodedarray[0])
                decodedarray.pop(0)
                recall(counter)
        else:
            while counter != 0:
                finishedproduct.write(decodedarray[0])
                counter-= 1
            decodedarray.pop(0)
            counter = 0
            recall(counter)
    recall(counter)
    return 

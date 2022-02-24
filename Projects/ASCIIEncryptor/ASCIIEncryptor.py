#imports
import string
#import array file along with other variables
art = open("Projects/ASCIIEncryptor/ASCIIArt.txt", "r").read()
alphabet = string.printable
# main function

def encrypt(object):
    encryptedarray = []
    counter = 0
    for alphabet in object:
        if len(alphabet) > 0:
            encryptedarray.append(alphabet)
            encryptedarray.pop(encryptedarray.index(alphabet))
            counter+=1
            print(counter)
    return encryptedarray

print(encrypt(art))
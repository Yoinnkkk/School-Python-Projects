with open("Projects/Wordle Recreation/Python/dictionary.txt", "r", errors="ignore") as f1:
    read,array,i = f1.readlines(),[],1
    for x in read:
        x = x.rstrip()
        array.append(x)
    while len(array) > 0:
        for c in array:
            if len(c) == i:
                with open("dict"+str(i)+".txt", "a") as f2:
                    f2.write(c+"\n")
                    array.pop(array.index(c))
            elif c == array[-1]:
                print("Alphabet "+str(i)+" is finished")
                i+=1
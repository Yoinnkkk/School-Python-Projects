#################################################### 1
MyItem = int(input("please enter a number"))
MyList = [1,2,3,4,5,6,7,8,9,10]
match = False
position = 0
while position < len(MyList) and match == False:
    if MyList[position] == MyItem:
        match = True
    position = position + 1
print(match)

#################################################### 2 
def linearsearch (myItem,myList):
    match = False
    position = 0
    while position < len(myList) and match == False:
        if myList[position] == myItem:
            match = True
        position = position + 1
    return match
A = int(input())
B = [1,2,3,4,5,6,7,8,9,10]
print(linearsearch(A,B))

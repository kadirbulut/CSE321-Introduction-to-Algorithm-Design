def compareScales (leftScaleList, rightScaleList):
    result = sum(leftScaleList) - sum(rightScaleList)
    if result < 0:
        return 1
    elif result > 0:
        return -1
    else:
        return 0



def findRottenWalnut(inputList):
    flag=0
    #seperate the list into two part (left and right and compare their weights)
    a= compareScales(inputList[:int(len(inputList)/2)],inputList[int(len(inputList)/2):])
    #if left and right have equal weights . (namely,list's length is even number)
    if a==0:
        return -1
    #if the element is last element
    if len(inputList) == 1:
        return 0
    #check that if list's length is an odd number.    
    if len(inputList) % 2 == 1:
        if inputList[0] < inputList[1]: # if list's first element is lighter element
            return 0
        else:
            del inputList[0] #delete the first element if it is not lighter element
            if compareScales(inputList[:int(len(inputList)/2)],inputList[int(len(inputList)/2):]) == 0:
                return -1
            else:
                flag=1
				#scale left and right again
                a= compareScales(inputList[:int(len(inputList)/2)],inputList[int(len(inputList)/2):])
    #if left part is more lighter than right part,turn left
    if a==1:
        if flag == 1:
            return findRottenWalnut(inputList[:int(len(inputList)/2)]) + 1
        else:
            return findRottenWalnut(inputList[:int(len(inputList)/2)])
    #if right part is more lighter than left part,turn rihgt and increase (half of list's lenght )the searched element's index
    if a==-1:
        if flag == 1:
            return findRottenWalnut(inputList[int(len(inputList)/2):]) + int(len(inputList)/2) + 1
        else:    
            return findRottenWalnut(inputList[int(len(inputList)/2):]) + int(len(inputList)/2)
        
inputList=[1,1,1,1,1,0.5,1,1,1]      
index=findRottenWalnut(inputList)
print("Index:",index);




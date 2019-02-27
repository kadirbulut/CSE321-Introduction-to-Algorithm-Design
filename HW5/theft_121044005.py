def helper(inputArr,allCosts,row,column):
    if row>=0 and row<len(allCosts) and column<len(allCosts[0]):
        # if it has already been passed
        if allCosts[row][column] != -1:
            return allCosts[row][column]
        right=inputArr[row][column] + helper(inputArr, allCosts, row, column+1) # go right
        rightUp=inputArr[row][column] + helper(inputArr,allCosts, row-1, column+1) # go right-up
        rightDown=inputArr[row][column] + helper(inputArr,allCosts, row+1, column+1) # go right-down
        result=max(right,rightUp,rightDown) # select max of them
        allCosts[row][column]=result # replace the element with maximum cost
        return result
    return 0

def theft(inputArr):
    if not inputArr: # check that given matrix is empty or not
        return "empty matrix"
    rows=len(inputArr) # get num of rows
    columns=len(inputArr[0]) # get num of columns
    # create a 2d array to keep max costs
    allCosts = [[-1 for x in range(rows)] for x in range(columns)]
    maxMoney=-1
    i=0
    while i<rows:
        # find mox money for every row and return wich maximum of them
        maxMoney = max (maxMoney,helper(inputArr,allCosts,i,0))
        i+=1
    return maxMoney
    
    


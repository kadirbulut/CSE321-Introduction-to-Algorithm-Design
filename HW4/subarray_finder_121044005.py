def minimumSubArray(arr,head,tail):
    
    tempMin =  99999999999 #to check temp min array's
    minValue = 99999999999  # to check min array's 
    result=[]

    start=-1 # to keep min array's start index
    finish=-1 #to keep min array's finish index
    control=0 
    
    while control <= tail:
    
        if (tempMin > 0):
            tempMin = arr[control]
            if tempMin < minValue : # if there is exist another min array
                start = control # keep start index of subarray
        else:
            tempMin += arr[control] # add elements until finish index

        if tempMin < minValue :
            finish = control # keep finish index of subarray
            
        if tempMin < minValue : # if temp sum is smaller than minimum subarray's sum
            minValue=tempMin
            
        control += 1

    result = arr[start:finish+1] # get subarray with start and finish indexes

    return result   
    

def resultFunc(list1,list2,list3):
	#check that minimum sum of subarrays and return it
    if sum(list1)<sum(list2) and sum(list1)<sum(list3):
        return list1
    elif sum(list2)<sum(list1) and sum(list2)<sum(list3):
        return list2
    else:   
        return list3
    

def recursiveHelper(arr,head,tail): 
    if head ==  tail : # if division is terminated
            return arr
    mid = (head+tail)//2 # divide the array into two part 
    leftList=recursiveHelper(arr,head,mid) # get a subaray from left list
    rightList=recursiveHelper(arr,mid+1,tail) # get a subarray from right list
    return resultFunc(leftList,rightList,minimumSubArray(arr,head,tail)) 


def min_subarray_finder(arr):
    if not arr:
        return []
    elif len(arr) == 1:
        return arr
    else:
        return recursiveHelper(arr,0,len(inpArr)-1) # call recursive helper function


inpArr = [1, -4, -7, 5, -13, 9, 23, -1]
msa = min_subarray_finder(inpArr)
print(msa)
#Output: [-4, -7, 5, -13]
print(sum(msa))
#Output: -19

















def quickSortHoarePartition(arr,start,finish):
    
    pivElement=arr[start]
    i=start-1
    j=finish+1
    
    while True:
        while True:
            j=j-1
            if arr[j]<=pivElement:
                break
        while True:
            i=i+1
            if arr[i]>=pivElement:
                break
        if i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        else:
            return j
            
def helperH(arr,start,finish):
    
    if start < finish:
        m=quickSortHoarePartition(arr,start,finish)
        helperH(arr,start,m)
        helperH(arr,m+1,finish)
    
    return arr


def quickSortHoare(arr):
    return helperH(arr,0,len(arr)-1)


def quickSortLomutoPartition(arr,start,finish):
    pivot=arr[finish]
    s=start-1
    
    for i in range(start,finish+1):
        if arr[i] < pivot:
            s=s+1
            temp=arr[s]
            arr[s]=arr[i]
            arr[i]=temp
            
    temp=arr[finish]
    arr[finish]=arr[s+1]
    arr[s+1]=temp
    
    return s+1
    
def helper(arr,start,finish):
    
    if start < finish:
        m=quickSortLomutoPartition(arr,start,finish)
        helper(arr,start,m-1)
        helper(arr,m+1,finish)
        
    return arr

def quickSortLomuto(arr):
    return helper(arr,0,len(arr)-1)

arr = [15,4,68,24,75,16,42]
qsh = quickSortHoare(arr)
print(qsh)
#Output: [4, 15, 16, 24, 42, 68, 75]
qsl = quickSortLomuto(arr)
print(qsl)
#Output: [4, 15, 16, 24, 42, 68, 75]


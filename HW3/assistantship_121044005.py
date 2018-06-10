inputTable = [[5, 8,7],
              [8,12,7],
              [4, 8,5]]
              
#kombinasyon fonksiyonu
#gelen inp listesinden length uzunlugunda kac farkli list secilebilir ?
#bunu result listesinde return et
def comb(inp,length,result):
    if length == len(inp):
        if result.count(inp) == 0:
            result=result + [inp]
            result.sort()
        return result
        
    index=0
    while index < len(inp):
        newList=inp.copy()
        newList.pop(index)
        result = comb(newList,length,result)
        index+=1

    return result

              
#permutasyon fonksiyonu
#gelen inp listesi kac farkli siralanisa sahipse bir listeyle return et
def perm(inp):
    if len(inp) == 1:
        l=[]
        l.append(inp)
        return l
    else:
        result=[]
        
        i=0
        while i < len(inp):
            key = inp[i]
            newList=inp.copy()
            newList.pop(i)
            
            for others in perm(newList):
                others.insert(0,key)
                result.append(others)
            i+=1
    return result

#helper fonksiyon. input olarak bir table alir , permutasyon yardimi ile 
#kac farkli siralanis varsa hesaplar . hesaplanan tum durumlar ıcın zaman 
#hesaplamasi yapar ve en optimal olan siralanisi ve zamanı return eder
def find(inputTable):
    
    RA=len(inputTable) # get research assistants' size
    courses=len(inputTable[0]) #get courses' size
    
    #get index of RA's into a list
    temp=[]
    for x in range(0,courses):
        temp.append(x)
    
    # get all conditions for RA's with permutation
    allConditions=perm(temp)
    
    allSums=[] #to keep times
    
    #calculate total times for every condition in the permutation of table
    for i in allConditions:
        tempSum=0
        for j in range(0,courses):
            tempSum+=inputTable[j][i[j]]
        allSums.append(tempSum) #add sums to list
        
    #get result order with min time's index    
    resultList=allConditions[allSums.index(min(allSums))]  
    #get min. time
    minTime=min(allSums)
    return (resultList,minTime) # return the optimal result
              
def findOptimalAssistantship(inputTable):
    
    RA=len(inputTable) #get size of RA's
    courses=len(inputTable[0]) #get size of courses
    
    #if RA < courses return an empty list 
    if RA < courses:
        emptyList=[]
        return (emptyList,-1)
    
    if RA == courses :
        return find(inputTable)
    
    else:

        resultLists=[] #to keep result lists
        resultTimes=[] # to keep result times
        minTime=0 # to keep min time's index
        
        #get RA's indexes
        indexes=[]
        for i in range(0,RA):
            indexes.append(i)
        
        #get possible order's for all RA's (up to the number of courses)
        l=[]
        allCombins=comb(indexes,courses,l)
    
        #evaluate all conditions
        for i in allCombins:
            temp=[]
            for j in range(0,courses):
                temp.append(inputTable[i[j]])
            temp=find(temp) # get a optimal solution for a situation
            resultLists.append(temp[0]) # get optimal list and add result list as a sublist
            resultTimes.append(temp[1])  # get optimal time and add result list as a value
            
        # add time of department assistants
        minTime=min(resultTimes) + (RA-courses)*6  
        # get total time's index
        minIndex=resultTimes.index(min(resultTimes))
        #get result assigned list
        resultRAs=allCombins[minIndex]
        assigned=resultLists[minIndex]
        
        result = [-2] * RA # for result list to return 
        
        # match RA's and courses according to indexes
        for i in range(0,RA):
            if i not in resultRAs:
                result[i]=-1
            else:
                result[i]=assigned.pop(0)
        
            
        return (result,minTime) #return the result

    
asst, time =findOptimalAssistantship(inputTable)
print(asst)
print(time)


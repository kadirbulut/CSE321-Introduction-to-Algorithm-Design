def checkThat1orOwn(arr,index):
    #elemanın 1 olup olmayacağına yada Y listesindeki elemana eşit olup
    #olmayacağına karar ver
    size=len(arr)
    if index == 0: # baştaki elemansa
        if (abs(arr[1]-arr[0]) < abs(arr[1]-1)) and (abs(arr[2]-arr[1]) > abs(arr[2]-1)) :
            return 1
        else:
            return arr[index]

    if index == size-1: # sondaki elemansa
        if abs(arr[size-1]-arr[size-2]) < abs(1-arr[size-2]):
            return 1
        else:
            return arr[index]
    
    #ortalarda bir elemansa
    if (abs(arr[index]-arr[index-1]) + abs(arr[index+1]-arr[index])) < ((abs(1-arr[index-1]) + abs(arr[index+1]-1))):
        return 1
    else:
        return arr[index]       
    
    
def helper(arr,X):
    size=len(arr)    
    for i in range(0,size): #sırası ile tüm elemanları belirle 
        if i==0:
            X[i] = checkThat1orOwn(arr,i)
        elif i==size-1:
            X[i] = checkThat1orOwn(arr,i)
        else:
            X[i] = checkThat1orOwn(arr,i)
            #sonraki eleman 1 olacaksa ve toplamı küçültecekse
            if checkThat1orOwn(arr,i+1)==1 and arr[i+1] < arr[i]:
                X[i]=arr[i]
                
        if i != size-1:
            #peş peşe 3 eleman 1 e eşit değilse ve ortadaki eleman 1 olursa max. oluyorsa
            if arr[i-1] != 1 and arr[i]!=1 and (abs(arr[i]-arr[i+1]) < abs(1-arr[i+1])):
                X[i]=1
        
        arr[i]=X[i] # y listesindede güncelle elemanı
           
    maxCost=0     
    for i in range(1,size): # listenin elemanlarının faklarının mutlak değer toplamı
        maxCost += abs(X[i]-X[i-1])     
    
    return maxCost  #sonuç      

def find_maximum_cost(Y):
    if not Y: #liste boş gelirse
        return 0
    
    if len(Y)==1: # tek elemanlı gelirse
        return Y[0]
    
    if len(Y) == 2: # 2 elemanlı gelirse
        return abs(max(Y)-1)
    
    X=[-1 for number in range(0,len(Y))] # X listesini oluştur
    return helper(Y,X) 
    
   


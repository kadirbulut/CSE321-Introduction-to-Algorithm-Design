#   Bu soruda Y listesinden X listesini ederken X listesinde mutlak değerlerin
#   farkının toplamının maximum olması gerektiği için ;
#   1<=X[i]<=Y[i] kuralından max elde ertmek için öncelikle X listesini  
#   elde ederken X listesinin i. indexindeki elemanının ya Y listesinin i.
#   indexindeki elemana eşit olması yada 1 e eşit olması gerekli.
#   Öncelikle soruda Y listesinin uzunluğuna eşit olan bir X listesi oluşturdum.
#   Burada X listesinin elemanlarını elde ederken 0 dan başlayarak sonuncaya
#   doğru birdaha geri dönmemek üzere her indexteki elemanı bularak ilerlemeye
#   çalıştım.
#   Elemanların ne olacağına karar verip ilerlemek için her elemanda çeşitli
#   kontroller gerçekleştirdim.
#   Bu kontroller;
#   -eğer listenin ilk elemanı ise kendinden sonra gelen elemanla farkı
#   -eğer listenin son elemanı ise kendinden önce gelen elemanla farkı
#   -ortalarda bir eleman ise kendinden önce ve sonra gelen elemanlarla 
#   toplamlarının farkı.
#   -ayrıca ek kontrol olarak i+1. eleman 1 olacaksa ve max toplamı küçültecekse
#   i. elemanı 1 yapma durumunu kontrol ettim
#   -son olarak ortalarda peş peşe 3 elemanda 1 e eşit olmuyorsa ve ortadaki
#   elemanın 1 olma durumu max toplamı artırıyorsa ortadaki yani bulunduğum
#   indexteki elemanın 1 e eşit olma durumunu
#   Bütün bu kontrollerden sonra X listesini elde etmiş oluyorum ve max cost u
#   hesaplayıp return ediyorum.
#
#   Worst Case Analysis
#   find_maximum_cost fonksiyonumun içinde helper fonksiyonumu 
#   helper fonksiyonumun içinde de checkThat1orOwn fonksiyonumu çağırıyorum
#
#   checkThat1orOwn= O(1) ---> sadece statementlardan oluşuyor
#   helper fonksiyonumda ise for döngüsü  ;
#   n elemanlı bir Y listesi girdisi için n kez dönüyor
#   diğer for döngüsü n-1 kez dönüyor(absolute differences sum için)
#   
#   Time = O(n+(n-1)) = O(n)

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
    
   


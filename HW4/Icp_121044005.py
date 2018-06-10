# 	*Bu sorudada ilk soru gibi aldığım string listini sürekli olarak ikiye bölerek
# ilerliyorum . 
#
#	*Listenin size ına göre her seferinde middle değerin indexini bulup bu
# değere göre listeyi sol ve sağ olmak üzere ikiye bölüyorum.Ta ki 1 eleman
# kalana kadar.
#	
#	*Soldan ve sağdan elde ettiğim listelerdeki stringleri compareTwoString
# fonksiyonumla kontrol edip postfix olarak ortak stringi return ediyorum . 
#   
#	*Her seferinde elde ettiğim postfix stringi de bir sonraki aşamada kullanarak
# sonuca ulaşmaya çalışıyorum. 
#
#   *compareTwoString fonksiyonumda kontrol sayısı olarak uzunluğu küçük olan 
#   stringi kullanıyorum her defasında . Çünkü küçük string kadar kontrol edilebilir
#   max. Ve sonuç olarak sondan eşit olan elemanlarını bulup return ediyorum.
#
#   Worst Case Analysis
#   
#   T(n) = T(n/2) + T(n/2) 
#   
#   compareTwoString fonksiyonumun çalışma zamanı linear ;
#   O(n)
#
#   Toplam karmaşıklık;
#
#   T(n)=T(n/2) + T(n/2) + O(n)
#   T(n)=2T(n/2)+O(n)
#   T(n)=O(nlogn)




def compareTwoString(inp1,inp2):
    #find control size
    if len(inp1) >= len(inp2):
        controlSize=len(inp2)
    else:
        controlSize=len(inp1)

    result=""
    #check common elements
    for i in range(0,controlSize):
        if inp1[len(inp1)-1-i] != inp2[len(inp2)-1-i] :
            break
        else:
            result=inp2[len(inp2)-1-i]+result #add an element to result
            
    return result
    

def recursiveHelper(arr,head,tail):    
    if head ==  tail :
    	return arr[head]
    mid = (head+tail)//2
    strLeft=recursiveHelper(arr,head,mid) #get left string
    strRight=recursiveHelper(arr,mid+1,tail) #get right string
    
    return compareTwoString(strLeft,strRight) # check left and right strings

def longest_common_postfix(inpStrings):
    if not inpStrings:
        return []
    return recursiveHelper(inpStrings,0,len(inpStrings)-1)
    

inpStrings = ["absorptivity", "circularity" , "electricity", "importunity", "humanity"]
lcp = longest_common_postfix(inpStrings)
print(lcp)



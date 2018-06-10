#	Bu algoritmada da recursive olarak iki liste üzerinde ilerlemeye çalışıyorum.
#	Fakat diğer algoritmada her seferinde iki listeninde middle elementlerini 
#	karşılaştırıp birinin yarısını atarak ilerlerken ;  
#	Bu algoritmada ; 
#	-> Recursive kısmı k//2 defa çalıştırıyorum.
#	-> controlM ve controlN adlı iki değişken tutarak her defasında son bulunan 
#	elemandan itibaren controlM. yada controlN. elemanları bulup ilerleyerek 
#	k. elemana ulaşmaya çalışıyorum.
#	-> Her aşamada gelinen noktada m yada n de hangi noktada kalmışsam 
#	elemanlarını karşılaştırıp alfabetik olarak ön sırada olanın solunu alarak
#	ilerlemeye çalıştım.
#	->Sonuç olarak diğer algoritmadan farklı olarak decrease kısmı k//2 kez
#	gerçekleşeceğinden karmışıklığı O(logk) olacaktır.


def helper(m,n,k):
    #if m is null kth element is in n list
    if len(m)==0:
        return n[k-1]
    #if n is null kth element is in m list   
    if len(n)==0:
        return m[k-1]

    #if k is the next element , k is the smallest element between m[0] and n[0]
    if k==1:
        if m[0] < n[0]:
            return m[0]
        else:
            return n[0]

	#get controlM to divide list m

    if len(m) < (k//2) :
        controlM=len(m)
    else:
        controlM=k//2
        
	#get controlM to divide list n

    if len(n) < (k//2):
        controlN=len(n)
    else:
        controlN=k//2
        
    if m[controlM-1] > n[controlN-1]:
		# find controlN th element from last available element
        k=k-controlN
        return helper(m,n[controlN:],k)
    else:
		# find controlM th element from last available element
        k=k-controlM
        return helper(m[controlM:],n,k)
    

def find_kth_book_2(m,n,k):
    if k<1:
        return []
    if k > len(m) + len(n):
        return []
    return helper(m,n,k)

m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]
book = find_kth_book_2(m,n,4)
print(book)
#Output: oop
book = find_kth_book_2(m,n,6)
print(book)
#Output: systemsprogramming

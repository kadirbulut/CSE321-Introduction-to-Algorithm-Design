#	*Bu soruda logm+logn karmaşıklığı istendiğinden dolayı her aşamada 
#	m yada n listesinin sol yada sağ yarını alarak k. elemanı bulmaya çalıştım
#	*Her aşamada listeden attığım eleman sayısı kadar k ya yakınlaştığımı da
#	kontrol edip k. elemana ulaşmaya çalıştım.
#	*Öncelikle m yada n listelerinden birinin boşaldığı durumda aranan elemanı
#	dolu olan listede aradım.(Yani arranan elemanın dolu olan listede olduğu 
#	kesinleşmiş oluyordu.)
#	*Yine her aşamada listelerin yarısının uzunluklarının toplamını bularak ve k
#	ile karşılaştırarak aradığım elemanın soldaki yarım listelerde olup 
#	olmadığını kontrol ettim.
#		Kontrol uzunluğumun k dan daha büyük ise aramaya devam ettim listeleri 
#		küçülterek.
#		
#	*Listeleri elemek için ise şu durumları kontrol ettim ; 
#	-> Eğer sol yarımlarda ise aranan eleman ; 
#		-Orta elemanları karşılaştırıp , sıralama olarak önde olan elemanın   
#		bulunduğu listenin sol yarısını alıp sağ yarısını listeden çıkardım her seferinde
#	-> Eğer aranan eleman sağ yarımlarda ise;
#		-Yine ortadaki elemanları karşılaştırıp sıralama olarak geride olan
#		elemanın bulunduğu listenin sağ yarısını alıp sol yarısını listeden
#		atarak devam ettim.
#
#	Gerekli küçültme işlemlerinden sonra kth elemanı return ettim.	
#

def helper(m,n,k):
    if not m : # if m is null k th element in the n
        return n[k] 
    if not n : # if n is null k th elemen in the m 
        return m[k]
        
    mlen=len(m) # get m's length
    nlen=len(n) # get n's length

    controlLength = (mlen//2) + (nlen//2) # check that the left halfs are enough for k

    if controlLength < k : # if k th element is in the left halfs
        if m[mlen//2] > n[nlen//2] :
            eliminated=(nlen//2)+1
            return helper(m,n[(nlen//2)+1:], k-eliminated)
        else:
            eliminated=(mlen//2)+1 # get num of eliminated elements
            return helper(m[(mlen//2)+1:], n, k-eliminated)
    else: # # if k th element is not in the left halfs , or in right halfs
        if m[mlen//2] > n[nlen//2] :
            return helper(m[:mlen//2],n,k)
        else:
            return helper(m,n[:nlen//2],k)

def find_kth_book_1(m,n,k):
    if k<1:
        return []
    if k > len(m) + len(n):
        return []

    return helper(m,n,k-1)

m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]
book = find_kth_book_1(m,n,4)
print(book)
#Output: oop
book = find_kth_book_1(m,n,6)
print(book)
#Output: systemsprogramming

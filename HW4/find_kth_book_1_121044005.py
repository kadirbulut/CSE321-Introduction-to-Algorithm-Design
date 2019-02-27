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

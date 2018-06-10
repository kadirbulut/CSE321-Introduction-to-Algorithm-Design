def TOH(n,frompeg,topeg,auxpeg,arr):
    if n==1: # disk 1's move
        print ("disk 1:",frompeg," to ",topeg)
		#increase 2 if move between SRC and DST , otherwise increase 1 and multiply with 1 (with weight)
        if (frompeg=="DST" and topeg=="SRC"):
            arr[0] += 2
        elif (frompeg=="SRC" and topeg=="DST"):
            arr[0] += 2
        else:
            arr[0] += 1

        return 0
    else:
		#increase 1 in all moves of disk 2 and multply with 2 (with weight)
        if n == 2:
            arr[1] += (1*2)
		#In disk3's moves increase 2 if move between SRC and DST , otherwise increase 1 and multiply with 3 (weight)
        if n == 3:
            if (frompeg=="DST" and topeg=="SRC"):
                arr[2] += (2*3)
            elif (frompeg=="SRC" and topeg=="DST"):
                arr[2] += (2*3)
            else:
                arr[2] += (1*3)
        
        TOH(n-1,frompeg,auxpeg,topeg,arr)
        print ("disk",n,":",frompeg," to ",topeg) # print disk2 and disk3's moves
        TOH(n-1,auxpeg,topeg,frompeg,arr)
    
    

def TOHtime(n):
	#print the input size
    print("Input size is",n,"\n")
    a = [0] * n # to keep n disk's times
    TOH(n,"SRC","DST","AUX",a)
    #print the elapsed times
    print("\nElapsed time for disk 1:",a[0])
    print("Elapsed time for disk 2:",a[1])
    print("Elapsed time for disk 3:",a[2])


TOHtime(3) #call the function

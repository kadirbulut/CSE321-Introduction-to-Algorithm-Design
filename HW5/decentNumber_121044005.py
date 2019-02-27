def decentNumber(num):
    
    count3=num//3 # first find out how many 3's (for 5 digit)
    count5=0    # for num of 5's (for 3 digit)
    
    while count3 > 0: 
        if (num - (count3*3)) % 5 == 0:
            # if I found the num with num of 3's and 5's
            result = count3*3*'5' + count5*5*'3' # get result string
            return result
        else:
            # if I don't found the num with num of 3's and 5's
            count3-=1 # decrease 1 num of 3's (5 digits)
            temp= num - (count3*3 + count5*5) # get overflow
            #if overflow is bigger than 5 
            if temp >= 5:
                count5+=1 # increase 1 num of 5's (3 digits)
            
    # check that number can be obtained
    if (count3*3 + count5*5) == num:
        result = count3*3*'5' + count5*5*'3'
        return result
    # else result is -1
    else:
        return "-1"

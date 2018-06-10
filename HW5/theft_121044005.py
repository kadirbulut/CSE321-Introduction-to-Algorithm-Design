#   *Algoritmayı dinamik programlama kullanarak çözümlememiz istenmiş.
#   *Soruda hırsızın maximum parayı toplaması için belli bir rowdan yola çıkması
#   gerekiyor.
#   *Yine algoritmada 3 farklı harekete izin verilmiş.Bunun için;
#       -Sağa gitmek için x,y den x,y+1 (1 column artır)
#       -Sağ üste gitmek için x,y den x-1,y+1 (1 row azalt , 1 column artır)
#       -Sağ alta gitmek için x,y den x+1,y+1 (1 row artır , 1 column artır)
#   algoritmalarını kullandım recursive olarak.
#   *İlerlerken her adımda sağa yada çapraz olarak aşağı mı yukarı mı gitmek için max
#   olanı tercih ettim
#   *Gezdiğim pathlerde her seferinde geldiğim kısma kadar olan kısmı saklamak
#   için 2 boyutlu bir array oluşturdum,soruda verilen matrixin row ve column
#   sayısı ile
#   *Oluşturduğum bu arrayde her seferinde gittiğim kısma kadar olan maximum
#   moneyi tuttum.
#   *Her ilerleyişimde ise bir sonraki kadar adıma kadar gidip maximum moneyi 
#   bulup geriden geldiğim kısmı bulduğum yeni max money ile artırdım
#   *Böylece en sona geldiğimde her seferinde bir önceki adıma kadar     
#   toplayabileceğim max. moneyleri tuttuğum için sonuçtada gerideki adımları
#   kullanarak sonuç olan max moneyi elde etmiş oldum.
#
#   Worst Case Time Complexity:
#   Her seferinde sağ,sağ-üst,sağ-alt olmak üzere 3 farklı duruma recursive
#   olarak ayrıldığından dolayı zaman karmaşıklığı exponensiyeldir.
#
#   m satır ve n sütündan oluşan bir matrix için ; 
#   k=m+n dersek;
#   Time Complexity = 3^k olur.    


def helper(inputArr,allCosts,row,column):
    if row>=0 and row<len(allCosts) and column<len(allCosts[0]):
        # if it has already been passed
        if allCosts[row][column] != -1:
            return allCosts[row][column]
        right=inputArr[row][column] + helper(inputArr, allCosts, row, column+1) # go right
        rightUp=inputArr[row][column] + helper(inputArr,allCosts, row-1, column+1) # go right-up
        rightDown=inputArr[row][column] + helper(inputArr,allCosts, row+1, column+1) # go right-down
        result=max(right,rightUp,rightDown) # select max of them
        allCosts[row][column]=result # replace the element with maximum cost
        return result
    return 0

def theft(inputArr):
    if not inputArr: # check that given matrix is empty or not
        return "empty matrix"
    rows=len(inputArr) # get num of rows
    columns=len(inputArr[0]) # get num of columns
    # create a 2d array to keep max costs
    allCosts = [[-1 for x in range(rows)] for x in range(columns)]
    maxMoney=-1
    i=0
    while i<rows:
        # find mox money for every row and return wich maximum of them
        maxMoney = max (maxMoney,helper(inputArr,allCosts,i,0))
        i+=1
    return maxMoney
    
    


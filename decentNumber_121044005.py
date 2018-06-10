#   Soruda greedy aproach (aç gözlü yaklaşım) kullanmamız istendi.
#   Verilen digit sayısı büyüklüğündeki sayıyı 3 ve 5 digitleriyle elde edip 
#   daha doğrusu 3 ve 5 digitleriyle elde edilebilecek sayıların en büyüğü 
#   sorulduğundan dolayı algoritma gereği ; 
#   Öncelikle sayıyı tamamen 5 digitleriyle doldurmaya çalışıyorum,bunun için
#   yani 5 digitleriyle doldurmak için sayının 3 ün katları olma durumunu kontrol    
#   ediyorum.Bulunabilecek max. sayı tamamen 5 rakamlarıyla elde edilecek sayı.
#   Bunun için sayının 3 ün tam katı olması gerekli . Eğer değilse her seferinde
#   3 ün katı olma durumlarını eksiltip 5 in katı olma durumunu 1 artırıp ihtimale 
#   koyuyorum. Böyleliklede sayının tamamını 5 rakamlarından oluşturamasamda
#   5 rakamanın içerisinde max. sayıda geçtiği sayıyı elde etmeye çalışıyorum.
#   İçerisindeki 5 rakamlarının sayısını 3 ün , 3 rakamlarının sayısınıda 5 in
#   katı olması durumuyla kontrol ederken ; öncelik olarak verdiğim 3 ün katını 
#   bir azaltıp 5 in katı olma durumlarını devreye sokup sayıyı 3 rakamlarıyla
#   bulmaya çalışıyorum.Bunu yaparkende elimde olan countlarla bir sayı edip
#   verilen sayıdan çıkarıp kalanla kontrol ediyorum.Fonksiyonumda 3ün ve 5in 
#   katları sayısını tutup sonuç olarak ise öncelikle 3 ün sonra 5 in countlarıyla 
#   bir string oluşturup return ediyorum.


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

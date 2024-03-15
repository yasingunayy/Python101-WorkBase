# BİR DİZİDE HER ELEMAN İÇİN, O ELEMANDAN SONRA GELEN VE AYNI ZAMANDA ONDAN KÜÇÜK OLAN SAYILARIN 
# KONTROL EDİLDİĞİ VE KAÇ ADET SAYI OLDUĞUNUN BELİRLENİP KAYIT EDİLDİĞİ BİR ALGORİTMA

def controler(arr):
    new_arr = []
    for index1,item in enumerate(arr):
        counter=0
        for index2,numb in enumerate(arr):
            if item>numb and index1<index2:
                counter+=1

        new_arr.append(counter)
         
    return new_arr

arr = [5,7,2,9,11,4,3,8,14,17,10,1,2]
print(controler(arr))

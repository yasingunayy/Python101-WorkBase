# BİR SAYI DİZİSİ VERİLİYOR. BU SAYI DİZİSİNDE HER BİR ELEMANIN YERİNE O ELEMAN HARİÇ 
# DİZİDEKİ DİĞER TÜM ELEMANLARIN ÇARPIMINI YAZARAK YENİ BİR DİZİ OLUŞTURMANIZ İSTENİYOR.

arr = [8,3,1,7,2,14]

def multiplier(arr):
    new_arr = []
    result=1
    for numb in arr:
        index = arr.index(numb)
        arr.remove(numb)
        for item in arr:
            result *= item 

        new_arr.append(result)
        result=1

        arr.insert(index,numb)

    return new_arr

sonuc = multiplier(arr)
print(sonuc)   

# Dizinin elemanlarının toplam çarpım sonucunu bulup, bu çarpımı her ilgili elemana bölerek da yapılabilir.
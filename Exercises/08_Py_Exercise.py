# (GOOGLE MÜLAKAT SORUSU) ELİMİZDE BİR SAYI DİZİSİ VE K SAYISI VAR.BU DİZİDEKİ HERHANGİ 
# İKİ SAYININ TOPLAMININ K OLUP OLMADIĞINI BULAN BİR PROGRAM YAZIN. MÜMKÜNSE O(n) ZAMAN TÜKETMELİ.

arr = [10,25,11,7,4,2,21,13,9]
K = 16

def sum_control(arr,K):
    for numb in arr:
        if (K-numb) in arr:
            return True
        else:
            continue
    return False

print(sum_control(arr,K))

# Dizi sıralanıp baş ve son pivot noktalar kullanılarak da çözülebilir. Fakat diziyi sıralamak da 
# ekstra maliyet anlamına geliyor.
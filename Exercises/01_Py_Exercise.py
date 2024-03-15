# KULLANICIDAN ALINAN SAYININ FAKTÖRİYELİNİN HESAPLANMASI

def fact(numb):
    if numb==0:
        return 1
    elif numb>0:
        return numb * fact(numb-1)
    else:
        print("Hatalı giriş yaptınız.")


fact_number = int(input("Faktöriyel Hesabı İçin Sayı Giriniz..."))

print(fact(fact_number))


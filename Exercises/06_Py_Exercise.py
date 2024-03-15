# 1537 ŞEKLİNDE STRİNG OLARAK GİRİLEN DEĞERİN RAKAMLARI ÇARPIMINI HESAPLAYAN FONKSİYON

def digit_multiplier(input_str):
    result = 1
    for digit in input_str:
       result = int(digit)*result
    
    return result

input_string = input("Bir rakam dizisi giriniz...") 

if input_string.isdigit():
   print(digit_multiplier(input_string))
else:
    print("Hatalı bir giriş yaptınız.")    

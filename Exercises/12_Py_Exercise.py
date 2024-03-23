# RASTGELE TİPTE ELEMANLAR İÇEREN BİR LİSTEDEKİ SADECE STRİNG TİPİNDEKİ ELEMANLARI AYIRMA VE GERİ DÖNDÜRME

def return_str(arr):
    str_arr = []

    for item in arr:
        if type(item) == str:
            str_arr.append(item)
        else:
            pass

    return str_arr

arr = ["abc",5,71,[124,"klm"],"prs",198]
print(return_str(arr))


# VEYA

filter(lambda item: item if type(item)==str else None,arr)

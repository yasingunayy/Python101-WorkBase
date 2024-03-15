# BİR DİZİYİ TEKRAR EDEN TERİMLERDEN ARINDIRMA

arr = [5,6,2,8,12,45,3,2,485,89,2,3,2,6,7,9,5,1,2,5,77,8,96,2,1,8,2,4,9]

def clear_arr(arr):
    new_arr=[]
    for element in arr:
        if not (element in new_arr):
            new_arr.append(element)
        else:
            continue 

    return new_arr           

print(clear_arr(arr))
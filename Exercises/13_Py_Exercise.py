# DİZİDEKİ EN BÜYÜK İKİNCİ ELEMANIN BULUNMASI
import random

arr = []
for rand in range(20):
    arr.append(random.randint(0, 100))

searched_number = 0
largest = arr[0]   
for item in arr:
    if item>largest:
        searched_number=largest
        largest=item
    elif item > searched_number and item != largest:
            searched_number = item

            
print(sorted(arr))
print(searched_number)
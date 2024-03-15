# 1 İLE 100 ARASINDAKİ SAYILAR İÇİN 3 E BÖLÜNENLERİN YERİNE "Fizz", 5 E BÖLÜNENLERİN YERİNE "Buzz",
#  15'E BÖLÜNENLERİN YERİNE "FizzBuzz" YAZDIRALIM.

def FizzBuzz(arr):

    for index,item in enumerate(arr):
        if item%3==0 and item%5==0:
            arr[index] = "FizzBuzz"
        elif item%3==0:
            arr[index] = "Fizz"
        elif item%5==0:
            arr[index] = "Buzz"
            
    return arr

Number_arr = [*range(1,101)]      

print(FizzBuzz(Number_arr))
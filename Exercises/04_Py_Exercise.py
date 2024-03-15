# PALİNDROM STRİNGLERİ TESPİT ETME

def is_Palindrome(exmpl_word):
    exmpl_word = str(exmpl_word).lower()
    if exmpl_word == reverse_word(exmpl_word):
        return True
    else:
        return False

def reverse_word(input_word):
    input_arr = []
   
    for char in input_word:
        input_arr.append(char)

    input_arr.reverse()
    reversed_input = "".join(input_arr)
    return reversed_input

input_word = input("Palindrom Kontrolü için bir kelime giriniz...")
print(is_Palindrome(input_word))




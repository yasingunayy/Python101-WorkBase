# ANAGRAM STRİNGLERİN KONTROLÜ

def is_Anagram(word_1,word_2):
    word_1 = str(word_1).lower()
    word_2 = str(word_2).lower()

    if sorted(word_1) == sorted(word_2):
        return True
    else:
        return False


print(is_Anagram("KemaL","MelKa"))
def vogal(letra):
    if (letra == "a" or letra == "A" or 
        letra == "e" or letra == "E" or 
        letra == "i" or letra == "I" or 
        letra == "o" or letra == "O" or 
        letra == "u" or letra == "U"):
        return True
    else:
        return False

letra = input("Letra: ")

print(vogal(letra))


# Imprimir cada letra de una palabra

vocales = "aeiou"
palabra = input("Ingrese su palabra: ")

for letra in palabra:
    if letra.lower() in vocales:
        print(letra.upper())
    else:
        print(letra)
    
    
    
    
    
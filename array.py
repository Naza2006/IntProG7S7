numero = input("Dime un numero: ")

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
repetidos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for digito in numero:
    if digito == "0": += 1
        repetidos[0]
    elif digito == "1":
        repetidos[1] += 1
        
for i, j in zip(numeros, repetidos):
    print(i, j)
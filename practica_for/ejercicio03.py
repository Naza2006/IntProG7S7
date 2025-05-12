# Mostrar la tabla de multiplicar del numero 5

print("Cual es la tabla que desea aprender")
numero = int(input("Introduce un numero: "))
for i in range (1, 11):
    print(f"{numero} x {i} = {numero * i}")
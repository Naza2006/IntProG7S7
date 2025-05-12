# Promedio de N calificaciones

import datetime as dt
import time

fecha = dt.datetime.today()
print (f"Fecha actual: {fecha}")

cant = int(input("Cuantas notas: "))

suma = 0
for i in range (cant):
    nota = int(input(f"ingrese la calificacion {i+1}: "))
    suma += nota
    
promedio = suma / cant

cont = 0
tiempo_espera = 1
max_pasos = 10
espacios_iniciales = 10
os.system("cls || clear")

tiempo_espera = 1
while cont < max_pasos:
    print("Calculando promedio", end="")
    print({""} * (cont+1), end= "")
    print(f"{(cont+1) * 10}%")
    time.sleep(1)
    cont += 1

print("El promedio es: ", promedio)
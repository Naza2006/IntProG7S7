# Pedir una contraseña hasta que sea correcta

contraseña_correcta = "12345"
intentos = 0
while True:
    entrada = input("Escriba la contraseña: ")
    intentos += 1

    if entrada == contraseña_correcta:
        print("La contraseña es correcta")
        break
    else:
        print("La contraseña es incorrecta")
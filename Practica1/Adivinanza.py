import random


def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    print("Bienvenido al juego de adivinanza!")
    print("Debes adivinar un numero del 1 al 100")
    while not adivinado:
        adivinanza = input("Introduzca un numero del 1 al 100: ")
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor que {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menor que {adivinanza}")
            else:
                print(
                    f"Felicitaciones has ganado! El numero {adivinanza} es el secreto y lo has logrado en {intentos} intentos"
                )


juego_adivinanza()

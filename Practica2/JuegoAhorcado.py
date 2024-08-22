import random

def obtener_palabra() -> str:
    palabras = ["javascript","git","django","python","react"]
    return random.choice(palabras)

def avance(palabra_secreta, letras_adivinandas):
    adivinado = ''

    for letra in palabra_secreta:
        if letra in letras_adivinandas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado

def ahorcado():
    palabra_secreta = obtener_palabra()
    letras_adivinadas = []
    intentos = 10
    juego_terminado = False

    print("Bienvenido al juego del ahorcado!")
    print(f"Tenes {intentos} intentos para adivinar la palabra")
    print(avance(palabra_secreta, letras_adivinadas),"La cantidad de letras de la palabra es: ",len(palabra_secreta))

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor ingrese una letra valida")
        elif adivinanza in letras_adivinadas:
            print("Ya esta presente esa letra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"Muy bien has acertado, la letra '{adivinanza}' esta presente en la palabra")
            else:
                intentos -= 1
                print(f"Lo siento mucho, la letra '{adivinanza}' no esta presente en la palabra")
                print(f"Te quedan {intentos} intentos")

        progreso_actual = avance(palabra_secreta,letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(f"¡Felicitaciones has ganado el juego ! La palabra completa es '{palabra_secreta}'")


    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(f"Lo sentimos mucho se te han acabado los intentos, la palabra secreta era: '{palabra_secreta}'")

ahorcado()



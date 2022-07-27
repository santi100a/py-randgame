from sys import exit
from santitools.colors import colorize
from santitools.math import random
from santitools import clear

MAXIMO, conjetura, respuesta, nombre_jugador, jugar_nuevamente = 30, 0, 0, '', True
try:
    clear()
    print(colorize("¡Bienvenido al juego de números aleatorios!", "blue"))
    nombre_jugador = input("¿Cuál es tu nombre? ")
    respuesta = random(MAXIMO)
    while True:
        _conjetura = input(f'¿Cuál es tu conjetura (entre 0 y {MAXIMO})? ')
        if _conjetura == 'salir': break
        conjetura = int(_conjetura)
        if conjetura > MAXIMO:
            clear()
            print(colorize(f"¡No puedes adivinar un número mayor a {MAXIMO}!", "magenta"))
            continue
        elif conjetura < 0:
            clear()
            print(colorize("¡No puedes adivinar un número menor a 0!", "cyan"))
            continue
        elif conjetura == respuesta:
            clear()
            print(colorize(f"¡Hurra! {nombre_jugador}, ¡lo adivinaste! ", "green"))
            def validar(ent):
                if ent == "s":
                    return True
                elif ent == "n":
                    return False
                else:
                    return True
            jugar_nuevamente = validar(input(f"¿Te gustaría jugar nuevamente? ({colorize('s', 'green')}/{colorize('n', 'red')}) ").strip().lower()[0])
            if not jugar_nuevamente: break
            if jugar_nuevamente:
                respuesta = random(MAXIMO)
                continue
        elif conjetura != respuesta:
            clear()
            print(colorize(f"Lo siento {nombre_jugador}, ¡adivinaste incorrectamente!", "red"))
            continue
    exit(0)
except KeyboardInterrupt:
    exit(0)
except Exception as e:
    print(e)
    exit(1)
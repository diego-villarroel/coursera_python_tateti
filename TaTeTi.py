#coding: utf8
import os

#TABLERO
columna1_TaTeTi = ['_', '_', '_']
columna2_TaTeTi = ['_', '_', '_']
columna3_TaTeTi = ['_', '_', '_']
filas_TaTeTi = [columna1_TaTeTi, columna2_TaTeTi, columna3_TaTeTi]

def mostrar_tablero():
    print("|{}|{}|{}|".format(columna1_TaTeTi[0], columna1_TaTeTi[1], columna1_TaTeTi[2]))
    print("|{}|{}|{}|".format(columna2_TaTeTi[0], columna2_TaTeTi[1], columna2_TaTeTi[2]))
    print("|{}|{}|{}|".format(columna3_TaTeTi[0], columna3_TaTeTi[1], columna3_TaTeTi[2]))

#JUGADOR 1
def player1():
    seleccionPlayer1_columna = int(input("Selecciona una columna: ") - 1)
    seleccionPlayer1_fila = int(input("Selecciona una fila: ") - 1)

    player1_Fila = filas_TaTeTi[seleccionPlayer1_fila]
    player1_Columna = player1_Fila.insert(seleccionPlayer1_columna, 'X')

#JUGADOR 2
def player2():
    seleccionPlayer2_columna = int(input("Selecciona una columna: ") - 1)
    seleccionPlayer2_fila = int(input("Selecciona una fila: ") - 1)

    player2_Fila = filas_TaTeTi[seleccionPlayer2_fila]
    player2_Columna = player2_Fila.insert(seleccionPlayer2_columna, 'O')

#INTRODUCCION E INSTRUCCIONES
print("BIENVENIDOS A CLASIC TA-TE-TI - 2 Jugadores")
print("")
print("Hecho por Diego Villarroel")
print("")
print("")
print("")

print("Este es EL TABLERO")
print("|_|_|_|")
print("|_|_|_|")
print("|_|_|_|")
print("")
print("")

print("INSTRUCCIONES:")
print("* Para jugar tienes que seleccionar una columna |")
print("                                                v")
print("* Después tienes que elegir una fila -->")
print("")
print("")
print("¿Estas listo?")
raw_input("Presiona Enter para continuar")

os.system('clear')

#GAMEPLAY
print("Comienza el Jugador 1!")
print("")
print("|_|_|_|")
print("|_|_|_|")
print("|_|_|_|")
print("")
raw_input("Presiona Enter para continuar...")
print("")
player1()
os.system('clear')
print("Ahora es el turno del Jugador 2!")
print("")
mostrar_tablero()
print("")
player2()
os.system('clear')
print("Ahora es el turno del Jugador 1!")
print("")
mostrar_tablero()
print("")
player1()
os.system('clear')
print("Ahora es el turno del Jugador 2!")
print("")
mostrar_tablero()
print("")
player2()
os.system('clear')
print("Ahora es el turno del Jugador 1!")
print("")
mostrar_tablero()
print("")
player1()
os.system('clear')
print("Ahora es el turno del Jugador 2!")
print("")
mostrar_tablero()
print("")
player2()
os.system('clear')
print("Ahora es el turno del Jugador 1!")
print("")
mostrar_tablero()
print("")
player1()
os.system('clear')
print("Ahora es el turno del Jugador 2!")
print("")
mostrar_tablero()
print("")
player2()
os.system('clear')
print("Ahora es el turno del Jugador 1!")
print("")
mostrar_tablero()
print("")
player1()
os.system('clear')
print("Ahora es el turno del Jugador 2!")
print("")
mostrar_tablero()
print("")
player2()
os.system('clear')
print("Ahora es el turno del Jugador 1!")
print("")
mostrar_tablero()
print("")
player1()
os.system('clear')
print("Ahora es el turno del Jugador 2!")
print("")
mostrar_tablero()
print("")
player2()
os.system('clear')
print("Ahora es el turno del Jugador 1!")
print("")
mostrar_tablero()
print("")
player1()

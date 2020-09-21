#coding: utf8
import os
import sys

#TABLERO
columna1_TaTeTi = ['_', '_', '_']
columna2_TaTeTi = ['_', '_', '_']
columna3_TaTeTi = ['_', '_', '_']
filas_TaTeTi = [columna1_TaTeTi, columna2_TaTeTi, columna3_TaTeTi]

def mostrar_tablero():
    print("   0 1 2 --->")
    print("0 |{}|{}|{}|".format(columna1_TaTeTi[0], columna1_TaTeTi[1], columna1_TaTeTi[2]))
    print("1 |{}|{}|{}|".format(columna2_TaTeTi[0], columna2_TaTeTi[1], columna2_TaTeTi[2]))
    print("2 |{}|{}|{}|".format(columna3_TaTeTi[0], columna3_TaTeTi[1], columna3_TaTeTi[2]))
    print("")
    print("|")
    print("V")

#JUGADOR 1
def player1():
    seleccionPlayer1_columna = int(input("Selecciona una columna: "))
    seleccionPlayer1_fila = int(input("Selecciona una fila: "))

    fila_Player1 = filas_TaTeTi[seleccionPlayer1_fila]
    columna_Player1 = fila_Player1.insert(seleccionPlayer1_columna, 'X')

#JUGADOR 2
def player2():
    seleccionPlayer2_columna = int(input("Selecciona una columna: "))
    seleccionPlayer2_fila = int(input("Selecciona una fila: "))

    fila_Player2 = filas_TaTeTi[seleccionPlayer2_fila]
    columna_Player2 = fila_Player2.insert(seleccionPlayer2_columna, '0')

#WIN
def win_player1_col():
    for i in (0, 1, 2):
        if columna1_TaTeTi[i] == 'X' and columna2_TaTeTi[i] == 'X' and columna3_TaTeTi[i] == 'X':
            print("Ganó Jugador 1!!!")
            print("")
            mostrar_tablero()
            sys.exit()
        else:
            return -1

def win_player2_col():
    for i in (0, 1, 2):
        if columna1_TaTeTi[i] == '0' and columna2_TaTeTi[i] == '0' and columna3_TaTeTi[i] == '0':
            print("Ganó Jugador 2!!!")
            print("")
            mostrar_tablero()
            sys.exit()
        else:
            return -1

#TURNOS

def turno_player1():
    print("Ahora es el turno del Jugador 1!")
    print("")
    mostrar_tablero()
    print("")
    player1()
    os.system('clear')
    win_player1_col()

def turno_player2():
    print("Ahora es el turno del Jugador 2!")
    print("")
    mostrar_tablero()
    print("")
    player2()
    os.system('clear')
    win_player2_col()

#INTRODUCCION E INSTRUCCIONES
print("BIENVENIDOS A CLASIC TA-TE-TI - 2 Jugadores")
print("")
print("Hecho por Diego Villarroel")
print("")
print("")

print("Este es EL TABLERO")
print("")
mostrar_tablero()
print("")
print("")
print("")

print("INSTRUCCIONES:")
print("-------------")
print("")
print("* Para jugar tienes que seleccionar una columna |  desde 0 al 2")
print("                                                V")
print("")
print("* Después tienes que elegir una fila --->  también desde 0 al 2")
print("")
print("")
print("¿Estas listo?")
raw_input("Presiona Enter para continuar...")

os.system('clear')

#GAMEPLAY
print("Comienza el Jugador 1!")
print("")
mostrar_tablero()
print("")
player1()
os.system('clear')
# Hacer Iteracion hasta que gane alguien

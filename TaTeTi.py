#coding: utf8
import os

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

print("Comienza el Jugador 1!")
print("")
print("|_|_|_|")
print("|_|_|_|")
print("|_|_|_|")
print("")
raw_input("Presiona Enter para continuar...")
print("")

#TABLERO
columna1_TaTeTi = ['_', '_', '_']
columna2_TaTeTi = ['_', '_', '_']
columna3_TaTeTi = ['_', '_', '_']
filas_TaTeTi = [columna1_TaTeTi, columna2_TaTeTi, columna3_TaTeTi]

#JUGADOR 1
seleccionPlayer1_columna = int(input("Selecciona una columna: ") - 1)
seleccionPlayer1_fila = int(input("Selecciona una fila: ") - 2)

player1_Fila = filas_TaTeTi[seleccionPlayer1_fila]
player1_Columna = player1_Fila.insert(seleccionPlayer1_columna, 'X')

print("|{}|{}|{}|".format(columna1_TaTeTi[0], columna1_TaTeTi[1], columna1_TaTeTi[2]))
print("|{}|{}|{}|".format(columna2_TaTeTi[0], columna2_TaTeTi[1], columna2_TaTeTi[2]))
print("|{}|{}|{}|".format(columna3_TaTeTi[0], columna3_TaTeTi[1], columna3_TaTeTi[2]))

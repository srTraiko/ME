import os
from colorama import Fore

# Listado de bebidas añadidas
bebidas = []


def ascii_menu():
    print(f"""
    __________________________
   /                         /|        _____________________
  /       ^_^ TraiCORP      / |        |   Vista General   |
 /_________________________/  |        |{money}            |
 | |---------------------| |  |        --------------------
 | | Maquina Expendedora | |  |
 | |---------------------| |  |
 | | 1. Comprar          | |  |
 | |                     | |  |
 | |                     |  | |
 | |                     | |  |
 | |                     | |  |
 | |                     | | /
 | |_____________________| |/
 |_________________________/
 """)

def ascii_comprar():
    print("""
    __________________________
   /                         /|
  /       ^_^ TraiCORP      / |
 /_________________________/  |
 | |---------------------| |  |
 | | Maquina Expendedora | |  |
 | |---------------------| |  |
 | | 1. Pepsi         5$ | |  |
 | |                     | |  |
 | |                     |  | |
 | |                     | |  |
 | |                     | |  |
 | |                     | | /
 | |_____________________| |/
 |_________________________/
 """)

# Limpiar consola
def clear():
    if os.system == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

while True:
# Inicio
bot = Fore.RED + 'Robto 003: ' + '\033[39m'

print(bot + 'Hola mucho gusto, me presento, el dia de hoy sere tu maquina expendedora :D! \n')

money = int(input("Ingresa la cantidad de dinero que desees gastar: "))

clear()

while True:

    ascii_menu()

    opcion = input('Elige una opcion: ')

    # Comprar
    if opcion == 1:
        print(bot + "Bien, vas a comprar")
        clear()

        ascii_comprar()


        bebida = int(input('Bebida que vas a comprar: '))

        # Pepsi
        if bebida == 1:
            if money == 5:
                print('has comprado una pepsi')
                money -= 5


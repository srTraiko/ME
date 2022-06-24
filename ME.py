import os
# from typing import Type
from colorama import Fore

# base del programa 
bebidas = []

# Limpiar consola
def clear():
    if os.system == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

bot = Fore.RED + 'Robto 003: ' + '\033[39m'

print(bot + 'Hola mucho gusto, me presento, el dia de hoy sere tu maquina expendedora :D!')

# Revisar como resolver este error.

try:
    money = int(input(bot + 'Ingresa la cantidad de dinero que desees gastar: '))

except:
    print("error, ese numero no existe")
else:

    print(money)


    clear()

    def ascii_menu():
        print(f"""
            __________________________
           /                         /|        _____________________
          /       ^_^ TraiCORP      / |        |   Vista General   |
         /_________________________/  |        ---------------------
         | |---------------------| |  |                     {money}
         | | Maquina Expendedora | |  |         {bebidas}
         | |---------------------| |  |
         | | 1. Comprar          | |  |
         | | 2. vender           | |  |
         | | 3. Salir            | |  |
         | |                     | |  |
         | |                     | |  |
         | | 99. ???             | | /
         | |_____________________| |/
         |_________________________/
    """)

    def ascii_comprar():
        print(f"""
        __________________________
       /                         /|            ---------------------
      /       ^_^ TraiCORP      / |            |   Vista General   |
     /_________________________/  |            ---------------------
     | |---------------------| |  |                         {money}
     | | Maquina Expendedora | |  |            {bebidas}
     | |---------------------| |  |
     | | 1. Pepsi         5$ | |  |
     | | 2. Cocacola      5$ | |  |
     | | 3. Regresar         | |  |
     | |                     | |  |
     | |                     | |  |
     | |                     | | /
     | |_____________________| |/
     |_________________________/
     """)

    while True:

        ascii_menu()

        try:
            opcion = int(input('Selecciona una opcion: '))

            clear()

            # Comprar
            if opcion == 1:
                ascii_comprar()

                bebida = int(input("Selecciona una compra: "))

                # Comprar Pepsi
                if bebida == 1 and money >= 5:
                    bebidas.append('Pepsi')
                    money -= 5
                    print(f"Has comprado una Pepsi, tienes ahora {money}$")

                # Comprar Cocacola
                elif bebida == 2 and money >= 5:
                    bebidas.append("Cocacola")
                    money -= 5
                    print(f"Has comprado una Cocacola, tienes ahora {money}$")

                # Regresar
                elif bebida == 3:
                    clear()

                # No existe esa opcion
                else:
                    print("No existe esa opcion ;(")
        
            # Vender bebidas
            if opcion == 2:
                clear() 
        
                print(f"""
            ---------------------
            |   Vista General   |
            ---------------------
            {bebidas}
        
        
        """)
        
                vender = input(Fore.RED + "Escribe la bebida que deseas vender: " + '\033[39m')
        
                if vender == 'pepsi':
                    vender.lower()
                    bebidas.remove('Pepsi')
        
                elif vender == 'cocacola':
                    vender.lower()
                    bebidas.remove('Cocacola')
                else:
                    print('No existe esa bebida')
        
            # Salir
            if opcion == 3:
                os._exit(os.EX_OK)
        
        except ValueError:
            print("Error, ese numero no es valido")
            break
        

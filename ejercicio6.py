#Compañia de focos de colores 

import os
os.system("cls")


cantiFocos = int(input("Digite la cantidad de focos que quiere contabilizar: "))

if cantiFocos > 0:

    verdes = 0
    blancos = 0
    rojos = 0

    for i in range (cantiFocos):

        foco = str(input("Ingrese el color del foco: "))

        if foco == "verde": 
            
            verdes += 1
        
        elif foco == "blanco":

            blancos += 1
        
        else:

            rojos += 1
    
    print ("La cantidad de focos verdes es de ",verdes,", la cantidad de focos blancos es de ",blancos,
    ", mientras que la cantidad de focos rojos es de ",rojos)

else:
    print ("El número ingresado es incorrecto. Intente de nuevo")
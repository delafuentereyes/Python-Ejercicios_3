#Piramide de asteriscos

import os
os.system ("cls")

altura = 5
asteriscos = 1

for espacio in range  (altura, 0, -1):

    for e in range (espacio):

        print ("- ", end="")
    
    for a in range (asteriscos):

        print ("* ", end="")
    
    print()
    asteriscos += 2
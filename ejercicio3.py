#Contraseña con intentos limitados

import os
os.system("cls")

intentos = 1

while intentos <= 3:
    contra = input("Digite la contraseña: ")

    intentos += 1
    
    if contra == "8602":

        print ("Acceso permitido, bienvenido")
        intentos = 4
        break
    
    else:

        print ("Contraseña incorrecta")
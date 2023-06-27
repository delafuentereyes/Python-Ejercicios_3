#Usuario y contraseña

import os
os.system ("cls")

contador = 0

usuario = str(input("Digite su usuario: "))

while usuario == "pepe":

    contra = str(input("Digite la contraseña: "))
    
    while contra == "1709":

        print ("Acceso permitido. Bienvenido")
        break
        
        
    else: 

        print ("Intente de nuevo")


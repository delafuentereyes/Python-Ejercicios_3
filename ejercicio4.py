#Bono mensual

import os
os.system("cls")

cantidadAnnos = int(input("Digite la cantidad de años que lleva trabajando en la empresa: "))
sueldo = int(input("Digite lo que recibe de sueldo: "))

if cantidadAnnos >= 2 and cantidadAnnos < 5:

    total = sueldo + (sueldo * 0.2)

elif cantidadAnnos >=5:

    total = sueldo + (sueldo * 0.3)

    if sueldo < 1000:

        total = sueldo + (sueldo * 0.25)
    
    elif sueldo > 1000 and sueldo <= 3500:
        
        total = sueldo + (sueldo * 0.15)
    
    else: 

        total = sueldo + (sueldo * 0.1)

else: 

    print ("Bono no aplicable")

print ("El total del sueldo es de: ",total)







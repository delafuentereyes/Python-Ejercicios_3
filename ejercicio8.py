#Sueldo de trabajador

import os
os.system ("cls")

horas = int(input("Digite las horas trabajadas: "))
sueldoHora = float(input("Digite lo que gane por hora: "))
nombre = input("Digite el nombre del trabajador: ")

if sueldoHora > 0 and sueldoHora < 150:

    total = sueldoHora*horas
    sueldoHora = sueldoHora - (total*0.5)

elif sueldoHora > 150 and sueldoHora < 300:

    total = sueldoHora*horas
    sueldoHora = sueldoHora - (total*0.7)
    
else: 

    total = sueldoHora*horas
    sueldoHora = sueldoHora - (total*0.9)
    
print ("El sueldo de",nombre," es de: ",total)

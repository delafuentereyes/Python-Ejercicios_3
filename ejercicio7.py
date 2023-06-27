#Cuenta de ahorros en banco

import os
os.system ("cls")

total = 0
interes = 0

annos = int(input("Ingrese la cantidad de años que desea ahorrar: "))

while annos > 0:
    for i in range (1,12):

        ahorro = float(input("Digite el ahorro del mes: "))
        total = total + ahorro
    
    interes = interes + (total*0.1)
    annos = annos-1
    print ("El interes anual es",interes," y la inversion final es de ",total+interes)


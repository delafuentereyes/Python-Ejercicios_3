#Productos del super pepe

import os 
os.system("cls")

condicion = "si"
conta = 0
total = 0

print ("Bienvenido a Super Pepe")
print ("\n")
precioArticulo = int(input("Digite el precio del producto que está adquiriendo: "))
cantiArticulo = int(input("Digite la cantidad de productos que está adquiriendo: "))

while condicion.lower() == "si":

    if precioArticulo >= 10000:

        total = precioArticulo*cantiArticulo
        precioArticulo = precioArticulo - (total*0.15)
        total = precioArticulo*0.13

    condicion = input("Desea continuar? Digite si o no: ")

    while condicion.lower() != "si" and condicion.lower() != "no":

        condicion = input("Por favor digite si o no, no otra cosa: ")
conta = conta + 1 

print ("Usted adquirio",cantiArticulo," productos y el total de su compra es de: ",total)
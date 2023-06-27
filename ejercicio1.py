#Notas de estudiantes 
import os
os.system ("cls")

condicion = "si"
conta = 0

while condicion.lower() == "si":

    nota1 = int(input("Digite la nota del estudiante: "))
    nota2 = int(input("Digite la nota del estudiante: "))
    nota3 = int(input("Digite la nota del estudiante: "))

    total = (nota1+nota2+nota3)/3

    print ("Desea continuar? Digite si o no")
    condicion = input()

    while condicion.lower() != "si" and condicion.lower() != "no":

        print ("Por favor digite si o no, no otra cosa")
        condicion = input()
conta = conta + 1 

print ("El promedio total es de: ",total)
    



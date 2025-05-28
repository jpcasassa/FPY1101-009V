# datos de usuario
numBase = int(input("Ingrese un número base: "))
numExpo = int(input("Ingrese un exponente: "))

# cualquier número elevado a 0 es 1 
numTotal = 1
if numBase > 0 :
# Usamos un ciclo for para multiplicar la base por sí misma
    for i in range(numExpo):
        numTotal = numTotal * numBase
elif numExpo != 0 :

    

else 

# resultado final
print("El número", numBase, "elevado a", numExpo, "es:", numTotal)


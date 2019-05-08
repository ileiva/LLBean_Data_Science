# Ejercicio: Escribir un for para buscar el máximo de la lista e imprimirlo

lista = [44,11,15,29,53,12,30]

maximo = 0

for i in lista:
    if i > maximo:
        maximo = i

print('el maximo es=',maximo)

# con el max

print('el maximo es=',max(lista))

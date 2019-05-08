# esto es un ejemplo de tuplas

# crear una tupla de 5 elementos de tipos diferentes

mi_tupla = (1,'l','mi texto', True)

# imprimir la tupla

print(mi_tupla)

# como podria hacer para agregar mas elementos!

mi_tupla = mi_tupla + (8,'c')

# imprimir la tupla
print(mi_tupla)

#acumular elementos
mi_tupla += (0,'x')

#imprimir
print(mi_tupla)

# subtupla
# el segundo hasta el penultimo
print (mi_tupla[1:-1])

# subtupla con saltos
# los elementos pares
print('los elementos pares', mi_tupla[::2])

# los elementos impares
print('los elementos impares', mi_tupla[1::2])



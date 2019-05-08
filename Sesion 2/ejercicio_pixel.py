#Ejercicio
# Pasar a escala de grises el color codificado en los elementos de la lista `pixel

pixel= [0.6,0.3,0.4]

suma = pixel[0] + pixel[1] + pixel[2]
n = len(pixel)
promedio = suma / n

print('suma=', suma, 'n', 'promedio=', promedio)

# otra solucion
# mediante ciclos
p = 0
for numero in pixel:
    p += numero

p = p / len(pixel)

print('el promedio es=', p)

# tercer solucion

mi_suma = sum(pixel)
mi_promedio = mi_suma / len(pixel)

# 4ta opcion
mi_promedio = sum(pixel) / len(pixel)

#Ejercicio
# Pasar a blanco y negro el valor de intensidad codificado en la variable intensidad

# decidir blanco o negro

if mi_promedio >= 0.5:
    print('el pixel es blanco')
else:
    print('el pixel es negro')

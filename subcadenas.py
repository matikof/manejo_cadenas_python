#Sub cadenas en python
cadena = "Hola, mundo!"


# Obtenemos la subcadena de hola [inicio:fin (sin incluirlo)]
subcadena_hola = cadena[0:4]#
print(f"Subcadena de la cadena original: {subcadena_hola}")


#Obtenemos la subcadena mundo
subcadena_mundo = cadena[6:11]
print(f"Subcadena Mundo: {subcadena_mundo}")


indice_mundo = cadena.find("mundo")
print(f"El indice donde se encontro la palabra mundo es: {indice_mundo}")

#Obtener el indice de la subcadena hola
indice_hola = cadena.find("Hola")
print(f"El indice de la subcadena hola: {indice_hola}")

#Reemplazar una subcadena
cadena = "hola mundo"
nueva_cadena = cadena.replace("mundo","a todos")
print(nueva_cadena)
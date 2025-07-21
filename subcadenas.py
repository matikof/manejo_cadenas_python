#IMPORTANTE
#Una cadena es inmutable así que al usar la mayoría de estos
#Métodos no estamos modificando la cadena original, si no
#mas bien estamos creando una nueva.
#La original no se toca, queda siempre igual!!!!!


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

# Sustituir hola por adios
cadena_nueva_hola = cadena.replace("hola", "Adios")
print(f"Nueva cadena reemplazada: {cadena_nueva_hola}")

#Generador de Email
nombre = " Ubaldo Acosta Soto "
nombre_normalizado = nombre.strip().replace(" ",".").lower()
print(nombre_normalizado)


nombre_empresa = " Global Mentoring "
extension_dominio = " .com.mx "
dominio_email_normalizado = "@" + nombre_empresa.strip().lower().replace(" ", "") + extension_dominio.lower().strip()
print(dominio_email_normalizado)
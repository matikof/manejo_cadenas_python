# Métodos de cadenas

cadena1 = "Hola Mundo"
print(f"Cadena Original: {cadena1}")
#Se genera una nueva cadena, no es que estemos modificando la primera
#Metodo upper para poner todo en mayusculas
mayusculas = cadena1.upper()
print(f"Cadena en mayusculas: {mayusculas}")

#Método lower
print(f"Cadena en minusculas: {cadena1.lower()}")

cadena2 = " Juan Perez "
#.strip() para eliminar espacios tanto al inicio como en el final
print(f"Cadena con espacios: {cadena2}")
print(f"Cadena sin espacios: {cadena2.strip()}")

#Método len() para obtener el largo de algun elemento
saludo = "Hola, mundo!"
largo_cadena = len(saludo)
print(f"Largo de la cadena: {largo_cadena}")


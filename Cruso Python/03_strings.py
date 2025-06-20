nombre_curso = "Cruso Python"
descripcion_curso = """
Curso de python
este curos tiene todos los detalles
para ser programador
"""
#funciones que nos permiten saber la cantidad de caracteres que tiene lo que mostramos en print
print(len(nombre_curso))
#con los cuadrados podemos mostrar el caracter que elijamos, siempre empezando por el 0 sera la primera letra
print(nombre_curso[0])
#con esto cortarmos los caracteres que queramos
print(nombre_curso[0:5])
print(nombre_curso[6:])#si no rellenamos el segundo espacio, coge todo lo demas que queda

#Formatear los strings

nombre = "Alberto"
apellido = "Bello"
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)
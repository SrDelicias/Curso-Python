animal = "perro fliz"
print(animal.upper()) #lo transforma todo a mayusculas
print(animal.lower())  #todo a minuscula
print(animal.capitalize()) #el primer caracter lo transforma a mayuscula
print(animal.title()) #toma la primera letra de cada palabra a mayuscula
print(animal.strip()) #esto elimina cualquier espacio en blanco que haya al principio y al final del string
print(animal.rstrip()) #esto elimina cualquier espacio en blanco que haya en la derecha
print(animal.lstrip()) #esto elimina cualquier espacio en blanco que haya en la izquierda
print(animal.find("fl")) #nos dice en que lugar estan esas letras
print(animal.replace("fl", "pl")) #remplaza caracteres por el que le pongas
print("fl" in animal) #nos dice si esos caracteres estan o no, es un boolean
print("fl" not in animal) #nos dice si esos caracteres estan o no, es un boolean

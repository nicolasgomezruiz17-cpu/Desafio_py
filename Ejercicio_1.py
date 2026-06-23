lista = ["manzana", "pera", "naranja", "plátano", "kiwi", "uva", "piña",
"mango", "sandía", "melón"]

#Imprime el quinto elemento de la lista.

print(lista[5])

#Imprime del cuarto al sexto inclusive

for i in range(3,6):
    print(lista[i])   
    
    
#Elimina el elemento en la posición 3

lista.pop(3)

print(lista)

#Agrega dos nuevos elementos a la lista

lista.append('maracuya')
lista.append('Limon')

print(lista)

#Ordena la lista alfabéticamente

lista.sort()
print(lista)

#Genera un diccionario usando lista1 como llaves y lista como valores

lista1 = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete",
"ocho", "nueve", "diez"]

diccionario = {}
for i in zip(lista, lista1):
    diccionario[i[0]] = i[1]
print(diccionario)
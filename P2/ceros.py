"""
Fecha   :15/04/26
Grupo   :2 i
Nombre  :ruben luquin sanchez


Encontrar que elementos de una lista suman cero

Escribe una clase de python que encuentre 3 elementos que sumen cero
Los elementos se encuentran en una lista y son numeros enteros +-

"""

#Codigo
class Sumacero:
    def encontrar(self, lista):
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                for k in range(j+1, len(lista)):
                    if lista[i]+ lista[j] + lista[k] == 0:
                        return lista[i], [lista], lista[k]
# Ejemplo
numeros =[2,-3, 1, 4,-1]
obj= Sumacero()
resultado = obj.encontrar (numeros)
print("Numeros que suman 0:", resultado)




"""
Resutlado
Numeros que suman 0: (2, [[2, -3, 1, 4, -1]], 1)

"""

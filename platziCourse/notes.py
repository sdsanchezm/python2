=LISTAS
operaciones con listas
append se usa con listas 
las listas son mutables
sirve iterar con indices
pop, eliminar ultimo elemento de la lista
sort
extender la lista (extend)
se puede crear lista, con la funcion lista(parametro) // parametro es una secuencia (un str es una secuencia)
para unirlos, se usa join 
los strings son inmutables
escribiendo una variable en MAYUSCULAS podemos ver que es una constante, por que en python no existen
Empty list:: 
empty_list = []
empty_list = list()

ejemplos de listas: 
http://librosweb.es/libro/python/capitulo_7/metodos_de_agregado.html
https://docs.python.org/3.8/tutorial/datastructures.html

Las listas son Arrays y las tuplas son Arrays. La diferencia: las tuplas son inmutables
Algunos métodos de las listas:
insert(posicion, elemento) --->inserta elemento
append() ----> inserta elemento al final de la lista y puede asignarse a una variable
pop() ----> elimina elemento del final de la lista y puede asignarse a una variable
sort() ----> ordena la lista
del array[index] -----> borra un elemento de la lista por index
index(elemento) ------> busca un elemento y retorna el índice
list()------> si esto se aplica a un string, retorna un array con cada caracter con un indice propio
si a una variable que contiene por ejemplo ['H', 'o', 'l', 'a'] le aplicamos ''.join() da como resultado 'Hola'```
A list look like this: 
my_list = ['a', 'b', 'c']

=Diccionarios
Un diccionaro es un mapa de llaves de valores
los valores pueden ser de varios tipos
se crea con corchetes (curly brackets)
en listas los index son enteros, en las diccionarios son las key
dictionary_one = {}
dictionary_one['key'] = 'value'
values can also be added when created: 
dictionary_one {'key': 'value'}
Cuando se itera un diccionario se obtienen las llaves, aunque tambien se puede iterar con los valores
se pueden tambien obtener las llaves (keys) y valores al mismo tiempo
https://realpython.com/iterate-through-dictionary-python/
Los metodos son: myDict.keys(),  myDict.values(),  myDict.items()
Empty Dict: 
empty_dict = {}
a dictionary looks like this:

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
}

=Tuplas
Secuencias de valores indexada por enteros
similar a las listas pero inmutables
las tuplas se crean separando los valores con comas
se usan parentesis para declararlas
es mutable (se puede re-asignar)
las tuplas, al igual que las listas se acceden a traves de indices 
pueden usarse para retornar mas de un valor en una funcion o se puede crear estructuras de datos ligeras
para hacer tupla de un solo valor, es necesario la coma mi_tupla = (10,) 
Empty tupla: 
empty_tuple = ()
empty_tuple = tuple()
A tuple looks like this: 
my_tumple = ('a', 1)

=Sets 
Son inmutables (no se puede cambiar los valores)
Se declaraon con : Empty Set:  empty_set = set()
Operaciones con sets: 
s = {1,2,3} # s = set([1, 2, 3])
t = {3,4,5} # t = set([3, 4, 5])
print(s | t) # | union                  s.union(t)
print(s & t) # & interseccion           s.intersection(t)
print(s - t) # - diferencia             s.difference(t)
print(s ^ t) # ^ diferencia simetrica   s.symmetric_difference(t)
print(s <= t) # <= subconjunto          s.issubset(t)
print(s >= t) # >= superconjunto        s.issuperset(t)
union: 
 s.union(t)
{1, 2, 3, 4, 5}
interseccion: 
 s.intersection(t)
{3}
diferencia: 
s.difference(t)
{1, 2}
t.fifference(s)
{[4,5]}
uno de los usos, es aber si un elemento se encuentra en un set (si se hace con una lista, no es tan eficiente)
1 not in s: False
2 in t : False
3 in t: True

=list comprehensions o dictionary comprehensions (azucar sintactico)
es mas comprensible y hacer mas legible el codigo
== List comprehension, tomar una secuencia y create una nueva lista
###########
even = []
for num in range(1,31):
    if num % 2 == 0:
        even.append(num)
###########
above code can be written as:
pares = [num for num in range(1,31) if num % 2 == 0]

== Dictionary comprehension, el resultado es un diccionario nuevo
myDict = {}
for num in range(1,21):
    myDict[num] = num**2

Mydict = {num:num**2 for num in range(1,21)}

= Errors in Python:

Estructure: 
try:
	# Código a ejecutar
except:
	# Código para 'cachar' o 'recibir' el error y hacer algo
else:
	# Código cuando el try SÍ sirva y NO se ejecute el except
finally:	
	# Código que SIEMPRE se va a ejecutar, independientemente se ejecute el except o el else

Python tiene una jerarquia de errores


= File handling
python puede leer y esrcribir archivos con la funcion open




=Classes
El nombre de una clase se declara con mayuscula
a class can be defined in a specific independent file 



= Decoradores

es una funcion, que recibe como parametro otra funcion y retorna una funcion
se conoce por que empieza por un arroba
Util para definir si una funcion debe ejecutarse o no (si se cumplen con las condiciones)
Es sintactic suggar




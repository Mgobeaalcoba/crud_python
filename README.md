# Creación de un CRUD: 

```bash
(C)reate
(R)ead or retreive
(U)pdate
(D)elete
```

-----------------------

## Iterators & Generators en Python: 

Aunque no lo sepas, probablemente ya utilices iterators en tu vida diaria como programador de Python. Un iterator es simplemente un objeto que cumple con los requisitos del Iteration Protocol (protocolo de iteración) y por lo tanto puede ser utilizado en ciclos. Por ejemplo,

```python
for i in range(10):
    print(i)
```

En este caso, la función range es un iterable que regresa un nuevo valor en cada ciclo. Para crear un objeto que sea un iterable, y por lo tanto, implemente el protocolo de iteración, debemos hacer tres cosas:

- Crear una clase que implemente los métodos iter y next
- iter debe regresar el objeto sobre el cual se iterará
- next debe regresar el siguiente valor y aventar la excepción StopIteration cuando ya no hayan elementos sobre los cual iterar.

Por su parte, los generators son simplemente una forma rápida de crear iterables sin la necesidad de declarar una clase que implemente el protocolo de iteración. Para crear un generator simplemente declaramos una función y utilizamos el keyword yield en vez de return para regresar el siguiente valor en una iteración. Por ejemplo,

```python
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b
```

Es importante recalcar que una vez que se ha agotado un generator ya no podemos utlizarlo y debemos crear una nueva instancia. Por ejemplo,

```python
fib1 = fibonacci(20)
fib_nums = [num for num in fib1]
...
double_fib_nums = [num * 2 for num in fib1] # no va a funcionar
double_fib_nums = [num * 2 for num in fibonacci(30)] # sí funciona
```

--------------------------------

## Uso de listas en Python: 

Python y todos los lenguajes nos ofrecen constructos mucho más poderosos, haciendo que el desarrollo de nuestro software sea

- Más sofisticado
- Más legible
- Más fácil de implementar
- 
Estos constructos se llaman Estructuras de Datos que nos permiten agrupar de distintas maneras varios valores y elementos para poderlos manipular con mayor facilidad.

Las listas las vas a utilizar durante toda tu carrera dentro de la programación e ingeniería de Software.

Las listas son una secuencia de valores. A diferencia de los strings, las listas pueden tener cualquier tipo de valor. También, a diferencia de los strings, son mutables, podemos agregar y eliminar elementos.

En Python, las listas son referenciales. Una lista no guarda en memoria los objetos, sólo guarda la referencia hacia donde viven los objetos en memoria

Se inician con [] o con la built-in function list.

### Operaciones con listas: 

Ahora que ya entiendes cómo funcionan las listas, podemos ver qué tipo de operaciones y métodos podemos utilizar para modificarlas, manipularlas y realizar diferentes tipos de cómputos con esta Estructura de Datos.

- El operador +(suma) concatena dos o más listas.
- El operador *(multiplicación) repite los elementos de la misma lista tantas veces los queramos multiplicar

Sólo podemos utilizar +(suma) y *(multiplicación).

Las listas tienen varios métodos que podemos utilizar.

- **append** nos permite añadir elementos a listas. Cambia el tamaño de la lista.
- **pop** nos permite sacar el último elemento de la lista. También recibe un índice y esto nos permite elegir qué elemento queremos eliminar.
- **sort** modifica la propia lista y ordenarla de mayor a menor. Existe otro método llamado sorted, que también ordena la lista, pero genera una nueva instancia de la lista
- **del** nos permite eliminar elementos vía indices, funciona con slices
- **remove** nos permite es pasarle un valor para que Python compare internamente los valores y determina cuál de ellos hace match o son iguales para eliminarlos.

-------------------------------------------

## Diccionarios:

Los diccionarios se conocen con diferentes nombres a lo largo de los lenguajes de programación como HashMaps, Mapas, Objetos, etc. En Python se conocen como Diccionarios.

Un diccionario es similar a una lista sabiendo que podemos acceder a través de un indice, pero en el caso de las listas este índice debe ser un número entero. Con los diccionarios puede ser cualquier objeto, normalmente los verán con strings para ser más explicitos, pero funcionan con muchos tipos de llaves…

Un diccionario es una asociación entre llaves(keys) y valores(values) y la referencia en Python es muy precisa. Si abres un diccionario verás muchas palabras y cada palabra tiene su definición.

Para iniciar un diccionario se usa {} o con la función dict

Estos también tienen varios métodos. Siempre puedes usar la función dir para saber todos los métodos que puedes usar con un objeto.

Si queremos ciclar a lo largo de un diccionario tenemos las opciones:

- keys: nos imprime una lista de las llaves
- values nos imprime una lista de los valores
- items. nos manda una lista de tuplas de los valores

------------------------------

## Tuples & Sets:

Tuplas(tuples) son iguales a las listas, la única diferencia es que son inmutables, la diferencia con los strings es que pueden recibir muchos tipos valores. Son una serie de valores separados por comas, casi siempre se le agregan paréntesis para que sea mucho más legible.

Para poderla inicializar utilizamos la función tuple.

Uno de sus usos muy comunes es cuando queremos regresar más de un valor en nuestra función.

Una de las características de las Estructuras de Datos es que cada una de ellas nos sirve para algo especifico. No existe en programación una navaja suiza que nos sirva para todos. Los mejores programas son aquellos que utilizan la herramienta correcta para el trabajo correcto.

Conjutos(sets) nacen de la teoría de conjuntos. Son una de las Estructuras más importantes y se parecen a las listas, podemos añadir varios elementos al conjunto, pero no pueden existir elementos duplicados. A diferencia de los tuples podemos agregar y eliminar, son mutables.

Los sets se pueden inicializar con la función set. Una recomendación es inicializarlos con esta función para no causar confusión con los diccionarios.

- add nos sirve añadir elementos.
- remove nos permite eliminar elementos.

Con los sets, podemos hacer operaciones de conjuntos como hacemos con SQL y los joins. Por ejemplo:

```python
a = set([1,2,3])
b = {3,4,5}

# Operaciones de conjuntos:
a.intersection(b)
# {3}

a.union(b)
# {1,2,3,4,5}

a.difference(b) # Todos los elementos de a que no están en b
# {1,2}

b.difference(a) # Todos los elementos de b que no están en a
# {4,5}
```

-------------------------------------

## Modulo Collections: Nos permite traernos las clases de los objetos primitivos para extender sus funciones...

El módulo collections nos brinda un conjunto de objetos primitivos que nos permiten extender el comportamiento de las built-in collections que poseé Python y nos otorga estructuras de datos adicionales. Por ejemplo, si queremos extender el comportamiento de un diccionario, podemos extender la clase UserDict; para el caso de una lista, extendemos UserList; y para el caso de strings, utilizamos UserString.

Por ejemplo, si queremos tener el comportamiento de un diccionario podemos escribir el siguiente código:

```python
class SecretDict(collections.UserDict):

   def _password_is_valid(self, password):
        …

    def _get_item(self, key):
        … 

    def __getitem__(self, key):
         password, key = key.split(‘:’)
         
         if self._password_is_valid(password):
              return self._get_item(key)
         
         return None

my_secret_dict = SecretDict(...)
my_secret_dict[‘some_password:some_key’] # si el password es válido, regresa el valor
```

Otra estructura de datos que vale la pena analizar, es namedtuple. Hasta ahora, has utilizado tuples que permiten acceder a sus valores a través de índices. Sin embargo, en ocasiones es importante poder nombrar elementos (en vez de utilizar posiciones) para acceder a valores y no queremos crear una clase ya que únicamente necesitamos un contenedor de valores y no comportamiento.

```python
Coffee = collections.NamedTuple(‘Coffee’, (‘size’, ‘bean’, ‘price’))
def get_coffee(coffee_type):
     If coffee_type == ‘houseblend’:
         return Coffee(‘large’, ‘premium’, 10)
```

El módulo collections también nos ofrece otros primitivos que tienen la labor de facilitarnos la creación y manipulación de colecciones en Python. Por ejemplo, Counter nos permite contar de manera eficiente ocurrencias en cualquier iterable; OrderedDict nos permite crear diccionarios que poseen un orden explícito; deque nos permite crear filas (para pilas podemos utilizar la lista).

En conclusión, el módulo collections es una gran fuente de utilerías que nos permiten escribir código más “pythonico” y más eficiente.

---------------------------------

## Comprehensions:

Las Comprehensions son constructos que nos permiten generar una secuencia a partir de otra secuencia.

Existen tres tipos de comprehensions:

- List comprehensions

```python
[element for element in element_list if element_meets_condition]
```

- Dictionaty comprehensions

```python
{key: element for element in element_list if element_meets_condition}
```

- Sets comprehensions

```python
{element for element in element_list if elements_meets_condition}
```

-----------------------------------

## Busqueda binaria:

Uno de los conceptos más importantes que debes entender en tu carrera dentro de la programación son los algoritmos. No son más que una secuencia de instrucciones para resolver un problema específico.

Búsqueda binaria lo único que hace es tratar de encontrar un resultado en una lista ordenada de tal manera que podamos razonar. Si tenemos un elemento mayor que otro, podemos simplemente usar la mitad de la lista cada vez.

Ver algoritmo para tales fines en busqueda_binaria.py

----------------------------------

## Manipulación de archivos

En realidad, cuando armamos un CRUD debemos guardar nuestros datos en un archivo o en una base de datos para luego poder retomarlo al reiniciar nuestro programa. 

Manipulación de archivos en Python:

- funcion open() nos permite leer archivos

```python
f = open('some_file')
```

- siempre debemos cerrar el archivo con la función close() luego de utilizarlo. Esto es para no desperdiciar memoria de nuestra CPU

```python
f.close()
```

- Una mejor manera de manipular archivos es utilizando "context managers", porque garantizan que el archivo se cierre. Ej:

```python
with open("filename.ext") as f:
    # Do something with the file
```

- Existen varios modos de abrir un archivo. Los mas importantes son r (read) y w (write):

```python
with open("filename.ext", mode = 'w') as f:
    # do something with the file
```

- El módulo "CSV" nos permite manipular archivos con terminación .csv

- Para utilizarlo lo importamos con la siguiente declaración:

```python
import csv
```

- Existes dos readers y dos writers
    A- csv.reader y csv.writer nos permiten manipular los valores a través de listas que representan filas. Solo se puede acceder por indice a los valores
    B- csv.DictReader y csv.DictWriter nos permiten manipular los valores a traves de diccionarios que representan filas. Se puede acceder a traves de llaves a los valores. 





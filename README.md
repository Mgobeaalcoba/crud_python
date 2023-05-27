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

-------------------------------

## Decoradores: 

Python es un lenguaje que acepta diversos paradigmas como programación orientada a objetos y la programación funcional, siendo estos los temas de nuestro siguiente módulo.

Los decoradores son una función que envuelve a otra función para modificar o extender su comportamiento.

Los decoradores envuelven a otra función y permiten ejecutar código antes y después de que es llamada. 

En Python las funciones son ciudadanos de primera clase, first class citizen, esto significan que las funciones pueden recibir funciones como parámetros y pueden regresar funciones. Los decoradores utilizan este concepto de manera fundamental.

Ej:

```python
def lower_case(func):
    def wrapper():
        # execute code before
        result = func()
        # execute code after
        return result
    return wrapper
```

---------------------------------

## Programación Orientada a Objetos (POO):

La programación orientada a objetos es un paradigma de programación que otorga los medios para estructurar programas de tal manera que las propiedades y comportamientos estén envueltos en objetos individuales.

Para poder entender cómo modelar estos objetos tenemos que tener claros cuatro principios:

- Encapsulamiento. / Encapsulation
- Abstracción. / Abstraction
- Herencia. / Inheritance
- Polimorfismo. / Polyphormism

Las clases simplemente nos sirven como un molde para poder generar diferentes instancias.

- **Encapsulation**: Cada objeto tiene sus propias funciones, y datos sin afectar a otros, son lógica interna.

- **Abstraction**: El usuario podrá interactuar con el objeto sin necesidad de conocer toda la lógica del mismo.

- **Inheritance**: si se declara un método en una clase todas las subclases heredan ese método, es decir: si tu declaras un método “imprime” que ejecute un print en una clase, las subclases podrán usar el método imprime, sin necesidad de declararlo en cada una.

- **Polyphormism**: usando el ejemplo anterior, en cada subclase se puede modificar el método “imprime” por lo tal cada sub clase contara con un método imprime pero acorde a las necesidades de cada subclase.

### Clases en Python:

Para declarar una clase en Python utilizamos la keyword class, después de eso le damos el nombre. Una convención en Python es que todas las clases empiecen con mayúscula y se continua con CamelCase.

- Un método fundamental es dunder init(__init__). Lo único que hace es inicializar la clase basado en los parámetros que le damos al momento de construir la clase.

- self es una referencia a la clase. Es una forma internamente para que podamos acceder a las propiedades y métodos.

Ejemplo:

- Declarar una clase:

```python
class Airplane:
    def __init__(self, passengers, seats, pilots=[]):
        self.passengers = passengers
        self.seats = seats
        # El "_" antes de un atributo o método 
        # significa que el mismo es privado. 
        # Es decir, no puede (en python no debe en realidad) ser accedido desde fuera de
        # la clase.
        self._pilots = pilots

    def takeoff(self):
        pass
```

- Inicializar un clase y usar sus métodos y atributos: 

```python
airplane1 = Airplane(passengers=20, seats=30, pilots=['Tom', 'Billy'])
# doc notation: se usa para acceder a atributos y metodos de una clase:
# Modifico un atributo de mi objeto:
airplane1.passengers = 31
# Uso un método de mi objeto:
airplane1.takeoff()
```

-----------------------------------

## Scopes and namespaces

En Python, un name, también conocido como identifier, es simplemente una forma de otorgarle un nombre a un objeto. Mediante el nombre, podemos acceder al objeto. Vamos a ver un ejemplo:

```python
my_var = 5

id(my_var) # 4561204416
id(5) # 4561204416
```

En este caso, el identifier my_var es simplemente una forma de acceder a un objeto en memoria (en este caso el espacio identificado por el número 4561204416). Es importante recordar que un name puede referirse a cualquier tipo de objeto (aún las funciones).

```python
def echo(value):
    return value

a = echo

a(‘Billy’) # 3
```

Ahora que ya entendimos qué es un name podemos avanzar a los namespaces (espacios de nombres). Para ponerlo en palabras llanas, un namespace es simplemente un conjunto de names.

En Python, te puedes imaginar que existe una relación que liga a los nombres definidos con sus respectivos objetos (como un diccionario). Pueden coexistir varios namespaces en un momento dado, pero se encuentran completamente aislados. Por ejemplo, existe un namespace específico que agrupa todas las variables globales (por eso puedes utilizar varias funciones sin tener que importar los módulos correspondientes) y cada vez que declaramos una módulo o una función, dicho módulo o función tiene asignado otro namespace.

A pesar de existir una multiplicidad de namespaces, no siempre tenemos acceso a todos ellos desde un punto específico en nuestro programa. Es aquí donde el concepto de scope (campo de aplicación) entra en juego.

Scope es la parte del programa en el que podemos tener acceso a un namespace sin necesidad de prefijos.

En cualquier momento determinado, el programa tiene acceso a tres scopes:

El scope dentro de una función (que tiene nombres locales)
El scope del módulo (que tiene nombres globales)
El scope raíz (que tiene los built-in names)
Cuando se solicita un objeto, Python busca primero el nombre en el scope local, luego en el global, y por último, en el raíz. Cuando anidamos una función dentro de otra función, su scope también queda anidado dentro del scope de la función padre.

```python
def outer_function(some_local_name):
    def inner_function(other_local_name):
         # Tiene acceso a la built-in function print y al nombre local some_local_name
         print(some_local_name) 
        
         # También tiene acceso a su scope local
         print(other_local_name)
```

Para poder manipular una variable que se encuentra fuera del scope local podemos utilizar los keywords global y nonlocal.

```python
some_var_in_other_scope = 10

def some_function():
     global some_var_in_other_scope
     
     Some_var_in_other_scope += 1
```

------------------------------

## Framework Click:

Click es un pequeño framework que nos permite crear aplicaciones de Línea de comandos. Tiene cuatro decoradores básicos:

- @click_group: Agrupa una serie de comandos
- @click_command: Aca definiremos todos los comandos de nuestra apliacion
- @click_argument: Son parámetros necesarios
- @click_option: Son parámetros opcionales

Click nos otorga una interfaz que podemos personalizar. También autogenera ayuda para el usuario.

Click también realiza las conversiones de tipo por nosotros. Esta basado muy fuerte en decoradores.

Tutorial en Youtube sobre Click: https://www.youtube.com/watch?v=riQd3HNbaDk

------------------------------------------------

Podrán ver como usar click para hacer un programa de linea de comandos en el modulo de este proyecto llamado "gobea-ventas".

También están en los archivos los pasos para instalarlo y ejecutarlo desde la terminal.

--------------------------------------------

## Estructura de un proyecto en Python: (Arquitectura):

Division (estructura) de nuestro programa:
<br>
👀👀👀Interface --------------> Comandos
👾👾👾Logica ---------------> Servicios
🙋🙋🙋ObjetosInteractivos --> Clientes

------------------------------------------

## Manejo y Jerarquia de errores en Python:

Python tiene una amplia jerarquía de errores que nos da posibilidades para definir errores en casos como donde no se pueda leer un archivo, dividir entre cero o si existen problemas en general en nuestro código Python. El problema con esto es que nuestro programa termina, es diferente a los errores de sintaxis donde nuestro programa nunca inicia.

Para ““aventar”” un error en Python utilizamos la palabra raise. Aunque Python nos ofrece muchos errores es buena práctica definir errores específicos de nuestra aplicación y usar los de Python para extenderlos.

Podemos generar nuestros propios errores creando una clase que extienda de BaseException.

Si queremos evitar que termine nuestro programa cuando ocurra un error, debemos tener una estrategia. Debemos utilizar try / except cuando tenemos la posibilidad de que un pedazo de nuestro código falle

- try: significa que se ejecuta este código. Si es posible, solo ponemos una sola línea de código ahí como buena práctica
- except: es nuestro manejo del error, es lo que haremos si ocurre el error. Debemos ser específicos con el tipo de error que vamos a atrapar.
- else: Es código que se ejecuta cuando no ocurre ningún error.
- finally: Nos permite obtener un bloque de código que se va a ejecutar sin importar lo que pase.

Jerarquia de clases para las built-in Exceptions:

```bash
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

------------------------------------------

## Context Managers:

Los context managers son objetos de Python que proveen información contextual adicional al bloque de código. Esta información consiste en correr una función (o cualquier callable) cuando se inicia el contexto con el keyword with; al igual que correr otra función cuando el código dentro del bloque with concluye. Por ejemplo:

```python
with open(‘some_file.txt’) as f:
    lines = f.readlines()
```

Si estás familiarizado con este patrón, sabes que llamar la función open de esta manera, garantiza que el archivo se cierre con posterioridad. Esto disminuye la cantidad de información que el programador debe manejar directamente y facilita la lectura del código.

Existen dos formas de implementar un context manager: con una clase o con un generador. Vamos a implementar la funcionalidad anterior para ilustrar el punto:

```python
class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

with CustomOpen('file') as f:
    contents = f.read()
```

Esta es simplemente una clase de Python con dos métodos adicionales: enter y exit. Estos métodos son utilizados por el keyword with para determinar las acciones de inicialización, entrada y salida del contexto.

El mismo código puede implementarse utilizando el módulo contextlib que forma parte de la librería estándar de Python.

```python
from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

with custom_open('file') as f:
    contents = f.read()
```

El código anterior funciona exactamente igual que cuando lo escribimos con una clase. La diferencia es que el código se ejecuta al inicializarse el contexto y retorna el control cuando el keyword yield regresa un valor. Una vez que termina el bloque with, el context manager toma de nueva cuenta el control y ejecuta el código de limpieza.

Mas sobre context manager acá: http://book.pythontips.com/en/latest/context_managers.html

------------------------------------

# Algunos de los usos de Python en el "mundo real":

Python tiene muchas aplicaciones:

En las ciencias tiene muchas librerías que puedes utilizar como analisis de las estrellas y astrofisica; si te interesa la medicina puedes utilizar Tomopy para analizar tomografías. También están las librerías más fuertes para la ciencia de datos numpy, Pandas y Matplotlib

En CLI por si te gusta trabajar en la nube y con datacenters, para sincronizar miles de computadoras:

- aws
- gcloud
- rebound
- geeknote

Aplicaciones Web:

- Django
- Flask
- Bottle
- Chalice
- Webapp2
- Gunicorn
- Tornado


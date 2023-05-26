from person_class import Person

def run():

    # No se usa el Keyword "new" en Python...
    mariano = Person("Mariano", 35)

    mariano.say_hello()

if __name__ == '__main__':
    run()
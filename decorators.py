PASSWORD = '12345'

def password_required(func):
    # wrapper es el nombre común de las funciones internas en decorators:
    def wrapper():
        password = input('Cual es tu contraseña? ')

        if password == PASSWORD:
            return func()
        else:
            print('La contraseña no es correcta.')

    # El utlimo paso de un decorador es return la función wrapper o interna:
    return wrapper
    
# Para usar un decorador debemos declararlos como anotaciones arriba de una funcion:
@password_required
def needs_password():
    print('La contraseña es correcta')

# Declaro un decorador que vuelva a mayusculas todo mi nombre:
def upper(func):
    # Con *args y **kwargs nos ahorramos el problema de determinar los parametros que vamos a recibir
    # de antemano: 
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()
    
    return wrapper

@upper
def say_my_name(name):
    # Debemos retornar algo explicitamente para poder aplicar el metodo upper() de str en el decorador.
    return f'Hola, {name}.'


def run():
    print(say_my_name('Mariano'))

    # Ejecuto la función decorada...
    # needs_password()
    # Que debería ser lo mismo qued ejecutarla así:
    # password_required(needs_password) # no funciona así


if __name__ == '__main__':
    run()
# Abstracciones u objetos sobre los que estamos interactuando. 

# Modulo uuid de Python nos permite generar Id únicas:
import uuid

class Client:

    def __init__(self, name, company, email, position, uid=None) -> None:
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4() # Standar en la industria para generar id´s en general

    # Convertimos el objeto a diccionario para poder agregarlo a disco en el csv donde estamos guardando los datos:
    def to_dict(self):
        # vars retorna nuestro objeto como diccionario:
        return vars(self)
    
    @staticmethod # Metodo estático: Método que se puede ejecutar sin necesidad de una instancia de clase.
    def schema(): # No recibe el keyword "self" porque no necesita una instancia para funcionar.
        return ['name', 'company', 'email', 'position', 'uid']


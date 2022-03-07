
'''

Clases 

'''
class Usuario:
    Nombre = 'Felipe'
    Apellido = 'Feliz'

usuario = Usuario()
# print(usuario) # mostrara la instancia de clase usuario
# print(usuario.Nombre, usuario.Apellido)

# Para poder prevenir que en una clase los objetos puedan ser los mismos 
# Y al ser iguales que estos seran dos clases completamente distintos

class User:
    def __init__(self, userName, Password):
        self.userName = userName
        self.Password = Password

user = User ('Felipe', 'Feliz') 
user2 = User ('Chanchito', 'Feliz')

# print(user.userName, user.Password, user2.userName, user2.Password)

'''

Metodos

'''

class SurnName:
    def __init__(self, Name, LastName):
        self.Name = Name
        self.LastName = LastName

    def Saludo(self):
         print('Hola soy ', self.Name,self.LastName)

surnName = SurnName('Felipe', 'Feliz')

# surnName.Saludo()
# surnName.Name = 'Chanchito' # Para poder cambiar las propiedas de las instancias 
# surnName.Saludo()

# del surnName.Name # Para poder eliminar una instancia 
# del surnName # Para eliminar completamente la class
# print(surnName)

'''

Herencia

'''

class Admin(SurnName):
    def superSaludo(self):
        print('Hola!, Me llamo', self.Name, ' y soy administrador')

admin = Admin('Super', 'Feliz')
# admin.Saludo()
# admin.superSaludo()

''' 

Ejercicio de Herencia

'''
# Para hacer individualmete una herencia

class Gato:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola!, mi nombre es',self.nombre,'y mi sonido es', self.onomatopeya)

gato = Gato('Fluffy', 'Maullido')


class Perro:
    def __init__(self,nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola!, mi nombre es', self.nombre, 'y mi sonido es', self.onomatopeya)
 
perro = Perro ('Firulais', 'Ladrido')

# gato.saludo()
# perro.saludo()

# Para poder agrupar una herencia 


class Animal:
    def __init__(self,nombre,onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el ', self.onomatopeya)

class Felino(Animal):
    tipo = 'Felino'
    def __init__(self,nombre,onomatopeya): # Para extender un metodo de __init__ de padre
        Animal.__init__(self,nombre,onomatopeya)
        print('Hola soy un gato extendido') 

class Lobo(Animal):
    tipo = 'Lobo'
    def __init__(self,nombre,onomatopeya): # Otra manera de extender un metodo de __init__ de padre
        super().__init__(nombre,onomatopeya)
        print('instanciando un perro')

felino = Felino('Fluffy', 'Maullido')
felino.saludo()

lobo = Lobo('Firulais', 'Ladrido')
lobo.saludo()

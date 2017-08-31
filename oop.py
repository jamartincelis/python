print "- " * 20
print "- " * 2 + "Definicion de una clase"
print "- " * 20

class MiClase: # Definicion de una clase
	def MiMetodo(self): # Definicion de un metodo ('self' representa un objeto)
		self.MiPropiedad = "Mi Dato" # Definicion de una propiedad de objeto
		
MiObjeto = MiClase() # Instanciacion de una clase
MiObjeto.MiMetodo() # Ejecucion de un metodo
print MiObjeto.MiPropiedad # Obtencion de la propiedad de un objeto

print
print "- " * 10
print "- " * 2 + "Propiedad de objeto y de clase"
print "- " * 10

class OtraClase:
	PropiedadClase = 0
	def __init__(self, n): # Metodo constructor de la clase
		self.PropiedadObjeto = n
		
Objeto1 = OtraClase(1) # Instancia 1: Inicializa la propiedad de Objeto1
Objeto2 = OtraClase(2) # Instancia 2: Inicializa la propiedad de Objeto2
print Objeto1.PropiedadClase # Imprime: 0
print Objeto1.PropiedadObjeto # Imprime: 1
print Objeto2.PropiedadClase # Imprime: 0
print Objeto2.PropiedadObjeto # Imprime: 2
OtraClase.PropiedadClase = 3 # Modifica la propiedad de la clase
print Objeto1.PropiedadClase # Imprime: 3
print Objeto2.PropiedadClase # Imprime: 3

print
print "- " * 10
print "- " * 2 + "Metodos. Constructor y Destructor"
print "- " * 10

class Persona:
	def __init__(self, nombre):
		self.nombre = nombre
	def saludar(self):
		print "Hola, mi nombre es", self.nombre
	def __del__(self):
		print "%s dice adios." % self.nombre

carlos = Persona("Carlos Zayas")
carlos.saludar()

print
print "- " * 10
print "- " * 2 + "Getters and Setters"
print "- " * 10

class Persona(object):
	def __init__(self, nombre):
		self.setNombre(nombre)
		
	def getNombre(self):
		return ' '.join(self.__nombre)
		
 	def setNombre(self, nombre):
 		self.__nombre = nombre.split()
 		
 	nombre = property(getNombre, setNombre)

carlos = Persona("Carlos Zayas")
print carlos.nombre.upper()

print
print "- " * 10
print "- " * 2 + "Herencia"
print "- " * 10

class Empleado(Persona):
	def __init__(self, nombre, cargo):
		Persona.__init__(self, nombre)
		self.cargo = cargo
		print "%s es %s" % (self.nombre, self.cargo)

empleado = Empleado("Carlos Zayas","Especialista")

print
print "- " * 10
print "- " * 2 + "Herencia Multiple"
print "- " * 10

class animal(object): pass
class perro(animal): pass
fido = perro()
print fido.__class__ is animal
print fido.__class__ is perro
print isinstance(fido, animal)
print isinstance(fido, perro)
#orden de resolucion de metodos
print animal.__mro__
print perro.__mro__

print
print "- " * 10
print "- " * 2 + "Polimorfismo"
print "- " * 10

class Animal:
	cantidad = 0
	def __init__(self):
		print "Hola, soy un animal."
		self.nombre = ""
		Animal.cantidad += 1
		print "Hay", Animal.cantidad, "animales."
		
 	def sonido(self):
 		print "Este es mi sonido:"
 		
 	def __del__(self):
 		print self.nombre, "dice: Adios!"
 		
class Perro(Animal):
	def __init__(self, nombre):
		Animal.__init__(self)
		print "Soy un perro."
		self.nombre = nombre
		print "Me llamo", self.nombre
 
	def sonido(self):
		Animal.sonido(self)
		print "Guau!"

class Gato(Animal):
	def __init__(self, nombre):
		Animal.__init__(self)
		print "Soy un gato."
		self.nombre = nombre
		print "Me llamo", self.nombre
 
	def sonido(self):
		Animal.sonido(self)
		print "Miau!"
		
fido = Perro("Fido")
fido.sonido()
tom = Gato("Tom")
tom.sonido()		
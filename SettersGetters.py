class Fecha():
	"""Si la primera linea del cuerpo se trata de una cadena de texto, esta sera la 
		cadena de documentacion de la clase o docstring
	"""	
	def __init__(self):
		self.__dia = 1
	def getDia(self):
		return self.__dia
	def setDia(self, dia):
		if dia > 0 and dia < 31:
			self.__dia = dia
			return
		print "Error"
mi_fecha = Fecha()
mi_fecha.setDia(33)

class Fecha1(object):
	"""Clase de nuevo estilo extienden de object"""	
	def __init__(self):
		self.__dia = 1
	def getDia(self):
		return self.__dia
	def setDia(self,dia):
		if dia > 0 and dia < 31:
			self.__dia = dia
			return
		print "Error"
	
	dia = property(getDia,setDia)
	
fecha = Fecha1()
fecha.dia = 33
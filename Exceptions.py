try:
	num = int("3a")
	print "no existe"
except NameError:
	print "La variable no existe"
except ValueError:
	print "El valor no es un numero"


try:
	num = int("3a")
	print no_existe
except (NameError, ValueError):
	print "Ocurrio un error"

try:
	num = 33
except:
	print "Hubo un error!"
else:
	print "Todo esta bien"

try:
	z = x / y
except ZeroDivisionError:
	print "Division por cero"
finally:
	print "Limpiando"

class MiError(Exception):
	def __init__(self, valor):
		self.valor = valor
	def __str__(self):
		return "Error " + str(self.valor)

try:
	resultado = 21
	if resultado > 20:
		raise MiError(33)
except MiError, e:
	print e
def saludar(lang):
	def saludar_es():
		print "Hola"
	def saludar_en():
		print "Hi"
	def saludar_fr():
		print "Salut"
		
	lang_func = {"es": saludar_es,
				"en": saludar_en,
				"fr": saludar_fr}
	return lang_func[lang]

f = saludar("fr")
f()
#equivalente
saludar("fr")()

#map
l = [1,2,3]
def cuadrado(n):
	return n ** 2
l2 = map(cuadrado,l)
print l2

#filter
def es_par(n):
	return (n % 2 == 0)
l2 = filter(es_par,l)
print l2

#reduce
def sumar(x,y):
	return x + y
l2 = reduce(sumar,l)
print l2

#lambda
#el ejemplo de filter podria haberse expresado asi
l2 = filter(lambda n: n % 2 == 0, l)
print l2

#list comprehensions, tomada de lenguaje funcional Haskell
#sustituira map y fliter
l2 = [n ** 2 for n in l]
print l2 
l2 = [n for n in l if n % 2.0 == 0]
print l2

#comprension de listas varias clausulas for
l = [0, 1, 2, 3]
m = ["a", "b"]
n = [s * v	for s in m
			for v in l
				if v > 0]
print n

#equivalente de lo anterior
l = [0, 1, 2, 3]
m = ["a", "b"]
n = []
for s in m:
	for v in l:
		if v > 0:
			n.append(s* v)
print n

#generadores
#no se devuelve una lista, sino un generador
l2 = (n ** 2 for n in l)
print l2

def mi_generador(n, m, s):
	while(n <= m):
		yield n
		n += s

for n in mi_generador(0, 5, 1):
	print n

#Decoradores
def mi_decorador(funcion):
	def nueva(*args):
		print "Llamada a la funcion ", funcion.__name__
		retorno = funcion(*args)
		return retorno
	return nueva

@mi_decorador
def imp(s):
	print s

imp("Hola")
	









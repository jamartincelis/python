print "Hola\n\n\tmundo"
for i in range(3):
	print i,	
print "\n"
for i in range(3):
	print i

print "Hola" + "mundo"
print "Hola" , "mundo" #introduce un espacio en blanco
print "Cuesta", 3, "euros"
#print "Cuesta"+ 3 + "euros" #error, para concatenar tienen que ser del mismo tipo

print "Hola %s" % "mundo"
print "%s %s" % ("Hola", "mundo")
print "%10s mundo" % "Hola"
print "%-10s mundo" % "Hola"
print "%.4f" % 3.1422344
print "%.4s" % "hola mundo"
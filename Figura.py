class Figura:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    descripcion = "Esta es una figura"
    author = "Javier Martin"
    def area(self):
        return self.x * self.y
    def perimetro(self):
        return 2 * self.x + 2 * self.y
    def descripcion(self,text):
        self.descripcion = text
    def autorNombre(self,text):
        self.author = text
    def getAutorNombre(self):
    	return self.author
    def escalaTamano(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale



rectangulo = Figura(100,45)
print rectangulo.area()
print rectangulo.perimetro()
print rectangulo.autorNombre("Pedro")
print rectangulo.getAutorNombre()
print rectangulo.escalaTamano(0.5)
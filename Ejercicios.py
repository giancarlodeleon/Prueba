class Persona:
  def __init__(self,nombre,apellido,edad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad= edad
  def mostrar(self):
    print(f'Persona: {self.nombre} Apellido: {self.apellido} Edad: {self.edad}')

persona1 = Persona ('Pedro','Ramirez','25')
persona1.mostrar()

class Operaciones:
  def __init__(self,valor1,valor2):
    self.valor1=valor1
    self.valor2=valor2  

  def sumar(self):
    return self.valor1+self.valor2

  def restar(self):
    return self.valor1-self.valor2 

  def multiplicar(self):
    return self.valor1*self.valor2

  def dividir(self):
    return self.valor1/self.valor2

op=Operaciones(5,3)    
print (op.sumar())
print (op.restar())
print (op.multiplicar())
print (op.dividir())
print (f'{op.dividir():.2f}')

class Volumen:
  def __init__(self,ancho,alto,prof):
    self.ancho=ancho
    self.alto=alto
    self.prof=prof

  def volumen(self):
    return self.ancho*self.alto*self.prof

ancho=int(input("Ingrese el ancho:"))    
alto=int(input("Ingrese el alto:"))  
prof=int(input("Ingrese la profundidad:"))  

cubo=Volumen(ancho, alto, prof)
print(cubo.volumen())
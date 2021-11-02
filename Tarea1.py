class Pila:
    def __init__(self):
        self.Pila = []

    def Add(self,x):
        self.Pila.append(x) 

    def remove(self):
        var=len(self.Pila)
        if var==0:
            print("No se puede, esta vacia")
        else:
            self.Pila.pop()  

    def __str__(self):
	    return str(self.Pila)	

class Cola:
    def __init__(self):
        self.Cola = []
        self.Initial=None
        self.Final=None

    def Add(self,y):
        self.Cola.append(y) 
        
    def remove(self):
        var=len(self.Cola)
        if var==0:
            print("No se puede, esta vacia")
        else:
            self.Cola.pop(0)  
      
    def __str__(self):
	    return str(self.Cola)	

MiCola=Cola()
MiPila= Pila() 

act=False
while act==False:
    print("Elija una opción:\n 1) Pila\n 2) Cola\n 3) Salir")
    res=input("Opción: ")
    if(res=="1"):
        print("Elija una opción:\n 1) Push pila\n 2) Pop fila")
        op1=input("Opción: ")
        act2=False
        while act2==False:
            if(op1=="1"):
                MiPila.Add(input("ingrese un dato: "))  
                print(MiPila,"\n")
                act2=True
            elif(op1=="2"):
                MiPila.remove() 
                print(MiPila,"\n")
                act2=True
            else:
                print("No se ingresó una opción válida, reintentelo")   
                print("Elija una opción:\n 1) Push pila\n 2) Pop fila")  
                op1=input("Opción: ")

    elif(res=="2"):
        print("Elija una opción:\n 1) Push cola\n 2) Pop cola")
        op2=input("Opción: ")
        act3=False
        while act3==False:
            if(op2=="1"):
                MiCola.Add(input("ingrese un dato: "))  
                print(MiCola,"\n")
                act3=True
            elif(op2=="2"):
                MiCola.remove() 
                print(MiCola,"\n")
                act3=True
            else:
                print("No se ingresó una opción válida, reintentelo")   
                print("Elija una opción:\n 1) Push cola\n 2) Pop cola")  
                op2=input("Opción: ")
    elif(res=="3"):
         act=True   
    else:
        print("No se ingresó una opción válida, reintentelo")     
print("Fin del Programa")
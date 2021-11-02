class Pilita:
    def __init__(self):
        self.Pilita = []

    def Add(self,num):
        return self.Pilita.append(num)   

    def remover(self):
	    return self.Pilita.pop()	

    def __str__(self):
	    return str(self.Pilita)

MiPila= Pilita()

MiPila.Add(input())  
MiPila.Add(input())   
MiPila.Add(input())   
MiPila.Add(input())     
print(MiPila)

MiPila.remover()
print(MiPila)

MiPila.remover()
print(MiPila)


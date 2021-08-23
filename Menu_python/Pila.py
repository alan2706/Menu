class Pila:
    def __init__(self,tamanio):
       self.lista=[]
       self.size=tamanio
       self.top=0

    def push (self,Dato):
        if self.top < self.size:
            self.lista += [Dato]
            self.top += 1
        else:
            print('Lista esta llena')

    def pop (self):
        if self.empty():
           return None
        else:
            top = self.lista[-1]
            self.lista = self.lista[:-1]
            self.top -= 1
            return top

    def show (self):
        for top in range(self.top-1,-1,-1):
            print("[{}]".format(self.lista[top]))

    def longitud(self):
        return self.top 

    def empty (self):
        if self.top == 0:
            return True
        else:
            return False


pila1=Pila(3)
pila1.push(6)
pila1.push(8)
pila1.push(5)

pila1.show()
print(pila1.longitud())
# Dato = pila1.pop()
# if Dato: print('el dato eliminado es: {}'.format(Dato))
# else: print('La lista esta vacia')
# Dato = pila1.pop()
# if Dato: print('el dato eliminado es: {}'.format(Dato))
# else: print('La lista esta vacia')
# Dato = pila1.pop()
# if Dato: print('el dato eliminado es: {}'.format(Dato))
# else: print('La lista esta vacia')
# Dato = pila1.pop()
# if Dato: print('el dato eliminado es: {}'.format(Dato))
# else: print('La lista esta vacia')
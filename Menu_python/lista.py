class Lista:
    def __init__(self,tamanio=3):
        self.lista = []
        self.longitud = 0
        self.size = tamanio 

    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud += 1
            return self.lista
        else:
            print('La lista esta llena')
    
    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            return self.lista[pos]
    
    def mostrar(self):
        print(" {:6} {}".format("lista","Posicion"))
        for pos, ele in enumerate(self.lista):
            print("[{:6}] {:4}".format(ele,pos))  
   

lista1 = Lista()
lista1.append("Elkins")
lista1.append(19)
lista1.append(True)


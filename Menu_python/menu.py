import os
from Pila import Pila 
from Cola import Cola
from lista import Lista 


class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo=titulo
        self.opciones= opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija la opción [1...{}]:".format(len(self.opciones)))
        return opc
opc = ""
while opc != "4":
    os.system("cls")
    men = Menu("Menu Principal",["1)Pila", "2)Cola", "3)Lista","4)Salir" ])
    opc = men.menu()
    dato=int(input("Ingrese el tamaño : "))
    pila1=Pila (dato)
    cola1= Cola (dato)
    lista1= Lista (dato)
    if opc == "1":
        opc1 = ""
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("Menu Pila",["1)Push", "2)Pop", "3)Show","4)Longitud", "5)Empty", "6)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("Usted escogio la operacion push")
                valor=int(input("Ingrese el valor : "))
                print(input(pila1.push(valor)))
                
            elif opc1 == "2":
                os.system("cls")
                print("Usted escogio la operacion pop")
                dato = pila1.pop()
                if dato: print(input("el dato elimanado es :{}".format(dato)))
                else: print(input(" La lista esta vacia"))
            
            elif opc1 == "3":
                os.system("cls")
                print("Usted escogio la operacion show")
                print(input(pila1.show()))
                
            elif opc1 == "4":
                os.system("cls")
                print("Usted escogio la operacion longitud") 
                num=pila1.longitud() 
                print(input("La longitud de la pila es:{}".format(num)))
                
            elif opc1 == "5":
                 os.system("cls")
                 print("Usted escogio la operacion empty") 
                 valor1=pila1.empty()
                 if valor1:print(input("La pila se encuentra vacía"))
                 else : print(input("La pila encuentra con elementos"))
                 
    if opc == "2":
        opc1 = ""
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("Menu Cola ",["1)Push", "2)Pop", "3)Show","4)Longitud", "5)Empty", "6)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("Usted escogio la operacion push")
                valor=int(input("Ingrese el valor : "))
                print(input(cola1.push(valor)))
                
            elif opc1 == "2":
                os.system("cls")
                print("Usted escogio la operacion pop")
                dato = cola1.pop()
                if dato: print(input("el dato elimanado es :{}".format(dato)))
                else: print(input("La lista esta vacia"))
                
            elif opc1 == "3":
                os.system("cls")
                print("Usted escogio la operacion show")
                cola = cola1.show()
                print(input(cola))
                
            elif opc1 == "4":
                os.system("cls")
                print("Usted escogio la operacion longitud") 
                num=cola1.longitud() 
                print(input("La longitud de la cola es:{}".format(num)))
                
            elif opc1 == "5":
                 os.system("cls")
                 print("Usted escogio la operacion empty") 
                 valor1=cola1.empty()
                 if valor1:print(input("La cola se encuentra vacía"))
                 else : print(input("La cola consta con elementos"))
                
    if opc == "3":
        opc1 = ""
        while opc1 != "4":
            os.system("cls")
            men1 = Menu("Menu Lista ",["1)Append", "2)Obtener Posicion ", "3)Mostrar","4)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("Usted escogio la operacion append")
                dato=(input("Ingrese el dato de la lista : "))
                print(input(lista1.append(dato)))
            
            elif opc1 == "2":
                os.system("cls")
                print("Usted escogio la operacion obtener posicion")
                dato=int(input("Ingrese la posicion que desee conocer : "))
                print(input(lista1.obtener(dato)))      
            
            elif opc1 == "3":
                os.system("cls") 
                print("Usted escogio mostrar la lista")
                print(input(lista1.mostrar()))
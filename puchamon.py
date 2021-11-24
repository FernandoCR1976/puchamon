from operator import truediv
import random

numero_ran1=random.randint(50,100)
numero_ran2=random.randint(1,50)
numero_ran3=random.randint(50,100)
numero_ran4=random.randint(1,50)


poke1_exist=False
poke2_exist=False

class pokemon:
    def __init__(self,pNombre,pVida,pAtaque,pContAttack):
        self.nombre=pNombre
        self.vida=pVida
        self.ataque=pAtaque
        self.contAttack=True
        

    def atackque(self,otropokemon):

        input("PRESIONE ENTER PARA ATACAR \n")
        print(self.nombre," ATACA A ",otropokemon.nombre)
        print(" ")

        otropokemon.vida=otropokemon.vida-self.ataque
        self.contAttack=False
        otropokemon.contAttack=True

        if otropokemon.vida>0 :
            print("A ",otropokemon.nombre," le quedan ",otropokemon.vida," puntos de vida\n")
            print(otropokemon.nombre," Es su turno")          
            
            
            if self.vida>0:
                self.contAttack=False
                input("Presione enter para continuar")
        else:
            print(otropokemon.nombre," PERDIO :'( ")
            print("fin del juego")

    def curar(self,otropokemon):

        self.contAttack=False
        otropokemon.contAttack=True

        print("Le restan ",self.vida," puntos de vida \n")
        print("Tiene un ataque de: ",self.ataque," puntos \n")
        print("Puede utilizar sus puntos de ataque para cuararse \n")
        sanar=int(input("Digite la cantidad de puntos a sanar: \n"))
        if sanar <= self.ataque:
            self.ataque=self.ataque-sanar
            self.vida=sanar+self.vida
            print(self.nombre," Cuenta con ",self.vida," puntos de VIDA")
            print(self.nombre," Cuenta con ",self.ataque," puntos de ATAQUE")
        else:
            ("No puede curar tantos puntos")

    def huir(self,otropokemon):
        print(self.nombre,"PERDIO\n",otropokemon.nombre," GANA LA PARTIDA")

            
                


def crear_poke():
    
    print("VAMOS A CREAR AL POKEMON \n")
    nombre=input("Ingrese el nombre de su pokemon: \n")
    global poke1
    global poke1_exist
    vida=numero_ran1
    atack=numero_ran2
    poke1=pokemon(nombre,vida,atack,True)
    poke1_exist=True
    print(poke1.nombre,"VIDA: ",poke1.vida,"ATAQUE: ",poke1.ataque)
    
    return poke1

def crear_enemigo():

    print("VAMOS A CREAR AL POKE ENEMIGO\n")
    nombre=input("ingrese el nombre de su poke ENEMIGO: ")
    global poke2
    vida=numero_ran3
    atack=numero_ran4
    
    poke2=pokemon(nombre,vida,atack,True)
    print(poke2.nombre,"VIDA: ",poke2.vida,"ATAQUE: ",poke2.ataque)
    

    return poke2


    
def inicio():

    if poke1_exist==True and poke2_exist==True:
        print("Los pokemons están listos para la batalla \n")

    else:
        print("Debe de crear a los dos pokemones \n")
        
        menu_crear=int(input("Desea crear los pokemones? \n1.SI\n2.NO \n"))
        if menu_crear==1:
            crear_poke()
            crear_enemigo()
            print("POKEMONES CREADOS \n")

        else:
            print("no se crearon los pokemones")
    
    print("PUEDE INICIAR LA BATALLA \n")
    
   


def menu_batalla():
    #cont=0
    bandera=True

    while bandera:

        if poke1.vida<=0 or poke2.vida<=0:
            bandera=False
        


        empieza=int(input("INDIQUE CUAL POKEMON EMPIEZA \n 1.POKEMON USUARIO \n 2.ENEMIGO \n"))


        
        

        if empieza==1 and poke1.contAttack==True:
            
            

            opc_menu=int(input("DESEA \n 1. ATACAR \n 2.CURARSE \n 3.HUIR \n"))
            if opc_menu==1:
                poke1.atackque(poke2)
                
            elif opc_menu==2 and poke1.contAttack==True:
                poke1.curar(poke1)
                
            elif opc_menu==3:
                print("FIN DEL JUEGO")
                print(poke2.nombre, " GANO EL JUEGO")
                bandera=False


            else:
                print("OPCION INCORRECTA",poke2.nombre)
                input("PRESIONE ENTER PARA CONTINUAR")

        elif empieza==2 and poke2.contAttack==True and bandera==True:
            opc_menu=int(input("DESEA \n 1. ATACAR \n 2.CURARSE \n 3.HUIR \n"))
            if opc_menu==1:
                
                poke2.atackque(poke1)
            elif opc_menu==2 and poke2.contAttack==True:
                
                poke2.curar(poke2)

            elif opc_menu==3:
                print("FIN DEL JUEGO")
                print(poke1.nombre, " GANO EL JUEGO")
                bandera=False
            else:
                print("OPCION INCORRECTA",poke2.nombre)
                input("PRESIONE ENTER PARA CONTINUAR")

        else:
            print("FIN DEL JUEGO")
            input("Presione ENTER pata terminar")
            bandera=False       

        #cont+=1



inicio()

menu_batalla()



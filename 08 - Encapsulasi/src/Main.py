class Hero:
    
    def __init__(self, name, health, attack):
        self.__name = name
        self.__health = health
        self.__attack = attack

    #getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    #setter

    def diserang(self,damage):
        self.__health -= damage
    
    def setAttack(self, powerUp):
        self.__attack += powerUp

# awal dari game
earthshaker = Hero('earthshaker', 50, 5)

print(earthshaker.__dict__)

# game berjalan

print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())


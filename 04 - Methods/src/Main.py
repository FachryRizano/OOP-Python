class Hero:
    #class variable
    jumlah_hero = 0

    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        Hero.jumlah_hero += 1
    # void function, method tanpa return
    def siapa(self):
        print("namaku adalah " + self.name)

    # method dengan argumen
    def healthUp(self,up):
        self.health += up
    
    # method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero('sniper', 100, 10, 5)
hero2 = Hero('mario bros', 90, 5, 10)

hero1.siapa()
hero1.healthUp(10)
print(hero1.getHealth())
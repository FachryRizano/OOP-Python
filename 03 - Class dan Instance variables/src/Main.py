class Hero:
    #class variable / static variable
    jumlah = 0
    def __init__(self, name, health, attack, armor):
        # instance variabel
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        Hero.jumlah += 1

hero1 = Hero("sniper", 100, 10, 4)
hero2 = Hero("Mirana", 100, 15, 1)
hero3 = Hero("Ucup", 1000, 100, 10)

print(hero1.name)
print(hero2.name)
print(hero3.name)
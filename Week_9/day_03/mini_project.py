class Character():
    all_characters = []
    
    def __init__(self,name,life = 20,attack = 10):
        self.name = name
        self.life = life
        self.attack = attack
        self.all_characters.append(self)
    
    def basic_attack(self,other):        
        other.life -= 1
    
    def show_lifeattack(self):
        print(f"{self.name} has {self.life} lives left and {self.attack} attacks left.")    


class Druid(Character):
    def __init__(self,name,life = 20,attack = 10):
        super().__init__(name,life = 20,attack = 10)
        print(f"I am a Druid named {name} and I love to chill in the nature")
    
    def meditate(self):
        self.life += 10
        self.attack -= 2
    
    def animal_help(self):
        self.attack += 5
    
    def fight(self,other_char):
        other_char.life -= (0.75*self.life + 0.75*self.attack)


class Warrior(Character):
    def __init__(self,name,life=20,attack=10):
        super().__init__(name,life=20,attack=10)
        print(f"I am a Warrior named {name} The Caffeine constricts the blood vessels in my body")
    
    def brawl(self,other_char):
        other_char.life -= 2*self.attack
        self.life += 0.5*self.attack
    def train(self):
        self.attack += 2
        self.life += 2
    def roar(self,other_char):
        other_char.attack -= 3


class Mage(Character):
    def __init__(self,name,life = 20,attack = 10):
        super().__init__(name,life = 20,attack = 10)
        print(f"I am a Mage named {name} an ancient tale of a mage who made lush gardens grow in the desert")
    
    def curse(self,other_char):
        other_char.attack -= 2
    
    def summon(self):
        self.attack += 3
    
    def cast_spell(self,other_char):
        other_char.life -= self.attack/self.life


druid1=Druid("Druid Princess")
warrior1=Warrior("War Man")
mage1=Mage("Magic Mage")

druid1.meditate()
warrior1.train()
mage1.summon()

for char in Character.all_characters:
    char.show_lifeattack()

warrior1.roar(mage1)
mage1.cast_spell(warrior1)
druid1.fight(mage1)

for char in Character.all_characters:
    char.show_lifeattack()

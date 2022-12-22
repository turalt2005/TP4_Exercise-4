#Troy Tural 404
#Exercise 4

import math
import random

class Hero:
   def __init__(self, name):
       self.HP = random.randint(2,10) + random.randint(2,10)
       self.ATK = random.randint(1,6)
       self.DEF = random.randint(1,6)
       self.name = name

   def attack(self):
       return random.randint(1,6) + self.ATK


   def damage(self,dmg):
       self.HP -= dmg - self.DEF


   def lives(self):
       if self.HP > 0:
           return True
       if self.HP <= 0:
           return False
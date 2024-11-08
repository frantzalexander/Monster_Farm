import random

from enemy import Enemy


class Zombie(Enemy):
    def __init__(self, health_points: int = 10, attack_damage: int = 1):
        super().__init__(
            type_of_enemy = "Zombie", 
            health_points = health_points, 
            attack_damage = attack_damage
            )
        
    def talk(self):
        print("**Grumbling...**")
        
    def spread_disease(self):
        print("The zombie is spreading infection.") # method Overriding
        
    def special_attack(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.health_points += 2
            print("Zombie regenerated 2HP!")
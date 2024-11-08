import random

from enemy import Enemy


class Ogre(Enemy):
    def __init__(self, health_points: int = 20, attack_damage: int = 3):
        super().__init__(
            type_of_enemy = "Ogre", 
            health_points = health_points, 
            attack_damage = attack_damage
            ) 
        
    def talk(self):
        print("Slams club on the ground.")
        
    def special_attack(self):
        did_special_attack_work = random.random() < 0.2
        if did_special_attack_work:
            self.attack_damage += 2
            print("Ogre gets angry and increases attack by 2!")
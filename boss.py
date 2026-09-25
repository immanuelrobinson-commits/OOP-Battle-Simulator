import random
from enemy import Enemy
import hero

class GobBoss(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health=200, attackPower=11)
        self.gold = 0
    
    def eater(self):
        attackStyle = random.randint(1, 2)
        if attackStyle == 1:
            print("Goblin Boss uses Bite!")
            return 5 * random.randint(1,4)
        else:
            print("Goblin Boss swallow")
            return self.attack_power() * random.randint(1, 2)

    def take_damage(self, damage):
        damage = damage * .75
        super().take_damage(damage)

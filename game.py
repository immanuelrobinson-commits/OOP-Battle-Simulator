from goblin import Goblin
import hero


ARENA_NAME = "The Iron Square"

def battle(hero: hero.Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)

        if hero.is_alive():
            print(f"{hero.name} has defeated {enemy.name}!")
        else:
            print(f"{enemy.name} has defeated {hero.name}!")




def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    
    goblinTwo = Goblin("lileman")
    print(f"{goblinTwo.name} enters the arena with {goblin.health} health.")

    print("But no hero has answered the call... yet.")



    greg = hero.Hero("greg")
    print(f"{greg.name} enters the arena with {greg.health} health.")
    herodamage = greg.attack()
    goblin.take_damage(herodamage)
    battle(greg, goblin)

if __name__ == "__main__":
    main()

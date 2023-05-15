import random


class War:
    def __init__(self, soldiers):
        self.soldiers = soldiers

    def start(self):
        while True:
            alive_soldiers = [
                soldier for soldier in self.soldiers if soldier.is_alive()
            ]
            if len(alive_soldiers) < 2:
                break
            soldier1, soldier2 = random.sample(alive_soldiers, 2)
            while True:
                soldier1.shoot_at(soldier2)
                if not soldier2.is_alive():
                    print(f"{soldier2} died!")
                    break
                soldier2.shoot_at(soldier1)
                if not soldier1.is_alive():
                    print(f"{soldier1} died!")
                    break

    def get_winner(self):
        alive_nations = set(
            soldier.nation for soldier in self.soldiers if soldier.is_alive()
        )
        if len(alive_nations) == 1:
            return alive_nations.pop()
        else:
            return None


class Weapon:
    def __init__(self, bullet):
        self.bullet = bullet

    def shoot(self):
        if self.bullet > 0:
            self.bullet -= 1
            return True
        else:
            return False

    def load(self, bullet):
        self.bullet += bullet


class Soldier:
    def __init__(self, weapon, nation, life):
        self.weapon = weapon
        self.nation = nation
        self.life = life

    def is_alive(self):
        return self.life > 0

    def shoot_at(self, other_soldier):
        if self.weapon.shoot():
            print(f"{self} shoots at {other_soldier}!")
            other_soldier.life -= 1
        else:
            print(f"{self} is out of bullets!")

    def load_weapon(self, bullet):
        self.weapon.load(bullet)

    def __str__(self):
        return f"{self.nation} soldier with {self.weapon.bullet} bullets and {self.life} life"


# Example usage
weapon1 = Weapon(10)
soldier1 = Soldier(weapon1, "Nation1", 5)
weapon2 = Weapon(10)
soldier2 = Soldier(weapon2, "Nation2", 5)
weapon3 = Weapon(10)
soldier3 = Soldier(weapon3, "Nation1", 5)
weapon4 = Weapon(10)
soldier4 = Soldier(weapon4, "Nation2", 5)

war = War([soldier1, soldier2, soldier3, soldier4])
war.start()
print(war.get_winner())

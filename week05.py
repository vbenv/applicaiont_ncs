class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.health = 100  # Basic health

    def attack(self, target, skill):
        print(f"{self.name} uses {skill} on {target.name}!")
        target.health -= 20  # Arbitrary damage
        print(f"{target.name}'s health: {target.health}")
        if target.health <= 0:
            print(f"{target.name} fainted!")

    def __str__(self):
        return f"{self.name} ({self.type} type, Health: {self.health})"

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", "Electric")

    def thunderbolt(self, target):
        print("Pikachu Thunderbolt!!!")
        self.attack(target, "Thunderbolt")

class Charizard(Pokemon):
    def __init__(self):
        super().__init__("Charizard", "Fire/Flying")

    def flamethrower(self, target):
        print("Charizard Flamethrower!!!")
        self.attack(target, "Flamethrower")

# Flyable Interface (Mixin) - Represents the ability to fly
class Flyable:
    def __init__(self):
        self.is_flying = False

    def fly(self):
        if hasattr(self, 'wings') or hasattr(self, 'balloon'):  # Needs wings or a balloon to fly
            print(f"{self.__class__.__name__} takes to the skies!")
            self.is_flying = True
        else:
            print(f"{self.__class__.__name__} cannot fly.")

    def land(self):
        print(f"{self.__class__.__name__} lands.")
        self.is_flying = False

# Wings Class
class Wings:
    def __init__(self, kind="Normal Wings"):
        self.kind = kind
        print(f"{self.__class__.__name__} created ({self.kind})")

# Balloon Class
class Balloon:
    def __init__(self, color="Red"):
        self.color = color
        print(f"{self.__class__.__name__} created ({self.color})")

# Flyable and Wings inheriting class (Charizard with wings)
class WingedCharizard(Charizard, Flyable):
    def __init__(self):
        Charizard.__init__(self)
        Flyable.__init__(self)
        self.wings = Wings("Steel Wings")  # Composition: Has a Wings object as a property

# Flyable and Balloon inheriting class (Pikachu with balloon)
class BalloonPikachu(Pikachu, Flyable):
    def __init__(self):
        Pikachu.__init__(self)
        Flyable.__init__(self)
        self.balloon = Balloon("Yellow")  # Composition: Has a Balloon object as a property

# Usage Example
pikachu = Pikachu()
charizard = Charizard()
winged_charizard = WingedCharizard()
balloon_pikachu = BalloonPikachu()

print(pikachu)
print(charizard)
print(winged_charizard)
print(balloon_pikachu)

pikachu.thunderbolt(charizard)
charizard.flamethrower(pikachu)

winged_charizard.fly()
winged_charizard.flamethrower(pikachu)
winged_charizard.land()

balloon_pikachu.fly()
balloon_pikachu.thunderbolt(charizard)
balloon_pikachu.land()
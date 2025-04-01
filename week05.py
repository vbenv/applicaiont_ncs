# copilot
# 포켓몬 기본 클래스
class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self):
        print(f"{self.name} uses a basic attack!")

# 피카츄 클래스 (포켓몬 상속)
class Pikachu(Pokemon):
    def __init__(self, level):
        super().__init__("Pikachu", level)

    def attack(self):
        print(f"{self.name} uses Thunderbolt!")

# 리자몽 클래스 (포켓몬 상속 + Flyable 인터페이스 사용)
class Charizard(Pokemon):
    def __init__(self, level):
        super().__init__("Charizard", level)
        self.flyable = Flyable()

    def attack(self):
        print(f"{self.name} uses Flamethrower!")

    def fly(self):
        self.flyable.fly(self.name)

# Flyable 클래스
class Flyable:
    def fly(self, name):
        print(f"{name} is flying high in the sky!")

# Wings 클래스
class Wings:
    def flap(self):
        print("Wings are flapping!")

# Balloon 클래스
class Balloon:
    def float(self):
        print("The balloon is floating in the air!")

# 테스트
pikachu = Pikachu(level=10)
charizard = Charizard(level=36)

# 피카츄와 리자몽 행동 테스트
pikachu.attack()  # Pikachu uses Thunderbolt!
charizard.attack()  # Charizard uses Flamethrower!
charizard.fly()  # Charizard is flying high in the sky!
# Not Suggestion version
class Pokemon:
    """모든 포켓몬의 기본 클래스"""

    def __init__(self, name, level=1, hp=100):
        self.name = name
        self.level = level
        self.hp = hp
        self.type = "Normal"

    def attack(self):
        print(f"{self.name}이(가) 공격합니다!")

    def make_sound(self):
        print(f"{self.name}이(가) 소리를 냅니다!")

    def level_up(self):
        self.level += 1
        self.hp += 10
        print(f"{self.name}이(가) 레벨 {self.level}이(가) 되었습니다!")


class Flyable:
    """날 수 있는 능력을 가진 클래스"""

    def fly(self):
        print(f"{self.name}이(가) 날아오릅니다!")

    def land(self):
        print(f"{self.name}이(가) 착륙합니다!")


class Wings:
    """날개를 가진 객체를 표현하는 클래스"""

    def __init__(self, wingspan=1.0):
        self.wingspan = wingspan

    def flap(self):
        print(f"날개를 펄럭입니다! (날개 폭: {self.wingspan}m)")


class Balloon:
    """풍선을 가진 객체를 표현하는 클래스"""

    def __init__(self, color="빨간색"):
        self.color = color

    def inflate(self):
        print(f"{self.color} 풍선이 부풀어 오릅니다!")

    def deflate(self):
        print(f"{self.color} 풍선이 수축합니다!")


class Pikachu(Pokemon):
    """피카츄 클래스"""

    def __init__(self, name="피카츄", level=1, hp=100):
        super().__init__(name, level, hp)
        self.type = "Electric"

    def make_sound(self):
        print("피카피카!")

    def thunder_shock(self):
        print(f"{self.name}이(가) 전기 충격을 발사합니다!")


class Charizard(Pokemon, Flyable):
    """리자몽 클래스"""

    def __init__(self, name="리자몽", level=36, hp=200):
        Pokemon.__init__(self, name, level, hp)
        self.type = "Fire/Flying"
        self.wings = Wings(wingspan=2.5)  # 합성 관계

    def make_sound(self):
        print("그아아아!")

    def fly(self):
        print(f"{self.name}이(가) 하늘 높이 날아오릅니다!")
        self.wings.flap()

    def flamethrower(self):
        print(f"{self.name}이(가) 화염방사를 합니다!")


class FlyingPikachu(Pikachu, Flyable):
    """날아다니는 피카츄 클래스"""

    def __init__(self, name="날아다니는 피카츄", level=15, hp=120):
        Pikachu.__init__(self, name, level, hp)
        self.balloon = Balloon(color="노란색")  # 합성 관계

    def fly(self):
        print(f"{self.name}이(가) 풍선을 타고 하늘을 날아갑니다!")
        self.balloon.inflate()

    def land(self):
        print(f"{self.name}이(가) 땅으로 내려옵니다.")
        self.balloon.deflate()


# 예제 사용
if __name__ == "__main__":
    pika = Pikachu(level=10)
    pika.make_sound()
    pika.thunder_shock()

    charizard = Charizard()
    charizard.attack()
    charizard.fly()
    charizard.flamethrower()

    flying_pika = FlyingPikachu()
    flying_pika.make_sound()
    flying_pika.fly()
    flying_pika.thunder_shock()
    flying_pika.land()
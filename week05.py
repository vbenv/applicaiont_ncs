## 📌 기본 포켓몬 클래스
class Pokemon:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f"{self.name}의 일반 공격!")

    def introduce(self):
        print(f"나는 {self.name}이다!")


## ⚡ 피카츄 클래스 (상속)
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("피카츄")

    # 메서드 오버라이딩
    def attack(self):
        print("피카츄의 백만볼트 공격!")

    # 고유 기능
    def thunder(self):
        print("천둥번개 발사!")


## 🔥 리자몽 클래스 (Composition + Flyable 의존)
class Charizard(Pokemon):
    def __init__(self):
        super().__init__("리자몽")
        self.wings = Wings()  # Composition: 날개 객체 소유

    def attack(self):
        print("리자몽의 화염방사!")

    def fly(self):
        self.wings.use()  # Wings 클래스에 기능 위임


## ✈️ Flyable 인터페이스 (의존 관계)
class Flyable:
    def fly(self):
        pass  # 구현은 구체 클래스에 위임


## 🦅 Wings 클래스 (Flyable 구현)
class Wings(Flyable):
    def use(self):
        print("날개를 퍼덕이며 날아감!")


## 🎈 Balloon 클래스 (Flyable 구현)
class Balloon(Flyable):
    def use(self):
        print("풍선을 타고 공중 부양!")


## 🚀 실행 예시
pikachu = Pikachu()
pikachu.introduce()  # 출력: 나는 피카츄이다!
pikachu.attack()  # 출력: 피카츄의 백만볼트 공격!

charizard = Charizard()
charizard.fly()  # 출력: 날개를 퍼덕이며 날아감!

# Balloon을 사용하는 경우
balloon_pokemon = Balloon()
balloon_pokemon.use()  # 출력: 풍선을 타고 공중 부양!
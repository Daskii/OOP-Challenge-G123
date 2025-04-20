import random

class Pet:
    def __init__(self, name, pet_type="Mystery Pet", age=None, hunger=5, energy=5, happiness=5,
                 health=10, tricks=None, level=1, experience=0):
        self.name = name
        self.pet_type = pet_type
        self.age = age if age is not None else random.randint(1, 5)
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.health = health
        self.tricks = tricks if tricks is not None else []
        self.level = level
        self.experience = experience

    def eat(self, food=None):
        if not food:
            food = random.choice(["Dog Food", "Cat Food", "Fish Flakes", "Bird Seeds"])
        self.hunger = min(10, self.hunger + 3)
        self.energy = max(0, self.energy - 1)
        self.happiness = min(10, self.happiness + 1)
        self.gain_xp(1)
        print(f"{self.name} enjoyed some {food}! 🍽️")

    def sleep(self):
        if self.energy < 10:
            self.energy = min(10, self.energy + 3)
            self.happiness = max(0, self.happiness - 1)
            self.age += 1
            print(f"{self.name} took a nap and feels refreshed! 💤 Age is now {self.age}.")
            self.update_health()
        else:
            print(f"{self.name} is not tired enough to sleep.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.hunger = min(10, self.hunger + 1)
            self.happiness = min(10, self.happiness + 2)
            self.gain_xp(2)
            print(f"{self.name} had a blast playing! 🎾")
        else:
            print(f"{self.name} is too tired to play. 😓")

    def train(self, trick):
        if self.energy >= 1:
            if trick not in self.tricks:
                self.tricks.append(trick)
                print(f"{self.name} learned a new trick: {trick}! 🐾")
                self.happiness = min(10, self.happiness + 2)
                self.gain_xp(3)
            else:
                print(f"{self.name} already knows {trick}!")
            self.energy = max(0, self.energy - 1)
        else:
            print(f"{self.name} is too tired to learn new tricks.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)} 🧠")
        else:
            print(f"{self.name} hasn’t learned any tricks yet.")

    def update_health(self):
        if self.hunger >= 9 or self.happiness <= 2:
            self.health = max(0, self.health - 1)
            print(f"{self.name} doesn't feel too well... ❤️‍🩹 Health is now {self.health}")
        elif self.hunger <= 3 and self.happiness >= 8:
            self.health = min(10, self.health + 1)

    def gain_xp(self, amount):
        self.experience += amount
        if self.experience >= self.level * 10:
            self.experience -= self.level * 10
            self.level += 1
            print(f"🎉 {self.name} leveled up! Now at level {self.level}!")

    def progress_bar(self, label, value, emoji=""):
        filled = "■" * value
        empty = "□" * (10 - value)
        return f"{label} {emoji}: [{filled}{empty}] {value}/10"

    def get_status(self):
        print(f"\n📋 {self.name}'s Status")
        print(f"Type: {self.pet_type}")
        print(f"Age: {self.age}")
        print(f"Level: {self.level} | XP: {self.experience}/{self.level * 10}")
        print(self.progress_bar("Hunger", self.hunger, "🍗"))
        print(self.progress_bar("Energy", self.energy, "⚡"))
        print(self.progress_bar("Happiness", self.happiness, "😊"))
        print(self.progress_bar("Health", self.health, "❤️"))
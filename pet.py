import random
# This program defines a virtual pet simulation where you can interact with a pet object.
# The Pet class includes attributes like hunger, energy, happiness, and health, 
# and methods to perform actions such as eating, sleeping, playing, and training.
class Pet:
    def __init__(self, name, pet_type="Mystery Pet"):
        self.name = name
        self.pet_type = pet_type
        self.age = random.randint(1, 5)
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.health = 10
        self.tricks = []
        self.level = 1
        self.experience = 0

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        self.update_health()
        print(f"{self.name} ate a tasty meal!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        self.update_health()
        print(f"{self.name} had a refreshing nap.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            self.gain_xp(2)
            print(f"{self.name} played joyfully!")
        else:
            print(f"{self.name} is too tired to play.")

    def train(self, trick):
        self.tricks.append(trick)
        self.gain_xp(5)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn’t learned any tricks yet.")

    def update_health(self):
        self.health = 10 - abs(self.hunger - 5) - abs(self.energy - 5)
        self.health = max(0, min(self.health, 10))

    def gain_xp(self, amount):
        self.experience += amount
        if self.experience >= 10:
            self.level += 1
            self.experience = 0
            print(f"🎉 {self.name} leveled up to Level {self.level}!")

    def get_status(self):
        print(f"🦴 {self.name}'s Status ({self.pet_type}) - Age {self.age}")
        print(f"  Level: {self.level} | XP: {self.experience}/10")
        print(f"  Hunger: {self.hunger}/10 | Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10 | Health: {self.health}/10")
        print("-" * 30)


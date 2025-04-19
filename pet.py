import random


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
            print(f"{self.name} took a nap and feels refreshed!")
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
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 2)
            self.energy = max(0, self.energy - 1)
            self.gain_xp(3)
            print(f"{self.name} learned a new trick: {trick}! 🐾")
        else:
            print(f"{self.name} is too tired to learn new tricks.")
        

    def show_tricks(self):
       

    def update_health(self):
        

    def gain_xp(self, amount):
        

    def get_status(self):
        

import os
import json
from pet import Pet

def load_pets(filename="pets.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        data = json.load(f)
        return [Pet(**pet) for pet in data]

def save_pets(pets, filename="pets.json"):
    with open(filename, "w") as f:
        json.dump([pet.__dict__ for pet in pets], f, indent=2)

def list_pets(pets):
    print("\n🐾 Existing Pets:")
    for idx, pet in enumerate(pets):
        print(f"{idx + 1}. {pet.name} ({pet.pet_type})")

def interact_with_pet(pet):
    while True:
        print(f"\nWhat would you like to do with {pet.name}?")
        print("1. Feed 🍽️")
        print("2. Sleep 😴")
        print("3. Play 🎾")
        print("4. Train 🧠")
        print("5. Show Tricks 🎩")
        print("6. Show Status 📋")
        print("7. Rename ✏️")
        print("8. Exit and Save 💾")
        choice = input("Choose (1-8): ").strip()

        if choice == "1":
            food = input("What food would you like to give? (Press enter for random): ").strip()
            pet.eat(food if food else None)
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            trick = input("Enter a new trick: ").strip()
            if trick:
                pet.train(trick)
        elif choice == "5":
            pet.show_tricks()
        elif choice == "6":
            pet.get_status()
        elif choice == "7":
            new_name = input(f"Enter new name for {pet.name}: ").strip()
            if new_name:
                print(f"{pet.name} is now named {new_name}!")
                pet.name = new_name
        elif choice == "8":
            break
        else:
            print("Invalid option.")

def main():
    pets = load_pets()
    
    if pets:
        list_pets(pets)
        selected_index = input("\nSelect a pet by number or type 'new' to create one: ").strip()
        if selected_index.lower() == "new":
            name = input("Pet name: ")
            pet_type = input("Pet type: ")
            selected_pet = Pet(name=name, pet_type=pet_type)
            pets.append(selected_pet)
        elif selected_index.isdigit() and 1 <= int(selected_index) <= len(pets):
            selected_pet = pets[int(selected_index) - 1]
        else:
            print("Invalid selection. Exiting.")
            return
    else:
        print("🐣 No pets found. Let's create your first one!")
        name = input("Pet name: ")
        pet_type = input("Pet type: ")
        selected_pet = Pet(name=name, pet_type=pet_type)
        pets.append(selected_pet)

    interact_with_pet(selected_pet)
    save_pets(pets)
    print("✅ Pet data saved!")

if __name__ == "__main__":
    main()
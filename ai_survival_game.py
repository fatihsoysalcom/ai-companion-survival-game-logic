import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 0
        self.thirst = 0
        self.inventory = []

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {amount} damage. Health: {self.health}")

    def eat(self, food):
        if food in self.inventory:
            self.inventory.remove(food)
            self.hunger -= 20 # Reduces hunger
            if self.hunger < 0:
                self.hunger = 0
            print(f"{self.name} ate {food}. Hunger: {self.hunger}")
        else:
            print(f"{self.name} doesn't have {food}.")

    def drink(self, water):
        if water in self.inventory:
            self.inventory.remove(water)
            self.thirst -= 20 # Reduces thirst
            if self.thirst < 0:
                self.thirst = 0
            print(f"{self.name} drank {water}. Thirst: {self.thirst}")
        else:
            print(f"{self.name} doesn't have {water}.")

    def needs_attention(self):
        return self.health < 50 or self.hunger > 70 or self.thirst > 70

class AIAssistant:
    def __init__(self, player):
        self.player = player

    def assess_situation(self):
        # AI assesses player's needs and environment
        if self.player.health < 30:
            print("AI: Your health is critical! We need to find supplies.")
            return "find_supplies"
        elif self.player.hunger > 80:
            print("AI: You seem very hungry. Let's look for food.")
            return "find_food"
        elif self.player.thirst > 80:
            print("AI: You're extremely thirsty. Water is our priority.")
            return "find_water"
        else:
            print("AI: Everything seems stable for now. Let's explore cautiously.")
            return "explore"

    def recommend_action(self):
        # AI provides a recommendation based on the assessment
        action = self.assess_situation()
        if action == "find_supplies":
            return "Search for medical herbs or bandages."
        elif action == "find_food":
            return "Look for berries, mushrooms, or small game."
        elif action == "find_water":
            return "Search for a stream or collect dew."
        else:
            return "Keep an eye out for threats and useful items."

    def assist(self):
        # AI performs an action to help the player
        if self.player.needs_attention():
            if self.player.health < 50:
                print("AI is trying to find basic medical supplies...")
                if random.random() < 0.3: # Chance to find something
                    print("AI found some herbs!")
                    self.player.inventory.append("herbs")
            elif self.player.hunger > 70:
                print("AI is searching for edible plants...")
                if random.random() < 0.4: # Chance to find something
                    print("AI found some berries!")
                    self.player.inventory.append("berries")
            elif self.player.thirst > 70:
                print("AI is looking for a water source...")
                if random.random() < 0.35: # Chance to find something
                    print("AI found a small stream!")
                    self.player.inventory.append("water")
        else:
            print("AI is scouting the immediate area for resources or dangers.")

# --- Game Simulation ---

player1 = Player("Alex")
ai_companion = AIAssistant(player1)

print(f"--- Starting Survival Scenario for {player1.name} ---")

# Simulate a few game turns
for turn in range(5):
    print(f"\n--- Turn {turn + 1} ---")

    # Player takes some random damage and gets hungry/thirsty
    if random.random() < 0.5:
        player1.take_damage(random.randint(5, 15))
    player1.hunger += random.randint(10, 25)
    player1.thirst += random.randint(10, 25)

    # AI assesses and recommends
    ai_companion.assess_situation()
    recommendation = ai_companion.recommend_action()
    print(f"AI Recommendation: {recommendation}")

    # AI attempts to assist if player needs attention
    ai_companion.assist()

    # Player uses items if available (simplified)
    if "berries" in player1.inventory and player1.hunger > 50:
        player1.eat("berries")
    if "water" in player1.inventory and player1.thirst > 50:
        player1.drink("water")
    if "herbs" in player1.inventory and player1.health < 70:
        player1.inventory.remove("herbs") # Using herbs to heal
        player1.health += 15
        if player1.health > 100:
            player1.health = 100
        print(f"{player1.name} used herbs. Health: {player1.health}")

    print(f"Current Status: Health={player1.health}, Hunger={player1.hunger}, Thirst={player1.thirst}, Inventory={player1.inventory}")

    if player1.health == 0:
        print("\nGame Over! Alex has succumbed to the wilderness.")
        break

if player1.health > 0:
    print("\nSurvival continues...")

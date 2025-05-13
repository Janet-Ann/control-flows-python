# Base class
class Superhero:
    def __init__(self, name, superpower, strength, origin):
        self.name = name
        self.superpower = superpower
        self.strength = strength
        self.origin = origin

    def display_details(self):
        print(f"🦸 Name: {self.name}")
        print(f"💥 Superpower: {self.superpower}")
        print(f"💪 Strength: {self.strength}")
        print(f"🌍 Origin: {self.origin}")

    def use_power(self):
        print(f"{self.name} uses {self.superpower}!")

# Subclass for inheritance demonstration
class Mutant(Superhero):
    def __init__(self, name, superpower, strength, origin, mutation_level):
        super().__init__(name, superpower, strength, origin)
        self.mutation_level = mutation_level

    def evolve(self):
        print(f"{self.name} is evolving! Mutation level increased to {self.mutation_level + 1}")

hero1 = Superhero("Photon", "Light Manipulation", 90, "Andromeda")
hero1.display_details()
hero1.use_power()

mutant1 = Mutant("GeneX", "Telekinesis", 85, "Earth", 3)
mutant1.display_details()
mutant1.evolve()

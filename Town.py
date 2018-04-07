#Ryan Kaplan
import random, Villager as v

class Town:

    # Initializes the town
    def __init__(self, name):
        self.day_count = 1
        self.name = name

        villager_list = []
        for i in range(15, 25):
            villager = v.Villager()
            villager_list.append(villager)

        self.villagers = villager_list

    # Displays the attributes of the town
    def display(self):
        print(self.name)
        print("Day", self.day_count)
        print()
        print("Villagers:")
        for villager in self.villagers:
            print(villager)



#Ryan Kaplan
import random, Villager as v, time

class Town:

    # Initializes the town
    def __init__(self, name):
        self.day_count = 1
        self.name = name
        self.villagers = self.init_villagers()

        self.chickens = 0
        self.roosters = 0

        self.wood = 300
        self.stone = 300
        self.ore = 300
        self.iron = 0

        self.wheat = 500
        self.eggs = 500
        self.food = self.wheat + self.eggs

    # Creates an initial population of villagers
    def init_villagers(self):
        villager_list = []
        population = random.randrange(10, 20)
        for i in range(0, population):
            villager = v.Villager()
            villager_list.append(villager)

        return villager_list

    #A day passes, and all of the relevant factors update
    def pass_day(self):
        if self.day_count % 365 == 0:
            for villager in self.villagers:
                villager.age += 1

        self.day_count += 1


    # Displays the attributes of the town
    def display(self):
        print(self.name)
        print("Day", self.day_count)
        print()
        time.sleep(1)

        print("Villagers:")
        for villager in self.villagers:
            print(villager)
        time.sleep(1)

        print()
        print("Resources:")
        print("Wood: " + " " * (35 - len("Wood") - len(str(self.wood))) + str(self.wood))
        print("Stone: " + " " * (35 - len("Stone") - len(str(self.stone))) + str(self.stone))
        print("Ore: " + " " * (35 - len("Ore") - len(str(self.ore))) + str(self.ore))
        print("Iron: " + " " * (35 - len("Iron") - len(str(self.iron))) + str(self.iron))

        time.sleep(1)
        print()
        print("Total Food: " + " " * (35 - len("Total Food") - len(str(self.food))) + str(self.food))
        print("Wheat: " + " " * (35 - len("Wheat") - len(str(self.wheat))) + str(self.wheat))
        print("Eggs: " + " " * (35 - len("Eggs") - len(str(self.eggs))) + str(self.eggs))
        time.sleep(1)



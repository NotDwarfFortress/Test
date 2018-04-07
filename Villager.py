# Ryan Kaplan
import random

class Villager:

    # Initializes the villager object
    def __init__(self):
        self.true_age = random.randrange(0, (80 * 365))
        self.age = int(self.true_age / 365)
        sex = random.randrange(0, 2)
        if sex == 0:
            self.sex = "Female"
        else:
            self.sex = "Male"
        self.name = self.pick_name(self.sex)
        self.job = self.init_occupation(self.age)
        self.strength = self.strength(self.age, self.job)

    # Represents the villager as a string
    def __str__(self):
        return "Name: " + self.name + " " * (10 - len(self.name)) \
        + "Sex: " + self.sex + " " * (9 - len(self.sex)) + "Age: "\
        + str(self.age) + " " * (5 - len(str(self.age))) + self.job \
        + " " * (15 - len(self.job)) + "Strength: " + " " + str(self.strength)

    # Generates a name for each villager
    def pick_name(self, sex):

        male_prefix = ["Tor", "Bor", "Carl", "Sven", "Johan", "Jarl"]
        male_suffix = ["ist", "en", "ic", "dor", "son", ]

        female_prefix = ["Ann", "Stell", "Ag", "Frej", "Katy"]
        female_suffix = ["a", "es", "is", "ia", "ea", "ara"]

        if sex == "Male":
            prefix_choice = random.randrange(0, len(male_prefix))
            suffix_choice = random.randrange(0, len(male_suffix))
            return male_prefix[prefix_choice] + male_suffix[suffix_choice]

        elif sex == "Female":
            prefix_choice = random.randrange(0, len(female_prefix))
            suffix_choice = random.randrange(0, len(female_suffix))
            return female_prefix[prefix_choice] + female_suffix[suffix_choice]

    # Generates an Occupation for each Villager
    def init_occupation(self, age):

        occupations = ["Lumberjack", "Farmer", "Miner", "Blacksmith", "Carpenter", "Doctor", "Wizard", "Alchemist"]

        if age < 15:
            return "Child"

        else:
            choice = random.randrange(0, len(occupations))
            return occupations[choice]

    # Generates Strength stat for each Villager
    def strength(self, age, job):

        base_stat = random.randrange(10, 20)
        agemod = 0
        jobmod = 0

        if age < 15:
            agemod = agemod - 5
        if 15 < age < 19:
            agemod = agemod + 5
        if 18 < age < 33:
            agemod = agemod + 15
        if 32 < age < 46:
            agemod = agemod + 10
        if 45 < age < 56:
            agemod = agemod + 5
        if age > 55:
            agemod = agemod - 5
        if age > 70:
            agemod = agemod - 5
        if age > 80:
            agemod = agemod - 5
        if age > 90:
            agemod = agemod - 5

        if job == "Lumberjack" or job == "Miner" or job == "Blacksmith" or job == "Carpenter":
            jobmod = 15
        if job == "Farmer":
            jobmod = 5
        if job == "Doctor" or job == "Wizard" or job == "Alchemist":
            jobmod = 0

        strength = base_stat + agemod + jobmod
        return strength






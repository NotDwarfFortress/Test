# Ryan Kaplan
import random

class Villager:

    # Initializes the villager object
    def __init__(self):
        self.age = random.randrange(0, 80)
        sex = random.randrange(0, 2)
        if sex == 0:
            self.sex = "Female"
        else:
            self.sex = "Male"
        self.name = self.pick_name(self.sex)

    # Represents the villager as a string
    def __str__(self):
        return "Name: " + self.name + " " * (10 - len(self.name)) \
        + "Sex: " + self.sex + " " * (9 - len(self.sex)) + "Age: "\
        + str(self.age)

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


import random

class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature: {} which is level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 20) * self.level

class Wizard(Creature):

    def attack(self, creature):
        print("{} comes forth to attack the wild {}!!".format(
            self.name, creature.name
        ))

        my_roll = self.get_defensive_roll()
        # creature_roll = random.randint(1, 20) * creature.level
        creature_roll = creature.get_defensive_roll()

        print("{} has scored {}".format(self.name, my_roll))
        print()
        print("The enemy {} has scored {}".format(creature.name, creature_roll))
        print()

        if my_roll >= creature_roll:
            print("{} has outplayed {} thus making him victorious!".format(self.name, creature.name))
            print()
            return True
        else:
            print("{} has unfortunately been defeated by {}.".format(self.name, creature.name))
            print()
            return False


class Weakling(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Legend(Creature):
    def __init__(self, name, level, booming_voice, breaths_fire ):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.booming_voice = booming_voice

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 2 if self.breaths_fire else 1
        voice_modifier = self.booming_voice / 4

        return base_roll * fire_modifier * voice_modifier













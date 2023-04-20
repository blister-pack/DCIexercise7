import random


class CharacterMaker:
    created_chars = []
    char_class = ["Barbarian", "Cleric", "Druid"]

    def __init__(self, char_name):
        self.name = char_name
        self.strength = random.randint(3, 15)
        self.health = random.randint(3, 15)
        self.magic = random.randint(3, 15)
        self.initiative = random.randint(3, 15)
        self.char_clasz = CharacterMaker.char_class[random.randint(0, 2)]

        if self.char_clasz == CharacterMaker.char_class[0]:
            self.strength *= 3
            self.health *= 3
        elif self.char_clasz == CharacterMaker.char_class[1]:
            self.magic *= 3
            self.initiative *= 3
        elif self.char_clasz == CharacterMaker.char_class[2]:
            self.health *= 2
            self.magic *= 2
            self.initiative *= 2


# -------------------------------------------


def creator_of_characters():
    num_of_characters = int(input("How many characters do you want to create? "))

    for i in range(0, num_of_characters):
        player = CharacterMaker(input(f"Name character {i+1}: "))
        CharacterMaker.created_chars.append(player)

    for char in CharacterMaker.created_chars:
        print(
            f"{char.name} is a {char.char_clasz}!\n    Strength: {char.strength}\n    Magic: {char.magic}\n    Health: {char.health}\n    Initiative: {char.initiative}\n\n"
        )


creator_of_characters()

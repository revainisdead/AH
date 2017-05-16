import random

import game.constants as c


class BaseItem:
    def __init__(self, name):
        # Every item is defined and should be unique
        self.name = name

        self.level = game.c.MAX_LEVEL
        self.rarity = self.random_rarity()
        # Generate stats once on creation, dependent on rarity
        self.stats = generate_stats()


    def generate_stats(rarity):
        return {
            c.Stats.STR: __random_stat(),
            c.Stats.INT: __random_stat(),
            c.Stats.AGI: __random_stat(),
        }


    def __random_stat():
        # XXX level and rarity algorithm to determine stat range
        return random.randint(30, 100)


class Axe(BaseItem):
    def __init__():
        super.__init__()



class ItemStore:
    """
    Hold item for all names in the game
    Store as a cache, maybe
    """
    pass


# XXX normally items would be created on drop
def dropitem():
    # Randomize item to drop . . .
    # itemstore.drop()

    item = Axe()



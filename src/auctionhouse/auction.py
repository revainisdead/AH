

class Auction:
    def __init__(self, item_id):
        self.bought = False    # new items haven't been bought
        self.item_id = item_id


    def bought(self):
        """ External function """
        self.bought = True



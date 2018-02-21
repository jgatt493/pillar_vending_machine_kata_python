"""Coins and Products"""

QUARTER = "quarter"
DIME = "dime"
NICKEL = "nickel"

COLA = "cola"
CANDY = "candy"
CHIPS = "chips"

class VendingMachine:

    def __init__(self):
        self.products = {COLA : 1.00, CHIPS : .50, CANDY : .65}
        self.valid_coins = {QUARTER : .25, DIME : .10, NICKEL : .5}
        self.accepted_coins = []
        self.rejected_coins = []
        self.is_selected = None

    def select_product(self, product):
        self.is_selected = product
        
    def display(self):
        if len(self.accepted_coins) == 0 and self.is_selected == None:
            return "INSERT COINS"
        if self.is_selected != None:
            if self.is_selected in self.products:
                return "PRICE " + format(self.products.get(self.is_selected), '.2f')
test = VendingMachine()

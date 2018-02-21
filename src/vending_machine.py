"""Coins and Products"""

QUARTER = "quarter"
DIME = "dime"
NICKEL = "nickel"

COLA = "cola"
CANDY = "candy"
CHIPS = "chips"

class VendingMachine:

    def __init__(self):
        self.products = [(COLA, 1.00),(CANDY, 0.65),(CHIPS, 0.50)]
        self.valid_coins = [(QUARTER, .25),(DIME, .10),(NICKEL, .05)]
        self.accepted_coins = []
        self.rejected_coins = []
        self.is_selected = None

    def display(self):
        if len(self.accepted_coins) == 0 and self.is_selected == None:
            return "INSERT COINS"
        if self.is_selected != None:
            return "PRICE ", 

test = VendingMachine()
    

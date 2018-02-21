"""Coins and Products"""

QUARTER = "quarter"
DIME = "dime"
NICKEL = "nickel"
PENNY = "penny"

COLA = "cola"
CANDY = "candy"
CHIPS = "chips"

class VendingMachine:

    def __init__(self):
        self.products = {COLA : 1.00, CHIPS : .50, CANDY : .65}
        self.valid_coins = {QUARTER : 0.25, DIME : 0.10, NICKEL : 0.5}
        self.accepted_coins = []
        self.rejected_coins = []
        self.returned_coins = []
        self.is_selected = None

    def select_product(self, product):
        self.is_selected = product
        
    def display(self):
        if len(self.accepted_coins) == 0 and self.is_selected == None:
            return "INSERT COINS"
        elif self.is_selected != None and len(self.accepted_coins) == None:
            if self.is_selected in self.products:
                return "PRICE " + format(self.products.get(self.is_selected), '.2f')
        elif self.is_selected != None and len(self.accepted_coins) != None:

            if (self.products.get(self.is_selected) - sum(self.accepted_coins)) > 0 :

                return "PRICE " + format((self.products.get(self.is_selected) - sum(self.accepted_coins)), '.2f')

            elif (self.products.get(self.is_selected) - sum(self.accepted_coins)) == 0 :

                return "THANK YOU"
        
        
    def take_coins(self, coin):
        if coin in self.valid_coins:
            cost = self.products.get(self.is_selected)
            coin = self.valid_coins.get(coin)
            self.accepted_coins.append(coin)
        else:
            self.rejected_coins.append(coin)
            
        
        
        

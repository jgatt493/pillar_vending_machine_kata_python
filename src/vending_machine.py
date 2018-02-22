"""Coins and Products"""

QUARTER = "quarter"
DIME = "dime"
NICKEL = "nickel"
PENNY = "penny"

COLA = "cola"
CANDY = "candy"
CHIPS = "chips"

class VendingMachine:

    """A representation of a vending machine.

    products: dictionary of products mapped to their costs
    valid_coins: dictionary oof coins mapped to their values
    accpeted_coins: list for holding accepted coins
    rejecte_coins: list for holding rejected coins
    returned_coins: list of holding returned coins
    is_selected: variable used to store product selection
    """

    def __init__(self):
        
        self.products = {COLA : 1.00, CHIPS : .50, CANDY : .65}
        self.valid_coins = {QUARTER : 0.25, DIME : 0.10, NICKEL : 0.5}
        self.accepted_coins = []
        self.rejected_coins = []
        self.returned_coins = []
        self.is_selected = None


    """Sets the selected product"""
    def select_product(self, product):
        
        self.is_selected = product

    """Displays based on current state of the system. Uses if elif statements to check if
    money has been inserted, if a selection has been made, and if enough money has been inserted.
    """
    
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
                self.is_selected = None
                return "THANK YOU"

            else:
                change = abs(self.products.get(self.is_selected) - sum(self.accepted_coins))
                change = round(change, 1)
                self.make_change(change)
                return "THANK YOU"
        
        
    def take_coins(self, coin):
        
        if coin in self.valid_coins:
            cost = self.products.get(self.is_selected)
            coin = self.valid_coins.get(coin)
            self.accepted_coins.append(coin)
            
        else:
            self.rejected_coins.append(coin)


    def make_change(self, change):
        while change > .05:
            change = change - .10
            self.returned_coins.append(DIME)
            
        while change > 0:
            change = change - .5
            self.returned_coins.append(NICKEL)

    def return_coins(self):
        for i in self.accepted_coins:
            if i == .25:
                self.returned_coins.append(QUARTER)
            elif i == .10:
                self.returned_coins.append(DIME)
            elif i == .05:
                self.returned_coins.append(NICKEL)
            else:
                return "ERROR"
        self.accepted_coins = []
        return self.returned_coins
        
            
        
        

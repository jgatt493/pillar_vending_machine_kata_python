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
    product_stock: dictionary of products mapped to their stock
    valid_coins: dictionary oof coins mapped to their values
    accpeted_coins: list for holding accepted coins
    rejecte_coins: list for holding rejected coins
    returned_coins: list of holding returned coins
    is_selected: variable used to store product selection
    """

    def __init__(self):
        
        self.products = {COLA : 1.00, CHIPS : .50, CANDY : .65}
        self.product_stock = {COLA : True, CHIPS : True, CANDY : True}
        self.valid_coins = {QUARTER : 0.25, DIME : 0.10, NICKEL : 0.5}
        self.accepted_coins = []
        self.rejected_coins = []
        self.returned_coins = []
        self.is_selected = None
        self.exact_change = False
        
        


    """Sets the selected product"""
    def select_product(self, product):
        if self.product_stock[product] == False:
            return "SOLD OUT"
        else:
            self.is_selected = product

    """Displays based on current state of the system. Uses if elif statements to check if
    money has been inserted, if a selection has been made, and if enough money has been inserted.
    """
    
    def display(self):

        """No selection has been made, no money has been inserted"""
        if len(self.accepted_coins) == 0 and self.is_selected == None:
            if self.exact_change == False:
                return "INSERT COINS"
            else:
                return "EXACT CHANGE ONLY"

        elif self.is_selected is None and len(self.accepted_coins) == None:
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
        
    """Takes one parameter coin, checks that coin is valid
    If valid, append to accepted coins
    If invalid, append to invalid coins
    """
    def take_coins(self, coin):
        
        if coin in self.valid_coins:
            cost = self.products.get(self.is_selected)
            coin = self.valid_coins.get(coin)
            self.accepted_coins.append(coin)
            
        else:
            self.rejected_coins.append(coin)


    """Takes one paramter change, that is the excess money inserted
    Returns proper change in the largest coins possible
    Appends coins to returned_coins
    """
    def make_change(self, change):
        while change > .05:
            change = change - .10
            self.returned_coins.append(DIME)
            
        while change > 0:
            change = change - .5
            self.returned_coins.append(NICKEL)
    """Returns coins when user presses return button
    Sorts through accepted coin list and appends them to returned_coins
    Had to add for loop to convert values back to coin names
    """
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
        
            
        
        

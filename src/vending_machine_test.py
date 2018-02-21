import unittest
import vending_machine
from vending_machine import VendingMachine


class VendingMachineTests(unittest.TestCase):

    def setUp(self):
        self.my_machine = VendingMachine()

    def test_when_machine_is_initialized_displays_INSERT_COINS(self):
        self.assertEqual(self.my_machine.display(),"INSERT COINS")

    def test_when_cola_is_selected_displays_PRICE_amount(self):
        self.my_machine.select_product(vending_machine.COLA)
        self.assertEqual(self.my_machine.display(),"PRICE 1.00")

    def test_when_chips_is_selected_displays_PRICE_amount(self):
        self.my_machine.select_product(vending_machine.CHIPS)
        self.assertEqual(self.my_machine.display(),"PRICE 0.50")

    def test_when_candy_is_selected_displays_PRICE_amount(self):
        self.my_machine.select_product(vending_machine.CANDY)
        self.assertEqual(self.my_machine.display(),"PRICE 0.65")

    def test_when_quarter_is_selected_price_is_updated(self):
        self.my_machine.select_product(vending_machine.COLA)
        self.my_machine.take_coins(vending_machine.QUARTER)
        self.assertEqual(self.my_machine.display(), "PRICE 0.75")

    def test_when_dime_is_entered_after_quarter_price_is_updated(self):
        self.my_machine.select_product(vending_machine.COLA)
        self.my_machine.take_coins(vending_machine.QUARTER)
        self.my_machine.take_coins(vending_machine.DIME)
        self.assertEqual(self.my_machine.display(), "PRICE 0.65")

    def test_when_invalid_coin_is_given_display_says_INVALID_COIN(self):
        self.my_machine.select_product(vending_machine.COLA)
        self.my_machine.take_coins(vending_machine.QUARTER)
        self.my_machine.take_coins(vending_machine.PENNY)
        self.assertEqual(self.my_machine.display(), "PRICE 0.75")
        

unittest.main()

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

    def test_when_exact_amount_is_given_display_says_THANK_YOU_and_product_is_dispensed(self):
        self.my_machine.select_product(vending_machine.COLA)
        self.my_machine.take_coins(vending_machine.QUARTER)
        self.my_machine.take_coins(vending_machine.QUARTER)
        self.my_machine.take_coins(vending_machine.QUARTER)
        self.my_machine.take_coins(vending_machine.QUARTER)
        self.assertEqual(self.my_machine.display(), "THANK YOU")
        self.assertEqual(self.my_machine.is_selected, None)

    def test_return_change_when_more_money_than_needed_is_inserted(self):
        self.my_machine.select_product(vending_machine.COLA)
        self.my_machine.take_coins(vending_machine.QUARTER)
        self.my_machine.take_coins(vending_machine.QUARTER)
        self.my_machine.take_coins(vending_machine.QUARTER)
        self.my_machine.take_coins(vending_machine.DIME)
        self.my_machine.take_coins(vending_machine.DIME)
        self.my_machine.take_coins(vending_machine.QUARTER)
        self.assertEqual(self.my_machine.display(), "THANK YOU")
        self.assertEqual(self.my_machine.returned_coins,['dime', 'dime'])

    def test_return_coins_when_customer_selects_return_coins(self):
        self.my_machine.select_product(vending_machine.COLA)
        self.my_machine.take_coins(vending_machine.QUARTER)
        self.my_machine.take_coins(vending_machine.DIME)
        self.my_machine.return_coins()
        self.assertEqual(self.my_machine.returned_coins,['quarter', 'dime'])

    def test_when_exact_change_is_required_display_shows_EXACT_CHANGE_ONLY(self):
        self.my_machine.exact_change = True
        self.assertEqual(self.my_machine.display(), "EXACT CHANGE ONLY")

unittest.main()

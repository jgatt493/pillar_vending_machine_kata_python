import unittest
import vending_machine
from vending_machine import VendingMachine


class VendingMachineTests(unittest.TestCase):

    def setUp(self):
        self.my_machine = VendingMachine()

    def test_when_machine_is_initialized_displays_INSERT_COINS(self):
        self.assertEqual(self.my_machine.display(),"INSERT COINS")

    def test_when_cola_is_selected_displays_PRICE_amount(self):
        self.assertEqual(self.my_machine.display(),"PRICE 1.00")

unittest.main()

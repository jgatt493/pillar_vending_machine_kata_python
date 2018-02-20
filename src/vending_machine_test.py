import unittest
import vending_machine
from vending_machine import VendingMachine


class VendingMachineTests(unittest.TestCase):

    def setUp(self):
        self.my_machine = VendingMachine()

    def test_when_machine_is_initialized_it_says_INSERT_COINS(self):
        self.assertEqual(self.my_machine.display(),"INSERT COINS")




unittest.main()

import unittest
from soldiers import Soldier

class TestSoldier(unittest.TestCase):

  def setUp(self):
    self.new_soldier = Soldier("102030", "Private", "Karl", "3 Rifles", "Infantry")

  def tearDown(self):
    Soldier.soldier_list = []

if __name__ == '__main__':
  unittest.main()
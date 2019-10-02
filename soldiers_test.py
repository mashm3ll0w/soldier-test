import unittest
from soldiers import Soldier

class TestSoldier(unittest.TestCase):

  def setUp(self):
    self.new_soldier = Soldier("102030", "Private", "Karl", "3 Rifles", "Infantry")

  def tearDown(self):
    Soldier.soldiers_list = []

  def test_init(self):
    self.assertEqual(self.new_soldier.svc_num, "102030")
    self.assertEqual(self.new_soldier.rank, "Private")
    self.assertEqual(self.new_soldier.name, "Karl")
    self.assertEqual(self.new_soldier.unit, "3 Rifles")
    self.assertEqual(self.new_soldier.corps, "Infantry")

  def test_save_soldier(self):
    self.new_soldier.save_soldier()
  
  def test_save_multiple_soldiers(self):
    self.new_soldier.save_soldier()
    test_soldier = Soldier("201030", "Corporal", "Keys", "7 Rifles", "Combat Engineer")
    test_soldier.save_soldier()

    self.assertEqual(len(Soldier.soldiers_list), 2)

  def test_delete_soldier(self):
    self.new_soldier.save_soldier()
    test_soldier = Soldier("201030", "Corporal", "Keys", "7 Rifles", "Combat Engineer")
    test_soldier.save_soldier()
    self.new_soldier.delete_soldier()

    self.assertEqual(len(Soldier.soldiers_list), 1)

if __name__ == '__main__':
  unittest.main()
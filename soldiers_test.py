import unittest
from soldiers import Soldier
import pyperclip

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

  def test_list_all_soldiers(self):
    self.assertEqual(Soldier.soldiers_list, Soldier.display_soldiers())

  def test_soldier_exists(self):
    self.new_soldier.save_soldier()
    found_soldier = Soldier.check_if_exists("102030")

    self.assertTrue(found_soldier)

  def test_find_soldier_by_svcNum(self):
    self.new_soldier.save_soldier()
    test_soldier = Soldier("201030", "Corporal", "Keys", "7 Rifles", "Combat Engineer")
    test_soldier.save_soldier()

    found_soldier = Soldier.find_by_svcNumber("201030")
    self.assertEqual(found_soldier.svc_num, test_soldier.svc_num)

  def test_find_by_rank(self):
    self.new_soldier.save_soldier()
    test_soldier = Soldier("201030", "Corporal", "Keys", "7 Rifles", "Combat Engineer")
    test_soldier.save_soldier()

    found_soldier = Soldier.find_by_rank("Corporal")
    self.assertEqual(found_soldier.rank, test_soldier.rank)

  def test_find_by_name(self):
    self.new_soldier.save_soldier()
    test_soldier = Soldier("201030", "Corporal", "Keys", "7 Rifles", "Combat Engineer")
    test_soldier.save_soldier()

    found_soldier = Soldier.find_by_name("Keys")
    self.assertEqual(found_soldier.name, test_soldier.name)

  def test_find_by_unit(self):
    self.new_soldier.save_soldier()
    test_soldier = Soldier("201030", "Corporal", "Keys", "7 Rifles", "Combat Engineer")
    test_soldier.save_soldier()

    found_soldier = Soldier.find_by_unit("7 Rifles")
    self.assertEqual(found_soldier.unit, test_soldier.unit)

  def test_find_soldier_by_corps(self):
    self.new_soldier.save_soldier()
    test_soldier = Soldier("201030", "Corporal", "Keys", "7 Rifles", "Gunner")
    test_soldier.save_soldier()

    found_soldier = Soldier.find_by_corps("Gunner")
    self.assertEqual(found_soldier.corps, test_soldier.corps)

  def test_copy_svcNumber(self):
    self.new_soldier.save_soldier()
    Soldier.copy_svcNumber("102030")

    self.assertEqual(self.new_soldier.svc_num, pyperclip.paste())

if __name__ == '__main__':
  unittest.main()
class Soldier:

  soldiers_list = []

  def save_soldier(self):
    Soldier.soldiers_list.append(self)

  def delete_soldier(self):
    Soldier.soldiers_list.remove(self)

  @classmethod
  def display_soldiers(cls):
    return cls.soldiers_list

  @classmethod
  def check_if_exists(cls, number):
    for soldier in cls.soldiers_list:
      if soldier.svc_num == number:
        return True

  @classmethod
  def find_by_svcNumber(cls, number):
    for soldier in cls.soldiers_list:
      if soldier.svc_num == number:
        return soldier

  @classmethod
  def find_by_rank(cls, number):
    for soldier in cls.soldiers_list:
      if soldier.rank == number:
        return soldier

  def __init__(self, svc_num, rank, name, unit, corps):
    self.svc_num = svc_num
    self.rank = rank
    self.name = name
    self.unit = unit
    self.corps = corps
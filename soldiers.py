class Soldier:

  soldiers_list = []

  def save_soldier(self):
    Soldier.soldiers_list.append(self)

  def delete_soldier(self):
    Soldier.soldiers_list.remove(self)

  def __init__(self, svc_num, rank, name, unit, corps):
    self.svc_num = svc_num
    self.rank = rank
    self.name = name
    self.unit = unit
    self.corps = corps
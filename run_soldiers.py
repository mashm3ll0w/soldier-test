#!/usr/bin/env python3

from soldiers import Soldier

def create_soldier(svc_num, rank, name, unit, corps):
  new_soldier = Soldier(svc_num, rank, name, unit, corps)

  return new_soldier

def save_soldiers(soldier):
  Soldier.save_soldier()

def list_soldiers():
  return Soldier.display_soldiers()

def remove_soldier(soldier):
  return Soldier.delete_soldier()

def find_soldier(number):
  return Soldier.find_by_svcNumber(number)

def check_soldier_exists(number):
  return Soldier.check_if_exists(number)

def copy_soldier_svcNumber(number):
  return Soldier.copy_svcNumber(number)


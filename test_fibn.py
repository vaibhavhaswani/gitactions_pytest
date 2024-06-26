from fibn import fibn
import pytest


def test_1():
  assert fibn(3,5)==[2, 3, 5, 8, 13]

def test_2():
  assert fibn(0,3)==[0,1,1]

# def test_2():
#   assert fibn(0,0)==None

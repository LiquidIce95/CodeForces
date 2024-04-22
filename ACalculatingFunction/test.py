from unittest import TestCase,main
from ACalculatingFunction import computeFunction


class TestSuite(TestCase):
  def test1(self):
    assert computeFunction(1) == -1

  def test2(self):
     assert computeFunction(2) == 1

  def test3(self):
     assert computeFunction(3) == -2

  def test4(self):
     assert computeFunction(4) == 2

  def test5(self):
     assert computeFunction(5) == -3

  def test6(self):
     assert computeFunction(6) == 3

  def test7(self):
     assert computeFunction(7) == -4
    
  def test8(self):
     assert computeFunction(8) == 4


if __name__ == '__main__':
    main()
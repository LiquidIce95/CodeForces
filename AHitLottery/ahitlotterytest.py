from unittest import TestCase,main
from ahitlottery3 import computeMinimalBills


class TestSuite(TestCase):
  def test1(self):
    n=1
    self.assertEqual(computeMinimalBills(4,n),1)

  def test2(self):
    n=4
    self.assertEqual(computeMinimalBills(4,n),4)

  def test3(self):
    n=5
    self.assertEqual(computeMinimalBills(4,n),1)

  def test4(self):
    n=20
    self.assertEqual(computeMinimalBills(4,n),1)

  def test5(self):
    n=25
    self.assertEqual(computeMinimalBills(4,n),2)

  def test6(self):
    n=101
    self.assertEqual(computeMinimalBills(4,n),2)

  def test7(self):
    n=30
    self.assertEqual(computeMinimalBills(4,n),2)

  


if __name__ == '__main__':
    main()
from unittest import TestCase,main
from bDrinks import computeAverage


class TestSuite(TestCase):
  def test1(self):
    l= [50,50]
    n = 2
    assert computeAverage(n,l) == 50

  def test2(self):
    l= [33.33333,33.33333,33.33333]
    n = 3
    self.assertAlmostEqual(computeAverage(n,l),33.333333,delta=10**(-4))

  def test3(self):
    l= [1,24,50]
    n = 3
    self.assertAlmostEqual(computeAverage(n,l),25,delta=10**(-4))

  def test4(self):
    l=[50,50,100]
    n=3
    self.assertAlmostEqual(computeAverage(n,l),66.666666666667,delta=10**(-4))

  def test5(self):
    l=[0,25,50,75]
    n = 4
    self.assertAlmostEqual(computeAverage(n,l),37.500000000000,delta=10**(-4))



  


if __name__ == '__main__':
    main()
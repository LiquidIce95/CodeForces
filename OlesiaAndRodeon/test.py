from unittest import TestCase,main
from olesiaAndRodeon import *


class TestSuite(TestCase):
  def testSingleDigit1(self):
    n = 1
    t = 2

    expcected = 2
    result = findNum(n,t)
    self.assertEqual(result,expcected)

  def testSingleDigit2(self):
    n = 1
    t = 6

    expcected = 6
    result = findNum(n,t)
    self.assertEqual(result,expcected)

  def testSingleDigit3(self):
    n = 3
    t = 2

    expcected = 222
    result = findNum(n,t)
    self.assertEqual(result,expcected)


  def testNoNum(self):
    n = 1
    t = 10

    expcected = -1
    result = findNum(n,t)
    self.assertEqual(result,expcected)

  def testDoubleDigit(self):
    n = 2
    t = 10

    expcected = 10
    result = findNum(n,t)
    self.assertEqual(result,expcected)


  def testDoubleDigit2(self):
    n = 4
    t = 10

    expcected = 1110
    result = findNum(n,t)
    self.assertEqual(result,expcected)



if __name__ == '__main__':
    main()
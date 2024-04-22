from unittest import TestCase,main
from theatreSquare import *


class TestSuite(TestCase):
  def test1(self):
    n = 2
    m = 2
    a = 2

    expcected = 1
    result = computeMinFlagstones(n,m,a)
    self.assertEqual(result,expcected)
 
  def test2(self):
    n = 4
    m = 4
    a = 2

    expcected = 4
    result = computeMinFlagstones(n,m,a)
    self.assertEqual(result,expcected)

  def test3(self):
    n = 2
    m = 3
    a = 2

    expcected = 2
    result = computeMinFlagstones(n,m,a)
    self.assertEqual(result,expcected)

  def test4(self):
    n = 6
    m = 6
    a = 4

    expcected = 4
    result = computeMinFlagstones(n,m,a)
    self.assertEqual(result,expcected)


if __name__ == '__main__':
    main()
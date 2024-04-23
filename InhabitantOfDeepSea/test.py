from unittest import TestCase,main
from inhabitantOfDeepSea import *


class TestSuite(TestCase):
  def testSingleShip1(self):
    numShips = 1
    numAttacks = 1
    shipsLife = [2]
    actual = computeSurv([numShips,numAttacks],shipsLife)
    expected = 1
    self.assertEqual(expected,actual)

  def testSingleShip2(self):
    numShips = 1
    numAttacks = 2
    shipsLife = [2]
    actual = computeSurv([numShips,numAttacks],shipsLife)
    expected = 0
    self.assertEqual(expected,actual)

  def testSingleShipNoAttack(self):
    numShips = 1
    numAttacks = 0
    shipsLife = [2]
    actual = computeSurv([numShips,numAttacks],shipsLife)
    expected = 1
    self.assertEqual(expected,actual)

  def testNoAttack1(self):
    numShips = 3
    numAttacks = 0
    shipsLife = [2,1,10]
    actual = computeSurv([numShips,numAttacks],shipsLife)
    expected = 3
    self.assertEqual(expected,actual)

  def testDestryoedFirst(self):
    numShips = 3
    numAttacks = 3
    shipsLife = [2,1,10]
    actual = computeSurv([numShips,numAttacks],shipsLife)
    expected = 2
    self.assertEqual(expected,actual)
  
  def testDestryoedFirst2(self):
    numShips = 3
    numAttacks = 12
    shipsLife = [2,16,10]
    actual = computeSurv([numShips,numAttacks],shipsLife)
    expected = 2
    self.assertEqual(expected,actual)

  def testDestryoedFirst3(self):
    numShips = 3
    numAttacks = 12
    shipsLife = [2,16,6]
    actual = computeSurv([numShips,numAttacks],shipsLife)
    expected = 2
    self.assertEqual(expected,actual)

  def testDestryoedFirstAndLast(self):
    numShips = 3
    numAttacks = 14
    shipsLife = [2,16,6]
    actual = computeSurv([numShips,numAttacks],shipsLife)
    expected = 1
    self.assertEqual(expected,actual)

  def testCodeforces1(self):
    numShips = 4
    numAttacks = 5
    shipsLife = [1,2,4,3]
    actual = computeSunk([numShips,numAttacks],shipsLife)
    expected = 2
    self.assertEqual(expected,actual)

  def testCodeforces2(self):
    numShips = 4
    numAttacks = 6
    shipsLife = [1,2,4,3]
    actual = computeSunk([numShips,numAttacks],shipsLife)
    expected = 3
    self.assertEqual(expected,actual)

  def testCodeforces3(self):
    numShips = 5
    numAttacks = 20
    shipsLife = [2,7,1,8,2]
    actual = computeSunk([numShips,numAttacks],shipsLife)
    expected = 5
    self.assertEqual(expected,actual)

  def testCodeforces4(self):
    numShips = 2
    numAttacks = 2
    shipsLife = [3,2]
    actual = computeSunk([numShips,numAttacks],shipsLife)
    expected = 0
    self.assertEqual(expected,actual)

  def testCodeforces5(self):
    numShips = 2
    numAttacks = 15
    shipsLife = [1,5]
    actual = computeSunk([numShips,numAttacks],shipsLife)
    expected = 2
    self.assertEqual(expected,actual)
  
  def testCodeforces6(self):
    numShips = 2
    numAttacks = 7
    shipsLife = [5,2]
    actual = computeSunk([numShips,numAttacks],shipsLife)
    expected = 2
    self.assertEqual(expected,actual)
  



if __name__ == '__main__':
    main()
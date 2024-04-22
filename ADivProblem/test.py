from unittest import TestCase,main
from aDivProblem import computeOutput


class TestSuite(TestCase):
  def test1(self):
    l= [
      [50,50]
    ]
    assert computeOutput(l) == [0]

  def test2(self):
    l = [
      [33,40],
      [1,2]
    ]
    
    solution = [
      7,
      1
    ]
    assert computeOutput(l) == solution


  def test3(self):
    l = [
      [3,6],
      [1,5],
      [90,290]
    ]
    
    solution = [
      3,
      4,
      200
    ]
    assert computeOutput(l) == solution

  



  


if __name__ == '__main__':
    main()
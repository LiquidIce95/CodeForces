import sys

def computeAverage(N:int,l:list)->float:
  return sum(l)/N 
  

if __name__ == "__main__":
  numberOfDrinks = int(sys.stdin.readline())
  percentages = list(map(int,sys.stdin.readline().split()))


  output = computeAverage(numberOfDrinks,percentages)
  sys.stdout.writelines(str(output))


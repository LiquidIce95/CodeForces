import sys

def computeMax(descr:list,a:list)->int:
  """
  @k list containing length of array and number of operations
  @a the array
  """
  leng = descr[0]
  k = descr[k]

  
  return 0
  

if __name__ == "__main__":
  numberOftests = int(sys.stdin.readline())

  for _ in range(numberOftests):
    testDescr = list(map(int,sys.stdin.readline().split()))
    array = list(map(int,sys.stdin.readline().split()))
    output = computeMax(testDescr,array)
    sys.stdout.writelines(str(output))



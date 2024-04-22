import sys

def computeSteps(a:int,b:int)->int:
  remainder = a%b
  if remainder == 0 : return 0
  else : return b-remainder

def computeOutput(Tests:list)->list:
  output = []
  for test in Tests:
    output.append(computeSteps(test[0],test[1]))
  return output
  

if __name__ == "__main__":
  numberOfTests = int(sys.stdin.readline())
  listOfTests = []

  for t in range(numberOfTests):
    test = list(map(int,sys.stdin.readline().split()))
    listOfTests.append(test)


  output = computeOutput(listOfTests)

  for result in output:
    sys.stdout.writelines(str(result)+"\n")

  

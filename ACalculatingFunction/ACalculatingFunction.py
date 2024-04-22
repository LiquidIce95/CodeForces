import sys

def computeFunction(n:int)->int:
  
  if (n%2) == 0: return n/2

  else : return (n+1)/(-2)

if __name__ == "__main__":
  input = sys.stdin.readline()
  output = computeFunction(int(input))
  sys.stdout.writelines(str(int(output)))


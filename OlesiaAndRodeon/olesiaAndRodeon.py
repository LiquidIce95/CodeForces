import sys

def findNum(n:int,t:int)->int:

  if t < 10:
    num = ""
    for j in range(n):
      num+= f"{t}"
    return int(num)
  
  else:
    if n ==1: return -1
    num =""
    for j in range(n-1):
      num+="1"

    num+= "0"
    return int(num)

if __name__ == "__main__":
  [n,t] = list(map(int,sys.stdin.readline().split()))


  output = findNum(n,t)
  sys.stdout.writelines(str(output))


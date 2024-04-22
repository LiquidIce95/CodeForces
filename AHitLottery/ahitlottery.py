import sys

def case1(dpmatrix :list,row:int,bankacc:int)->None:
  dpmatrix[row][bankacc-1] = dpmatrix[row-1][bankacc-1]

def case2(dpmatrix :list,row:int,bankacc:int,Bills:list)->None:
  Quotient = bankacc//Bills[row]
  withdraw = Quotient*Bills[row]
  if bankacc != withdraw: dpmatrix[row][bankacc-1] = Quotient + dpmatrix[row][bankacc-1-withdraw]
  else : dpmatrix[row][bankacc-1] = Quotient

def prepareDP(DP:list,n:int,N:int)->None:

  DP.append([k for k in range(1,n+1)])

  for j in range(1,N):
    DP.append([0 for k in range(n)])  

def makeEntry(DP:list,row:int,bankAcc:int,Bills:list,n:int)->None:
  if bankAcc<Bills[row]:
    case1(DP,row,bankAcc)
  else:
    case2(DP,row,bankAcc,Bills)

def computeMinimalBills(n:int)->int:
  Bills = [1,5,10,20,100]
  N = len(Bills)
  DP = []

  prepareDP(DP,n,N)

  for j in range(1,N):
    for k in range(1,n+1):
      makeEntry(DP,j,k,Bills,n)
  return DP[4][n-1]



if __name__ == "__main__":
  bankAccount = int(sys.stdin.readline())

  output = computeMinimalBills(bankAccount)

  sys.stdout.writelines(str(output))

  

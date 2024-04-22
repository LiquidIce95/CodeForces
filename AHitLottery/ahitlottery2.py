import sys

def case1(dpmatrix :list,row:int,bankacc:int)->None:
  dpmatrix[row][bankacc-1] = dpmatrix[row-1][bankacc-1]

def case2(dpmatrix :list,row:int,billind:int,bankacc:int,Bills:list)->None:
  Quotient = bankacc//Bills[billind]
  withdraw = Quotient*Bills[billind]
  if bankacc != withdraw: dpmatrix[row][bankacc-1] = Quotient + dpmatrix[row][bankacc-1-withdraw]
  else : dpmatrix[row][bankacc-1] = Quotient

def prepareDP(DP:list,n:int,N:int)->None:
  DP.append([k for k in range(1,n+1)])

def makeEntry(DP:list,row:int,billInd:int,bankAcc:int,Bills:list,n:int)->None:
  if bankAcc<Bills[billInd]:
    case1(DP,row,bankAcc)
  else:
    case2(DP,row,billInd,bankAcc,Bills)

def addRow(DP,n:int):
  DP.append([0 for k in range(n)])

def computeMinimalBills(n:int)->int:
  Bills = [1,5,10,20,100]
  N = len(Bills)
  DP = []

  prepareDP(DP,n,N)

  for j in range(1,N):
    addRow(DP,n)
    for k in range(1,n+1):
      makeEntry(DP,1,j,k,Bills,n)
    del DP[0]
  return DP[0][n-1]



if __name__ == "__main__":
  bankAccount = int(sys.stdin.readline())

  output = computeMinimalBills(bankAccount)

  sys.stdout.writelines(str(output))

  

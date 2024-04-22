import sys

Bills = [1,5,10,20,100]



def computeMinimalBills(billInd:int,bankAcc:int)->int:
  if billInd == 0:
    return bankAcc

  if bankAcc<Bills[billInd]:
    return computeMinimalBills(billInd-1,bankAcc)
  else:
    Quotient = bankAcc//Bills[billInd]
    withdraw = Quotient*Bills[billInd]

    if bankAcc != withdraw: 
      return  Quotient + computeMinimalBills(billInd,bankAcc-withdraw)
    else : 
      return Quotient
    





if __name__ == "__main__":
  bankAccount = int(sys.stdin.readline())

  output = computeMinimalBills(4,bankAccount)

  sys.stdout.writelines(str(output))

  

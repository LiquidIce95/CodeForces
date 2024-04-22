import sys


def computeSurv(descr:list,a:list)->int:
    """
    @k number of attacks of kraken
    @a list of durability of sips
    returns the number of surviving ships
    """
    numShips = descr[0]
    numAttack = descr[1]
    """which side is being attacked"""
    side = 0
    l=0
    r=-1

    while(numShips >0 and numAttack > 0):
        firstShip = a[l]
        lastShip = a[r]

        if(firstShip > lastShip and side == 0):
           firstCase(l,r,side,firstShip,lastShip,numAttack)    
        elif(firstShip > lastShip and side == 1):
           secondCase(l,r,side,firstShip,lastShip,numAttack)
        elif(firstShip < lastShip and side == 0):
            thirdCase(l,r,side,firstShip,lastShip,numAttack)
        elif(firstShip < lastShip and side == 1):
            fourthCase(l,r,side,firstShip,lastShip,numAttack)
        elif(firstShip == lastShip and side == 0):
            fifthCase(l,r,side,firstShip,lastShip,numAttack)
        elif(firstShip == lastShip and side == 1):
            sixthCase(l,r,side,firstShip,lastShip,numAttack)

    return (numShips+r)-l + 1
  


def firstCase(l:int,r:int,side:int,firstShip,lastShip,numAttack):
    """firstShip > lastShip and side == 0"""
    if numAttack < lastShip*2: k=0; return None;
    k -= lastShip*2
    firstShip -= lastShip
    r -= 1

def secondCase(l:int,r:int,side:int,firstShip,lastShip,numAttack):
    """firstShip > lastShip and side == 1"""
    if numAttack < lastShip*2-1: numAttack=0; return None;
    k-= lastShip*2-1
    firstShip -= lastShip-1
    r -= 1


def thirdCase(l:int,r:int,side:int,firstShip,lastShip,numAttack):
    """firstShip < lastShip and side == 0"""
    if numAttack < firstShip*2-1: numAttack=0;return None;
    k-= firstShip*2-1
    lastShip -= firstShip-1
    l += 1
    pass

def fourthCase(l:int,r:int,side:int,firstShip,lastShip,numAttack):
    """firstShip < lastShip and side == 1"""
    if numAttack < firstShip*2: k=0;return None;
    k -= firstShip*2
    lastShip -= firstShip
    l += 1

def fifthCase(l:int,r:int,side:int,firstShip,lastShip,numAttack):
    """firstShip == lastShip and side == 0"""
    if numAttack < firstShip*2-1: k=0;return None;
    k -= firstShip*2-1
    lastShip -= firstShip-1
    l+=1


def sixthCase(l:int,r:int,side:int,firstShip,lastShip,numAttack):
    """firstShip == lastShip and side == 1"""
    if numAttack < lastShip*2-1: k=0; return None;
    k-= lastShip*2-1
    firstShip -= lastShip-1
    r-=1


if __name__ == "__main__":
  numberOftests = int(sys.stdin.readline())

  for _ in range(numberOftests):
    testDescr = list(map(int,sys.stdin.readline().split()))
    array = list(map(int,sys.stdin.readline().split()))
    output = computeSurv(testDescr,array)
    sys.stdout.writelines(str(output))



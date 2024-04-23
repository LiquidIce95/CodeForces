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
    r= numShips-1

    if(l == r and numAttack < a[l]):
        return 1
    elif(l == r and numAttack >= a[l]):
        return 0

    while(numShips >0 and numAttack > 0):

        if(l == r and numAttack < a[l]):
            return 1
        elif(l == r and numAttack >= a[l]):
            return 0


        firstShip = a[l]
        lastShip = a[r]

        if(firstShip > lastShip and side == 0):
           numAttack,firstShip,r = firstCase(l,r,side,firstShip,lastShip,numAttack)    
        elif(firstShip > lastShip and side == 1):
           numAttack,firstShip,r = secondCase(l,r,side,firstShip,lastShip,numAttack)
        elif(firstShip < lastShip and side == 0):
            numAttack,lastShip,l = thirdCase(l,r,side,firstShip,lastShip,numAttack)
        elif(firstShip < lastShip and side == 1):
            numAttack,lastShip,l = fourthCase(l,r,side,firstShip,lastShip,numAttack)
        elif(firstShip == lastShip and side == 0):
            numAttack,lastShip,l = fifthCase(l,r,side,firstShip,lastShip,numAttack)
        elif(firstShip == lastShip and side == 1):
            numAttack,firstShip,r = sixthCase(l,r,side,firstShip,lastShip,numAttack)

        side = 1 - side 
        numShips = (numShips+r)-l + 1

    return r-l+1
  


def firstCase(l:int,r:int,side:int,firstShip,lastShip,numAttack):
    """firstShip > lastShip and side == 0"""
    if numAttack < lastShip*2: numAttack=0; return numAttack,firstShip,r;
    numAttack -= lastShip*2
    firstShip -= lastShip
    r -= 1
    return numAttack,firstShip,r

def secondCase(l:int,r:int,side:int,firstShip,lastShip,numAttack):
    """firstShip > lastShip and side == 1"""
    if numAttack < lastShip*2-1: numAttack=0; return numAttack,firstShip,r;
    numAttack-= lastShip*2-1
    firstShip -= lastShip-1
    r -= 1
    return numAttack,firstShip,r


def thirdCase(l:int,r:int,side:int,firstShip,lastShip,numAttack):
    """firstShip < lastShip and side == 0"""
    if numAttack < firstShip*2-1: numAttack=0;return numAttack,lastShip,l;
    numAttack-= firstShip*2-1
    lastShip -= firstShip-1
    l += 1
    return numAttack,lastShip,l

def fourthCase(l:int,r:int,side:int,firstShip,lastShip,numAttack):
    """firstShip < lastShip and side == 1"""
    if numAttack < firstShip*2: numAttack=0;return numAttack,lastShip,l;
    numAttack -= firstShip*2
    lastShip -= firstShip
    l += 1
    return numAttack,lastShip,l

def fifthCase(l:int,r:int,side:int,firstShip,lastShip,numAttack):
    """firstShip == lastShip and side == 0"""
    if numAttack < firstShip*2-1: k=0;return numAttack,lastShip,l;
    numAttack -= firstShip*2-1
    lastShip -= firstShip-1
    l+=1
    return numAttack,lastShip,l


def sixthCase(l:int,r:int,side:int,firstShip,lastShip,numAttack):
    """firstShip == lastShip and side == 1"""
    if numAttack < lastShip*2-1: numAttack=0; return numAttack,firstShip,r;
    numAttack-= lastShip*2-1
    firstShip -= lastShip-1
    r-=1
    return numAttack,firstShip,r


if __name__ == "__main__":
  numberOftests = int(sys.stdin.readline())

  for _ in range(numberOftests):
    testDescr = list(map(int,sys.stdin.readline().split()))
    array = list(map(int,sys.stdin.readline().split()))
    output = computeSurv(testDescr,array)
    sys.stdout.writelines(str(output))



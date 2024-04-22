import sys

def computeMinFlagstones(length:int,height:int,flagStn:int)->float:

  if length < flagStn and height < flagStn: return 1

  if length < flagStn: 
    rem = height% flagStn
    quot = height//flagStn
    if rem == 0 : return quot
    else : return quot+1

  if height < flagStn:
    rem = length%flagStn
    quot = length//flagStn
    if rem == 0: return quot
    else : return quot+1
  
  hQuant = length//flagStn
  lQuant = height//flagStn

  innterFlgStn = hQuant*lQuant


  flagStnArea = flagStn**2
  rectArea = length*height
  
  minFlagStns = 0


  lengthRemainder = length%flagStn
  heightRemainder = height%flagStn

  coverLength = length - lengthRemainder
  coverHeight = height - heightRemainder

  if lengthRemainder != 0: minFlagStns += coverHeight//flagStn
  if heightRemainder != 0: minFlagStns += coverLength//flagStn

  if lengthRemainder != 0 != heightRemainder : minFlagStns += 1

  return innterFlgStn+minFlagStns
  

if __name__ == "__main__":
  [n,m,a] = list(map(int,sys.stdin.readline().split()))


  output = computeMinFlagstones(n,m,a)
  sys.stdout.writelines(str(output))


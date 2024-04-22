from sys import stdin,stdout

def solver(a:str,b:str)->int:
  if len(a) != len(b): return max(len(a),len(b))

  else:
    if a==b: return -1

    else: return len(a)
  

if __name__ == "__main__":
  a = stdin.readline().strip()
  b = stdin.readline().strip()

  output = solver(a,b)
  stdout.writelines(str(output))


Matriz = int(input("Tu matriz es de 2 o 3 incognitas?"))
if Matriz == 3:
  print('Ingresa los valores de la ecuacion separados por un espacio')
  print('Ecuacion 1')
  A = [ float(x) for x in input().split()]
  print('Ecuacion 2')
  B = [ float(x) for x in input().split()]
  print('Ecuacion 3')
  C = [ float(x) for x in input().split()]
  D = ((A[0]*B[1]*C[2])+(A[1]*B[2]*C[0])+(A[2]*B[0]*C[1]))-((C[0]*B[1]*A[2])+(C[1]*B[2]*A[0])+(C[2]*B[0]*A[1]))

  iA = ((A[3]*B[1]*C[2])+(A[1]*B[2]*C[3])+(A[2]*B[3]*C[1])+(C[3]*B[1]*A[2])+(C[1]*B[2]*A[3])+(C[2]*B[3]*A[1]))/D
  iB = ((A[0]*B[3]*C[2])+(A[3]*B[2]*C[0])+(A[2]*B[0]*C[3])+(C[0]*B[3]*A[2])+(C[3]*B[2]*A[0])+(C[2]*B[0]*A[3]))/D
  iC = ((A[0]*B[1]*C[3])+(A[1]*B[3]*C[0])+(A[3]*B[0]*C[1])+(C[0]*B[1]*A[3])+(C[1]*B[3]*A[0])+(C[3]*B[0]*A[1]))/D
  print(f"iA = {iA}")
  print(f"iB = {iB}")
  print(f"iC = {iC}")
else:
  print('Ingresa los valores de la ecuacion separados por un espacio')
  print('Ecuacion 1')
  A = [ float(x) for x in input().split()]
  print('Ecuacion 2')
  B = [ float(x) for x in input().split()]
  D = (B[0]*A[1]) - (A[0]*B[1])
  iA = ((A[1]*B[2]) - (B[1]*A[2]))/D
  iB = ((B[0]*A[2]) - (A[0]*B[2]))/D
  print(f"iA = {iA}")
  print(f"iB = {iB}")

'''All our inputs to create a matrix'''
'''for loop to create a matrix using empty list and appending to that list'''
def main():
  M = int(input("Enter your rows: "))
  N = int(input("Enter your colums: "))
  A = []
  B = []
  for i in range (M):
    row = []
    for c in range (N):
      row.append(float(input(f" Enter your values for A: [ {i} , {c} ] ")))
    A.append(row)
    
  for i in range (M):
    row = []
    for c in range (N):
      row.append(float(input(f" Enter your values for B: [ {i} , {c} ] ")))
    B.append(row)
    #'''Multiplication formula of two matrices'''
  
  def multi(Ax,Bx):
    C = []
    for i in range(len(Ax)):
      C.append([])
      for j in range(len(Bx[0])):
         tmp = 0
         for k in range(len(Bx)):
           tmp += Ax[i][k] * Bx[k][j]
         C[-1].append(tmp)
    return C 
  Multiplication_results = multi(A,B)
  print(Multiplication_results)
    #Ax = [[10,20],[30,40],[50,60]]
    #Bx = [[1,2,3,4],[5,6,7,8]]
  print(multi(A,B))  
  def confirminverse(C):
    Results = True
    for i in range(len(C)):
        for j in range(len(C[0])):
         if i == j:
           if C[i][j] == 1: 
             Results = True
           else :  
             Results = False
             return Results
         else :
          if C[i][j] == 0:
            Results = True
          else :
            Results = False
            return Results
    return Results
  Results = confirminverse(Multiplication_results) 
  if Results is True:
      print("The two Matrixes are inverses of each other ")
  else: 
      print("The two Matrices are Not inverses of each other")
  print(f" Matrix A: {A}")
  print(f" Matrix B: {B}")
main()


#Ax = [[10,20],[30,40],[50,60]]
#Bx = [[1,2,3,4],[5,6,7,8]]
#print(multi(A,B))

#def confirminverse(A,B):
 # if len(Ax[0]) != len(Bx):

#if confirminverse(Ax, Bx):
 #   print("Matrices A and B are inverses of each other.")
  #else:
   # print("Matrices A and B are not inverses of each other.")







  #A = [[5,6], [10,12]]
  #B = [[2,3], [4,8]] 
  #if matrices(A) == 0 or matrices(B) == 0:
    #print("The matrices cannot be inversed.")
    #return

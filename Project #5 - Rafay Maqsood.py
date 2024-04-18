'''Cominations function'''
def comb(k, n):
  ans = 1
  for i in range(k):
    ans *= (n - i) / (i + 1)
  return round(ans)
#n = int(input("Enter number to define n: "))
#k = int(input("Enter the number of elements out of n: "))
'''Creating Pascals Triangle'''
'''defining the rows and value'''
def Pascals_triangle(numberofrows): 
  P_triangle=[]
  for row_num in range(numberofrows): 
    row = []
    for element_colm in range(row_num + 1):
      '''Value being plugged back in to combinations formula'''
      value= comb(element_colm, row_num)
      row.append(value)
    P_triangle.append(row)
    '''Printing the triangle and its formatting'''
    print(" ".join(str(value).center(3) for value in row).center(numberofrows * 6))
    '''All our inputs for user,front end of code'''
def main():
  '''While loop with break to tell code when to stop and check perameters'''
  while True:
    numberofrows = int(input("Please enter a number of rows between 4 to 8: "))
    if 4 <= numberofrows <= 8:
      Pascals_triangle(numberofrows)
      break
    else:
      print("Rows must be between 4 and 8, please enter value again: " )
    #Pascals_triangle(numberofrows)

main()
     
  
    

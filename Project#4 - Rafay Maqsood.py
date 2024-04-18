'''Computing Factorials'''
def f(n):
    result = 1
    for i in range(2, n+1):
      result = result *i
      '''printing the individual results for clarity'''
      #print (f"i = {i},result = {result}")
    return result
'''User inputing number of subsets for arrangements of multisets'''
def arrange_multiset(j, mj, n, k ):
  n = sum(mj)
  divisor = 1
  for mi in mj:
    divisor *=f(mi)
    #print(f' mi {mi}, divisor {divisor}' )
  z = f(n-k)
#Print statements to check if the math is correct
  #print (z)
  #print(f(n) // divisor)
  #print(f(n) // (z)*divisor)
  #print(f(n)*divisor // (z))
  #print(divisor)
  #print((z)*divisor)
  x = (z)*divisor
  #print (f(n) // x)
  return f(n) // x
'''User inputing number of subsets for permutations of multisets'''
j=0
while j<3:
    j = int(input("Enter the number of subsets (no smaller than 3, no greater than 8): "))
while j>8:
    j = int(input("Enter the number of subsets (no smaller than 3, no greater than 8): "))
mj = []
while len(mj)<1:
  mj = [int(input("What is the size of this subset? (from 1 to 5): ")) for _ in range(j)]
while len(mj)>5:
  mj = [int(input("What is the size of this subset? (from 1 to 5): ")) for _ in range(j)]
n = sum(mj)
k = int(input("What is the total number of the arragements? "
 "(Enter a number smaller than the total number of the subsets -n): "))
print(f" Given your inputs, the number of arrangements is {arrange_multiset(j, mj, n, k)}")

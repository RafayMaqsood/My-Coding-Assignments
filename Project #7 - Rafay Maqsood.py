#def Probability(K,N): P(x)= 1/b-a for a <= x <= b
                   #   P(x)= 0 for x < a or x > b 
def winning_big_lottery_probability():
    n = int(input("Enter the total number of possibilities (n): "))
    k = int(input("Enter the number of possibilities you are choosing (k): "))
    result = 1.0
    # Calculate the product of n, n-1, ..., n-k+1
    for i in range(n, n-k, -1):
        result *= i
    # Divide by the product of k, k-1, ..., 1
    for i in range(k, 0, -1):
        result /= i
    r=(((n-k))*(k)/result)
    print(f"The probability of winning the big lottery is {1/result}")
    print(f"The probability of winning(little)k-1 drawn numbers: {r} ")
  #while loop to account for negative whole numbers
    while n >= k and n > 0 and k > 0:
        break
    else:
      print("Invalid input, please enter positive integers with n >= k.")
      n = int(input("Enter the total number of possibilities (n) again please: "))
      k = int(input("Enter the number of possibilities for (k) again please: "))
      for i in range(n, n-k, -1):
        result *= i
      # Divide by the product of k, k-1, ..., 1 again for negative whole number input
      for i in range(k, 0, -1):
        result /= i
      r=(((n-k))*(k)/result)
      print(f"The probability of winning the big lottery is {1/result}")
      print(f"The probability of winning(little)k-1 drawn numbers: {r} ")
      return
    return 1 / result
  
# Calculate the probability of winning a lottery
winning_big_lottery_probability()

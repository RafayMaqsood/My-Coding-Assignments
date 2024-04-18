def printGP():
    a = float(input("Enter the scale factor: "))
    r = float(input("Enter the ratio: "))
    
    if -1 < r < 1:
        print(f"This GP converges with infinite elements to {round(a / (1 - r), 7)}")
        print(f"the first terms are {a}, {a*r}, and {a*r*r}")
    else:
        n = eval(input("This GP does not converge to a finite number with infinite elements. Enter the number of elements n: "))
        gp_sum = a * (r**n - 1) / (r - 1)
        print(f"This GP sum with {n} elements is equal to {(gp_sum)}")
        first_elements = [] 
        for i in range(n):
          first_elements += [a * (r**i)]
        print(f"the first elements are {', '.join(map(str,first_elements[:3]))}")
printGP()
 

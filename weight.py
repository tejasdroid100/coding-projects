weight=float(input("Enter your weight"))
cond = input("if weight is in kilograms then type K or if in pounds type L")
if cond=="K":
    print("Your weight in lbs is: ",weight*2.2)
elif cond=="L":
    print("Your weight in kg is: ",weight*0.45)
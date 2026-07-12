weight=float(input("Enter the weight: "))
unit= input("Kilograms or Pounds(K or L):")
if unit == "K":
    weight=weight*2.205
    unit="Lbs."
    print(f"The Weight is {weight} {unit}")
elif unit == "L":
    weight=weight/2.205
    unit="Kgs."
    print(f"The Weight is {weight} {unit}")
else:
    print("Invalid!...")
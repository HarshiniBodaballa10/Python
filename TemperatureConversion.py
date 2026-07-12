unit=input("Is the temperature in Celisius or Fahrenheit(F or L)?:")
temp=float(input("Enter the temperature:"))
if unit=="C":
    temp=round((9 * temp) /5 + 32,1)
    print(f"The temperature is {temp} F")
elif unit=="F":
    temp = round((temp - 32) * 5, 1)
    print(f"The temperature is {temp} C")
else:
    print("Enter Valid unit... ")
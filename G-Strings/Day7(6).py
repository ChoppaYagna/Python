T=float(input("Enter Temperature:"))
U=input("Enter Units(K or F or C):").upper()

if U == "C":
    f = (T * 9/5) + 32
    k = T + 273.15
    print(f"Temperature in Fahrenheit: {f}F")
    print(f"Temperature in Kelvin: {int(k)}K")

elif U == "F":
    c = (T - 32) * 5/9
    k = c + 273.15
    print(f"Temperature in Celsius: {c:.2f}C")
    print(f"Temperature in Kelvin: {int(k)}K")

elif U == "K":
    c = T - 273.15
    f = (c * 9/5) + 32
    print(f"Temperature in Celsius: {c:.2f}C")
    print(f"Temperature in Fahrenheit: {f:.2f}F")

else:
    print("Invalid unit. Please enter C, F, or K.")
Weigth=int(input("Enter your weight in Kilogram : "))
height=float(input("Enter your height in meter : "))

BMI=float(Weigth/height**2)
print(f"the Body Mass Index is {BMI}")

if 17.0 <=BMI <=18.4:
    print("You are underweight")
elif 18.5 >= BMI <=24.9:
    print("You are normal")
else:
    print("You are overweight")
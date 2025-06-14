Year=int(input("Enter the year: "))

if (Year %4==0 and Year % 100!=0) or (Year % 400 ==0):
    print(f"{Year} is leap year.")
else:
    print(f"{Year} is not a leap year.")
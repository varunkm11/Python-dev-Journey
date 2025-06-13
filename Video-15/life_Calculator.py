Age=int(input("Enter your age: "))

years_left=90-Age
months_left=years_left*12
weeks_left=years_left*52
days_left=years_left*365

print(f"Your current age is {Age}")
print(f"You Have approximately have :")
print(f"you have years to live: {years_left}")
print(f"you have months to live: {months_left}")
print(f"you have weeks to live: {weeks_left}")
print(f"you have days to live: {days_left}")
print(f"This is the data you live until you reach to 90 years old.")
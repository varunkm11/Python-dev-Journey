name1 = input("Enter your name:")
name2= input("enter his/her name:")
name_combine= name1+name2
lower_case_integer= name_combine.lower()
t=lower_case_integer.count('t')
r=lower_case_integer.count('r')
u=lower_case_integer.count('u')
e=lower_case_integer.count('e')

true= t+r+u+e
l=lower_case_integer.count('l')
o=lower_case_integer.count('o')
v=lower_case_integer.count('v')
e=lower_case_integer.count('e')

love= l+o+v+e
love_score = int(true)+int(love)
if love_score > 10 or love_score >= 90:
    print(f"your score  {love_score} and you go together like coke and Mentos..")
elif love >= 40 or love_score <= 50:
    print(f"your score {love_score} and you can go together.")
else:
    print(f"your love score is {love_score}")

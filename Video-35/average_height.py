num_people=int(input("how many people height will you  enter:  "))
total_height=0
for i in range(1,num_people + 1):
    height=input(f"Enter the height {i}: ")
    total_height+= int(height)

average_Height=total_height/num_people
print(f"Average height : {int(average_Height)} cm.")
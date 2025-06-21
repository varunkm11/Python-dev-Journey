import math

def paint_calculation( height,width,cover):
    area=height*width
    no_of_cans=math.ceil(area/coverage)
    print(f"Numbers of paint Cans needed: {no_of_cans}")

h=int(input("Enter the height of the wall: "))
w=int(input("Enter the weight of the wall: "))
coverage=7
paint_calculation(height=h,width=w, cover=coverage)
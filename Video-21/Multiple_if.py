Age=int(input("enter the age: "))
if Age<12:
    print("you are a kid")
    if Age<18:
        print("you are a teenager")
        if Age>=18:
            print("you are an adult")
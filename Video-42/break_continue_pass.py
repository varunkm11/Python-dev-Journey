for i in range(1, 8):
    if i == 3:
        print("pass encountered at", i)
        pass  # Does nothing, just a placeholder
    elif i == 5:
        print("continue encountered at", i)
        continue  # Skips the rest of the loop for this iteration
    elif i == 7:
        print("break encountered at", i)
        break  # Exits the loop
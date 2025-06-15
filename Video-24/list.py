my_list=[1, 2, 3, 4, 5]
print(len(my_list))
print(my_list[0])
my_list.append(6)
print("After append(6):", my_list)

my_list[2] = 10
print("After my_list[2] = 10:", my_list)

my_list.remove(2)
print("After remove(2):", my_list)

my_list.insert(1, 10)
print("After insert(1, 10):", my_list)

my_list.sort()
print("After sort():", my_list)

my_list.reverse()
print("After reverse():", my_list)

my_list.pop()
print("After pop():", my_list)

my_list.clear()
print("After clear():", my_list)

my_list.extend([7, 8, 9])
print("After extend([7, 8, 9]):", my_list)

my_list[0:2] = [10, 11]
print("After my_list[0:2] = [10, 11]:", my_list)

my_list = my_list + [12, 13]
print("After my_list + [12, 13]:", my_list)

my_list = my_list * 2
print("After my_list * 2:", my_list)

my_list = my_list[1:5]
print("After my_list[1:5]:", my_list)

my_list = my_list[::2]
print("After my_list[::2]:", my_list)

my_list = my_list[::-1]
print("After my_list[::-1]:", my_list)

my_list = my_list[1:-1]
print("After my_list[1:-1]:", my_list)

my_list = my_list[-3:]
print("After my_list[-3:]:", my_list)
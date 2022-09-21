count_z, count_o = 0, 0
n = int(input())
my_str = list(map(str, input()))
my_List = []
for _ in my_str:
    if str(_) == "z":
        my_List.append(0)
        count_z += 1

    elif str(_) == "n":
        my_List.append(1)
        count_o += 1
my_List.sort(reverse=True)
for _ in my_List:
    print(_, end=" ")
print()

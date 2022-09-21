n = list(map(int, input().split()))
string = input()
for _ in range(n[1]):
    s = list(map(str, input().split()))
    string = string[:int(s[0]) - 1] + string[int(s[0]) - 1:int(s[1])].replace(s[2], s[3]) + string[int(s[1]):]
print(string)

# other solution

# n, m = map(int, input().split())
# string = input()
# for i in range(m):
#     l, r, c1, c2 = (input().split())
#     string = string[:int(l) - 1] + string[int(l) - 1:int(r)].replace(c1, c2) + string[int(r):]
# print(string)

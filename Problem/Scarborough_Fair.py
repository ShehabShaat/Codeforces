def fun(n, string):
    global s
    for _ in range(n[1]):
        s = list(map(str, input().split()))
        # string. = string[int(s[0]):int(s[1])]

    return string


# (int(s[1]) - int(s[0])) + 1

n = list(map(int, input().split()))
string = input()
print(fun(n, string))

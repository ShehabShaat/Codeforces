n = int(input())
count = 0

for row in range(1, n):
    if n % row == 0:
        count += 1
print(count)


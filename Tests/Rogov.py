import math
n = int(input())
a = []
count = 0
for i in range(n):
    a.append(input())
for i in range(len(a)):
    if int(a[i]) == 0:
        count += 1
print(count)

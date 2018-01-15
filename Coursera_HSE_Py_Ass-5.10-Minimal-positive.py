l = list(map(int, input().split()))
a = 0

for i in range(0, len(l)):
    if l[i] > 0:
        a = l[i]
        break

if a == 0:
    print('All numbers are less then 0')

for i in range(0, len(l)):
    if a > l[i] & l[i] > 0:
        a = l[i]
print(a)

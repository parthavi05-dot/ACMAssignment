n, x = map(int, input().split())
a = list(map(int, input().split()))

count = 0

for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        if s == x:
            count += 1

print(count)
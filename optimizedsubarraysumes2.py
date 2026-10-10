n, x = map(int, input().split())
a = list(map(int, input().split()))

left = 0
s = 0
count = 0

for right in range(n):
    s += a[right]

    while s > x and left <= right:
        s -= a[left]
        left += 1

    if s == x:
        count += 1

print(count)
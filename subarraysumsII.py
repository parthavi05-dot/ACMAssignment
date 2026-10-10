n, x = map(int, input().split())
a = list(map(int, input().split()))

freq = {0: 1}
s = 0
count = 0

for num in a:
    s += num
    count += freq.get(s - x, 0)
    freq[s] = freq.get(s, 0) + 1

print(count)
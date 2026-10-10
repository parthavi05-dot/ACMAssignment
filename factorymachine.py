
n, t = map(int, input().split())
k = list(map(int, input().split()))

low = 1
high = min(k) * t

while low < high:
    mid = (low + high) // 2
    products = 0

    for x in k:
        products += mid // x
        if products >= t:
            break

    if products >= t:
        high = mid
    else:
        low = mid + 1

print(low)

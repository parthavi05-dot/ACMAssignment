n = int(input())
movies = []

for i in range(n):
    a, b = map(int, input().split())
    movies.append((a, b))

movies.sort(key=lambda x: x[1])

count = 0
end = 0

for a, b in movies:
    if a >= end:
        count += 1
        end = b

print(count)
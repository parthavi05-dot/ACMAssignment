r, c = map(int, input().split())
building = [list(input().strip()) for _ in range(r)]

def dfs(x, y):
    if x < 0 or x >= r or y < 0 or y >= c:
        return

    if building[x][y] == '#':
        return

    building[x][y] = '#'

    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)

rooms = 0

for x in range(r):
    for y in range(c):
        if building[x][y] == '.':
            rooms += 1
            dfs(x, y)

print(rooms)
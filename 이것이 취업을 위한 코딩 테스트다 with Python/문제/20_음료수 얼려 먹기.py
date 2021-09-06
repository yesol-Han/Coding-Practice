N, M = map(int, input().split())
icebox = [[]*M]*N

for i in range(N):
    icebox[i] = list(map(int, list(input())))

# 아래, 오른쪽 방향
direction = [[0, 1], [1, 0]]
icecream = 0

def dfs(icebox, x, y):
    if not icebox[y][x]:    # 구멍이 있으면,
        icebox[y][x] = 1    # 음료수 넣기

        for dy, dx in direction:  # 오른쪽이나 아래에 구멍이 있는지
            ny = y + dy
            nx = x + dx
            if nx >= M or ny >= N:    # 영역 체크
                continue

            dfs(icebox, nx, ny) # 그 옆도 구멍인지 체크하고 와라
        return True
    else:                       # 연결된 구멍이 더이상 없으면.
        return False

for y in range(N):              # x-M, y-N
    for x in range(M):
        if dfs(icebox, x, y):
            icecream += 1

print(icecream)
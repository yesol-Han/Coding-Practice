# 현재 좌표
point = input()
x, y = ord(point[0]), int(point[1])

# 이동할 수 있는 방법
dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]

# 반환 답안
answer = 0

# 단, a = 97
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    # 범위를 벗어나면 무시
    if nx < 97 or nx >= (97+8) or ny < 1 or ny >= 8:
        continue
    answer += 1

print(answer)

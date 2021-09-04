# N * N 크기 정사각형 공간
N = int(input())
# 이동 계획서
plan = input().split()

# 이동 명령 
direction = [ 'L', 'R', 'U', 'D' ]
x = [0, 0, -1, 1]
y = [-1, 1, 0, 0]
# 반환할 좌표
answer = [1, 1]

for p in plan:
    for i in range(4):
        # 좌표에 맞게 이동
        if p == direction[i]:
            answer[0] += x[i]
            answer[1] += y[i]
            if answer[0] < 1 or answer[0] > N or answer[1] < 1 or answer[1] > N:
                # 공간 벗어나는 경우 복구
                answer[0] -= x[i]
                answer[1] -= y[i]

print(answer)

# (세로, 가로)임을 기억할 것.

"""
    # 답안 보니 복구보다는 오류를 무시하는 것이 안전해 보임. line 14-22
    for i in range(4):
        # 좌표에 맞게 이동
        if p == direction[i]:
            nx = answer[0] + x[i]
            ny = answer[1] + y[i]
    # 공간 벗어나는 경우 무시
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue

    answer[0], answer[1] = nx, ny
"""

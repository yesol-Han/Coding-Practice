import copy

def solution(key, lock):
    answer = False  # True
    len_key = len(key)
    len_lock = len(lock)
    key_turn = [copy.deepcopy(key),copy.deepcopy(key),copy.deepcopy(key),copy.deepcopy(key)]  # 3개는 회전 예정

    for i in range(1, 4):
        for j in range(len_key):
            for k in range(len_key):
                # 시계방향 회전: key_turn[열쇠0][세로][가로] -> key_turn[열쇠1][가로][세로길이-세로]
                key_turn[i][k][len_key-1-j] = key_turn[i-1][j][k]

    print(key_turn)
    def check(a, b, c, each_lock):
        for y in range(len_key):
            for x in range(len_key):
                if (a + y) >=0 and (a + y) < len_lock and (b + x) >=0 and (b + x) < len_lock:
                    if c[y][x] + each_lock[a+y][b+x] != 1:
                        return False
                    each_lock[a+y][b+x] = 1
            if each_lock[y].count(0):
                return False
        return True

    for a in range(1-len_key, len_lock):   # 자물쇠 기준 좌표 이동
        for b in range(1-len_key, len_lock):   # 자물쇠 기준 좌표 이동
            for c in key_turn:  # 열쇠 종류별
                if check(a, b, c, copy.deepcopy(lock)):  # 열쇠가 맞으면
                    print(a, b, c)
                    answer = True
                    return answer
    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[0, 0, 1], [1, 1, 1], [1, 1, 1]]))
#https://programmers.co.kr/learn/courses/30/lessons/60059
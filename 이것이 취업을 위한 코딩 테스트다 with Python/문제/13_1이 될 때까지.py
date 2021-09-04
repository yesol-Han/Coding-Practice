# map으로 int 만들기 기억하기
# 공백 기준으로 구분해서 입력받기
N, K = map(int, input().split())

# 진행 횟수
count = 0

while N != 1:
    if N % K == 0:
        N /= K
    else:
        N -= 1
    count += 1

print(count)

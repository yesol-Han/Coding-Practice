# 문제 입력받기
N = int(input())
fear = list(map(int, input().split()))

# 내림차순 정렬
fear.sort()

group = 0           # 길드 수
count = 0           # 팀원 수
total_count = 0     # 필요 길드 인원 수
# 이하 N은 남은 인원

for i in range(N):
    # 남은 인원보다 필요 인원이 많을 경우 종료
    if fear[i] > N:
        break
    
    count += 1
    total_count = fear[i]

    if count == total_count:    # 공포도에 맞는 길드 인원이 채워진 경우
        N -= total_count
        group += 1
        count = 0

print(group)

"""
# 정답 보고 수정해 봄 (line 13~24)

for i in fear:  # 공포도 확인
    # 남은 인원보다 필요 인원이 많을 경우 종료
    if i > N:
        break
    
    count += 1

    if count == i:    # 공포도에 맞는 길드 인원이 채워진 경우
        group += 1
        count = 0
"""

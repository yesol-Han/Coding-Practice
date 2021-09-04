N = int(input())

# 반환할 변수
answer = 0

for hour in range(N+1):           #시
    for minute in range(60):      #분
        for sec in range(60):     #초
            if '3' in str(hour) + str(minute) + str(sec):
                answer += 1

print(answer)

# 1차 시도 (정답)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(progresses, speeds):
    answer = []
    answer.append(0)
    answer_index = 0
    
    while len(progresses) > 0:
        for i in range(0,len(progresses)):  # 하루 작업
            progresses[i] += speeds[i]
            
        for pro in progresses:  # 배포 가능한지 확인
            if pro < 100:
                break
            answer[answer_index] += 1
        
        if answer[answer_index] != 0:
            del progresses[:answer[answer_index]]
            del speeds[:answer[answer_index]]
            answer.append(0)
            answer_index += 1
        
    answer.remove(0)
    return answer

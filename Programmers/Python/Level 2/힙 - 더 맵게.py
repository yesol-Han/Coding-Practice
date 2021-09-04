# 2차 시도 (정답)
# 정확성: 76.2
# 효율성: 23.8
# 합계: 100.0 / 100.0
    
import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            answer = -1
            return answer
        
        new_sco = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, new_sco)
        
        answer = answer+1
    
    print(scoville)
    return answer

# 1차 시도
# 정확성: 76.2
# 효율성: 0.0
# 합계: 76.2 / 100.0

def solution(scoville, K):
    answer = 0
    
    scoville.sort()
    
    while scoville[0] < K:
        if len(scoville) < 2:
            answer = -1
            return answer
        
        scoville.sort()
        
        new_sco = scoville[0] + scoville[1] * 2
        del scoville[0:2]
        scoville.append(new_sco)
        
        answer = answer+1
    
    print(scoville)
    return answer 
  
  

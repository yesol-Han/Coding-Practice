answer = 0

def solution(numbers, target):
    total = 0
    length = len(numbers)
    
    def dfs(i, total):
        global answer
        if i < length:
            total1 = total + numbers[i]
            total2 = total - numbers[i]
            dfs(i+1, total1)
            dfs(i+1, total2)
        else:   # 다 썼으면,
            if total == target:
                answer += 1
    dfs(0, total)
    
    return answer

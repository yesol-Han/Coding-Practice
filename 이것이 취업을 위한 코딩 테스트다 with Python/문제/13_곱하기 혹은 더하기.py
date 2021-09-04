# 주어진 문자열 S
S = input()
# 문자열 길이
S_len = len(S)

# 연산자
calc = ['*', '+']
# 반환 변수
S_answer = S[0]

for i in range(1, S_len):
    if int(S[i-1]) <= 1 or int(S[i]) <= 1:
        S_answer += calc[1]
    else:
        S_answer += calc[0]
    S_answer += S[i]

print(S_answer)   # 계산식
print(eval(S_answer))

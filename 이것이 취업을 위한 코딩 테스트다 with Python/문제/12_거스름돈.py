total = int(input())

coin = [500, 100, 50, 10]   # 동전
coin_n = [0, 0, 0, 0]   # 동전별 갯수

for i in range(4):
    coin_n[i] = int(total / coin[i])
    total = total % coin[i]
    
    if total == 0:
        break

print(coin_n)

list_str = list(input())
list_alpha = []
number = 0

for list_s in list_str:
    if ord(list_s) < 65:    # 숫자
        number += int(list_s)
    else:                   # 문자
        list_alpha += [list_s]

# 알파벳 정렬
list_alpha.sort()

# 숫자가 있는지 확인
if number != 0:
    list_alpha += [str(number)]

print(''.join(list_alpha))

"""
# 알파벳인지 확인 line 6
if list_s.isalpha():
"""

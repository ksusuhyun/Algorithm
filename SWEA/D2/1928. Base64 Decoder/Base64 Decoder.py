def bit_6(num):
    na = []
    while num:
        na.append(str(num%2))
        num = num//2
    na = na + ['0']*(6-len(na))
    na = na[::-1]
    return ''.join(na)

# 문제에서 주어지는 매핑 테이블 이런 식으로 쉽게 만들 수 있음 
s = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')

t = int(input())
for tc in range(t):
    de = list(input())
    
    sum_bit_8 = []
    for de_s in de:
        num_6 = s.index(de_s)
        # 십진수를 6비트로 바꾸는 함수
        sum_bit_8.append(bit_6(num_6))
    
    ans = []
    sum_bit_8 = list("".join(sum_bit_8))
    for j in range(0,len(sum_bit_8),8):
        bit_8 = sum_bit_8[j:j+8][::-1]
        num_8 = 0
        for k in range(8):
            if int(bit_8[k]):
                num_8 += 2**k
        ans.append(chr(num_8))
    # *ans 못씀
    print(f"#{tc+1} {''.join(ans)}")
t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # long: A, short: B
    if len(a) >= len(b):
        A = a
        B = b
    else:
        A = b
        B = a

    ans = 0
    for i in range(len(A)-len(B)+1):
        s = 0
        for j in range(len(B)):
            s += A[i:i+len(B)][j] * B[j]
        if s > ans:
            ans = s

    print(f'#{tc+1} {ans}')
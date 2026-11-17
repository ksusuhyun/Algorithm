table = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    many = n//10
    score = {}
    for i in range(n):
        m, l, a = map(int, input().split())
        score[i+1] = m*0.35+l*0.45+a*0.20

    # 딕셔너리 정렬 -> k 앞에 몇명 있는지 찾기
    sorted_score = dict(sorted(score.items(), key=lambda x:-x[1]))
    ss_list = list(sorted_score.keys())
    front_k = ss_list.index(k)

    mok = front_k // many
    ans = table[mok]

    print(f'#{tc+1} {ans}')
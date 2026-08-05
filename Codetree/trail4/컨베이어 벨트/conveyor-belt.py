n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
def shift(u, d):
    new = u+d
    temp = new[-1]
    for i in range(2*n-1, 0, -1):
        new[i] = new[i-1]
    new[0] = temp
    return new[0:n], new[n:]

for _ in range(t):
    u, d = shift(u, d)

print(*u)
print(*d)
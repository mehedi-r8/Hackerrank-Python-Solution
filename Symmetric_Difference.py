e = int(input())
eng = set(map(int, input().split()))
f = int(input())
fre = set(map(int, input().split()))

m = set(eng ^ fre)

for i in sorted(m):
    print(i)


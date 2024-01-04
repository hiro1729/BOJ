a = [1, 0]
b = [0, 1]
for i in range(39):
	a.append(a[-1] + a[-2])
	b.append(b[-1] + b[-2])
for _ in range(int(input())):
	N = int(input())
	print(a[N], b[N])
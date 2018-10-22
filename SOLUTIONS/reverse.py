t=int(input())
while t>0:
	l=list(map(str,input().split()))
    l.reverse()
    print(*l)
    t=t-1

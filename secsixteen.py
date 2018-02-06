n=int(input(""))
l=[]
for a in range(0,n):
	b=int(input(""))
	l.append(b)
for a in range(0,n,1):
	m=0
	for b in range(a+1,n,1):
		if l[a]==l[b]:
			m=m+1
	if m==0:
		print(l[a])
		break
	

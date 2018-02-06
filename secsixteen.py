n=int(input(""))
l=[]
for a in range(0,n):
	b=int(input(""))
	l.append(b)
for a in range(0,n-1,1):
	for b in range(a+1,n,1):
		if l[a]<l[b]:
			c=l[a]
			l[a]=l[b]
			l[b]=c
for a in range(0,n,1):
	if a>0 and a<n-1:
		if l[a]!=l[a+1] and l[a]!=l[a-1]:
			print(l[a])
	elif a==0:
		if l[a]!=l[a+1]:
				print(l[a])
	elif a==n-1:
		if l[a]!=l[a-1]:
				print(l[a])
		

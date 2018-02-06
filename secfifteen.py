s=input("")
n=len(s)
max=0
for b in range(n-1,0,-1):
	m=0
	for a in range(b-1,-1,-1):
		if s[a]==s[b]:
			m=m+1
	if m>max:
		c=s[b]
		max=m
print(c)

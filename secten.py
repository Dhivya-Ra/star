s=input("")
n=len(s)
t=input("")
m=len(t)
b=0
if m-n==1:
	m=n
	b=1
elif n-m==1:
	n=m
	b=1
if m==n:	
	for a in range(m):
		if s[a] != t[a]:
			b=b+1
if b==1:
    print("yes")
else:
    print("no")

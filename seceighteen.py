s=[]
n=int(input(""))
for i in range(5):
	c=input("")
	s.append(c)
m=0
t="kabali"
t=(''.join(sorted(t)))
for a in s:
	if len(a)==len(t):
		a=(''.join(sorted(a)))
		if a==t:
			m=m+1
print(m)
		
			

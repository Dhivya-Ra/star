a=int(input(""))
y=int(input(""))
for x in range(a+1,y):
	m=0
	n=x
	while(x>0):
		r=x%10
		x=x//10
		m=(r*r*r)+m
	if m==n:
		print(m)

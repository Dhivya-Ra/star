a=int(input(""))
b=int(input(""))
for x in range(a+1,b):
	n=x
	m=0
	while(x>0):
		x=x//10
		m=m+1
	q=0
	x=n
	while(x>0):
		r=x%10
		x=x//10
		q=(r**m)+q
	if q==n:
		print(n)

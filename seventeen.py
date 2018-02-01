m=0
x=int(input(""))
n=x
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
	print("yes")
else:
	print("no")

x=int(input(""))

m=0
n=0
if x<0:
	x=x*(-1)
	n=1
	
while(x>0):	
	r=x%10
	x=x//10
	m=(m*10)+r
if n==1:
	print(m*(-1))
else:
	print(m)

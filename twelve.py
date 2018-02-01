
x=int(input(""))
n=x
m=0
while(x>0):
	r=x%10
	x=x//10
	m=(m*10)+r
	
if m==n:
	print("yes")
else:
	print("no")


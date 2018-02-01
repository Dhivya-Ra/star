m=0
x=int(input(""))
if x<0:
	print("enter positive integer")
else:
	n=x
	while(x>0):
		r=x%10
		x=x//10
		m=(r*r*r)+m
	if m==n:
		print("yes")
	else:
		print("no")

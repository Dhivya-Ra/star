n=int(input(""))
x=n
d=0
while(x>0):
	r=x%10
	x=x//10
	d=d+(r**2)
print(d)

x=int(input(""))
y=int(input(""))
c=0
if x<0 or y<0:
	print("enter positive integer")
else:
	for b in range(x,y+1):
		m=0
		if b==2:
			c=c+1
		elif b%2 != 0:
			for a in range(3,(b//2)+1):
				if b%a == 0:
					m=m+1
					break;
			if m==0:
				c=c+1
print(c)
		

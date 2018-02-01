x=int(input(""))
y=int(input(""))
if x<0 or y<0:
	print("enter positive integer")
else:
	for b in range(x+1,y):
		m=0
		if b==2:
			print(b)
		elif b%2 != 0:
			for a in range(3,(b//2)+1):
				if b%a == 0:
					m=m+1
					break;
			if m==0:
				print(b)
		

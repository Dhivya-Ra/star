m=0
x=int(input(""))
if x<0:
	print("enter positive integer")
else:
	if x==2:
		print("yes")
	elif x%2==0:
		print("no")
	else:
		for a in range(3,(x//2)+1):
			if x%a == 0:
				print("no")
				m=m+1
				break;
		if m==0:
			print("yes")

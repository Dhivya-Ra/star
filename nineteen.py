x = int(input(""))
if x<0:
	print("negative integer")
else:
	x=x+1
	m=1
	for a in range(1,x):
		m=m*a
	print(m)

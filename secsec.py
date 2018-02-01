x = int(input(""))
if x<0:
	print("negative integer")
else:
	m=1
	for a in range(1,x+1):
		m=m*a
	print(m)

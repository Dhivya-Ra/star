m=int(input(""))
n=int(input(""))
if m>n:
	if m%n ==0:
		print(m)
	else:
		print(m*n)
elif n%m==0:
	print(n)
else:
	print(m*n)

x = int(input(""))
y=int(input(""))
if x%2 == 0:
	x=x+1
else:
	x=x+2
while(x<y):
	print(x)
	x=x+2

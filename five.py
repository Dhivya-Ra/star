x = input(" ")
y=  input(" ")
z=  input(" ")
print("inputs:",end=" ")
print(x,end=" ")
print(y,end=" ")
print(z)
print("o/p")
if x>y :
	if x>z :
		print(x)
	else:
		print(z)
elif y>z:
	print(y)
elif z>y:
	print(z)
else:
	print("all are equal")



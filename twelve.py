x = int(input(""))
n=x
m=0
while (x>0):
	r=int(x)%10
	print(r)
            x=x/10
	m=(m*10)+r
	print(m)
if m==n :
	print("palindrome")
else :
	print("not palindrome")

s=input("")
n=len(s)
for b in range(n-1,-1,-1):
	a=s[b].lower()
	if a!='a' and a!='e' and a!='i' and  a!='o' and  a!='u':
		print(s[b],end="")

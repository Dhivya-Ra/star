n= int(input(""))
l=int(input(""))
if l<0 or n<0:
s=[]
for a in range(n):
	b=int(input(""))
	s.append(b)
b=0
while(b<l):
	d=s[0]
	for a in range(1,n):
		c=s[a]
		s[a]=d
		d=c
	s[0]=d
	b=b+1
for a in s:
	print(a,end=" ")
	

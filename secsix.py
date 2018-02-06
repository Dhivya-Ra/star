s=input("")
t=input("")
l=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
m=0
if len(t) == len(s):
	for a in range(len(s)):
		if m!= 0:
			break
		if l[a]==1:
			l[a]=0
			for b in range(a+1,len(s)):
				if s[b] == s[a]:
					l[b]=0
					if t[b]!= t[a]:
						print("no")
						m=m+1
						break
				if t[b] == t[a]:
					if s[b]!=s[a]:
						print("no")
						m=m+1
						break
	if m==0:
		print("yes")
else:
	print("no")

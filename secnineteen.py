x=int(input(""))
for b in range(2,x+1,1):
	m=0
	if b==2 and x%2 ==0:
		print('2')
	elif b%2 != 0:
		for a in range(3,(b//2)+1):
			if b%a == 0:
				m=m+1
				break;
		if m==0 and x%b==0:
			print(b)
				
		

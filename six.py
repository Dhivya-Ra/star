x=int(input(""))
if x<0:
	print("enter valid input")
else:
	if x%4 ==0 :
		if x%100 == 0:
			if x%400 ==0:
				print('leap year')
			else:
				print('non leap year')
		else:
			print('leap year')
	else:
		print('non leap year')

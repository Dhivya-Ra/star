x=int(input(''))
if x%4 == 0 :
	if x%100 == 0 :
		if x%400 == 0 :
			print("leap")
		else :
			print("non leap")
    else:
    	print("leap")
else:
	print("non leap")

string = input(" string pls \n")
print(string)
string=string.lower()
words = string.split(' ')
for x in words:
    x= x[0].upper() + x[1:]
    print (x, end=" ")
    

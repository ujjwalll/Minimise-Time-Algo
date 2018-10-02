def get_special_numbers(a,b,c,d) :
	l=[]
	for i in range(c,d+1):
		if i%a==0 and i%b!=0:
			l.append(i)


	return l


l=get_special_numbers(3,5,100,150)
print (str(l))

def get_sum(n,k,l):
	for i in range(k):
		for j in n:
			sum=sum+a
		l.append(sum+1)
	
	print(l)
	
#WRITE TEST CASES !!!
	

a,b=map(int,input("Enter two num: ").split())
if a>b:
	a,b=b,a
i=1
count=0
while True:
	count+=1
	if (b*i)%a==0:
		print(b*i," is the LCM of ",a,"and",b)
		break
	i+=1
print(count)
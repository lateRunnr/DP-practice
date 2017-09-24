a=[10,22,9,33,21,50,41,60,80]
lis=[]
for x in range(len(a)):
	lis.append(1)
i=0
while i <= len(a)-1:
	j=0
	while j <= i-1:
		if a[j] < a[i] and lis[i]< lis[j] +1 :
			lis[i]=lis[j]+1
		j+=1
	i+=1
print lis


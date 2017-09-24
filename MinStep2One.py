n=32
global a
a=[0]*33
def findMinSteps(n):
	if n ==1:
		return 0
	a[1]=0
	i=2
	while(i<=n):
		a[i]=1+a[i-1]
		if i%2==0:
			a[i]=min(a[i], 1+findMinSteps(i/2))
		if i%3==0:
			a[i]=min(a[i], 1+ findMinSteps(i/3))
		i+=1
	return a[n]

steps=findMinSteps(n)
print steps
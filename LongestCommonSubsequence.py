import numpy as np
a="azzzbng"
b="zzzzzzavbngh"
lcs=np.zeros([len(a)+1, len(b)+1],dtype=int)
i=0
while i <= len(a):
	j=0
	while j <= len(b):
		if i == 0 or j == 0:
			lcs[i][j]=0
		elif a[i-1] == b[j-1]:
			lcs[i][j]=1+lcs[i-1][j-1]
		else:
			lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
		j+=1
	i+=1
print lcs[len(a)][len(b)]

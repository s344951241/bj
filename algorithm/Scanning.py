#!/user/bin/python
# -*- coding:UTF-8 -*-
# 
import os
arr = [31,-41,59,26,-53,58,97,-93,-23,84]


maxsofar = 0
for i in range(0,len(arr)-1):
	sum = 0
	for j in range(i,len(arr)-1):
		sum = sum+arr[j]
		maxsofar=max(maxsofar,sum)

print(maxsofar)


maxsofar = 0
maxendinghere = 0

for i in range(0,len(arr)-1):
	maxendinghere = max(maxendinghere+arr[i],0)
	maxsofar = max(maxsofar,maxendinghere)

print(maxsofar)

os.system("pause")



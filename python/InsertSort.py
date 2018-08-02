#!/user/bin/python
# -*- coding:UTF-8 -*-
# 
import os

def insertSort(data):
	N = len(data)
	for i in range(1,N):
		for j in range(i,0,-1):
			if data[j]<data[j-1]:
				temp = data[j]
				data[j] = data[j-1]
				data[j-1] = temp
	return data

nums = [9,2,5,8,2,7,1]
print(insertSort(nums))

os.system("pause")
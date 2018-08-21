#!/user/bin/python
# -*- coding:UTF-8 -*-

import os

def quickSort(data,lo,hi):
	if hi<=lo:
		return
	j = partition(data,lo,hi)

nums = [9,2,5,8,2,7,1]
print(selectSort(nums))

os.system("pause")
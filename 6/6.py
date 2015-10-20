# import re

# def doLoop(number):
# 	f = open(str(number)+'.txt', "r")
# 	res = f.read()
# 	print(res)
# 	nums = re.findall('\d+', res)
# 	if nums:
# 		doLoop(nums[len(nums)-1])

# doLoop(90052)

import datetime
import zipfile

arr = list()

zf = zipfile.ZipFile('channel.zip')
for info in zf.infolist():
    arr.append(info.comment)
print(b''.join(arr))
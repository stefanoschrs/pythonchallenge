import re
str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj map"

reg = re.compile('[a-z]')

for x in str:
	if reg.match(x):
		if ord(x) + 2 > 122:
			x =  chr(ord(x) + 2 - 122 + 96)
		else:
			x =  chr(ord(x) + 2)

	print(x, end='')
import urllib.request
import urllib.parse
import re
import webbrowser

BASE_URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?'
def getNext(params):
	f = urllib.request.urlopen("%s%s" % (BASE_URL, urllib.parse.urlencode(params)))
	x = f.read().decode("utf-8")
	print(x)

	### Optional Hack to open the solution page once done
	if 'html' in x:		
		return webbrowser.open('http://www.pythonchallenge.com/pc/def/'+x, new=2)

	nums = re.findall('\d+', x)
	return nums[len(nums)-1]

def doLoop(number):
	res = getNext({
		'nothing': number
	})
	return doLoop(res)

doLoop(12345)
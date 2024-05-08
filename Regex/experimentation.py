import re

def Find(pattern, text):
	match = re.findall(pattern, text)
	if match:
		print(match)
	else:
		print("Not found")

find = Find(r"\w+[.]\w+[.]\w+", "www.google.com. But there is still the gmail www.facebook.com")

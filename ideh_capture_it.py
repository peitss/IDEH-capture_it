import string
import random
import base64


def rot47(s):
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)

def b64e(s):
	decodedBytes = base64.b64decode(s)
	return str(decodedBytes, "utf-8")


def decode(pt):

        for i in range(51):

        	if pt[0]=="1":  
        		pt = pt[1:] 
        		pt=rot47(pt)
        	else:
        		pt = pt[1:]
        		pt=b64e(pt)
   	

        print(pt)

file = open('flag', mode='r')

m = file.read()
decode(m)
file.close()
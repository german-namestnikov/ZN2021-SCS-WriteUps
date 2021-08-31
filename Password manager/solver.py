def convert1(s,prefix):
	ans = ""
	for i in range(len(s)):
		if i % 6 == 0:
			ans += prefix
		ans += s[i]
	while len(ans) % 8 != 0:
		ans += "0"
	return ans
def convert2(s):
	ans = ""
	for i in range(len(s)):
		if i % 8 == 0 or i % 8 == 1:
			continue
		ans += s[i]
	return ans

def xor(s1,s2):
	ans = ""
	for i in range(min(len(s1),len(s2))):
		ans += '1' if ord(s1[i]) ^ ord(s2[i])  else '0'
	return ans
	
def decrypt(ip,data):
	ip_b = ''.join(['{0:08b}'.format(int(i)) for i in ip.split('.')])
	ip_b += ip_b
	ip_b = convert1(ip_b,'01')
	data_b = ''.join(['{0:08b}'.format(ord(c)) for c in data])
	xored = convert2(xor(ip_b,data_b))
	print(len(xored))
	while len(xored) % 8 != 0:
		xored += "0"
	print(len(xored))
	res = ""
	for i in range(len(xored) // 8):
		res += chr(int(xored[8*i:8*i+8],2))
	return res
	
def encrypt(ip, key):
	ip_b = ''.join(['{0:08b}'.format(int(i)) for i in ip.split('.')])
	ip_b += ip_b
	ip_b = convert1(ip_b,'01')
	key_b = ''.join(['{0:08b}'.format(ord(c)) for c in key])
	key_b = convert1(key_b,'00')
	xored = xor(ip_b,key_b)
	res = ""
	for i in range(len(xored) // 8):
		res += chr(int(xored[8*i:8*i+8],2))
	return res
	
	
encrypted = open('128.129.130.131.txt','r').read()
ip = '128.129.130.131'
key=decrypt(ip,encrypted)
print("Master password: {}".format(key))

localhost_key = encrypt('127.0.0.1',key)
print("Archive password: {}".format(localhost_key))

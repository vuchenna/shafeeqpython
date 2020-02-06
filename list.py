alpha = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
msg= input("enter any message: ")

x=0
while x < len(msg):
	alpha[ord(msg[x]) - 65] += 1
	x+=1
i = 0

while i < len(alpha):
	if alpha[i] != 0:
		print(chr(i+65), "=", alpha[i])
	i+=1


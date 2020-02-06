msg = input("input a message")
output= ""
i=0
while i < len(msg):

	if ord(msg[i]) >= 65 and ord(msg[i]) <= 90:
		output = output + ((chr(ord(msg[i]) + 32)))

	elif ord(msg[i]) >= 97 and ord(msg[i]) <= 122:
		output = output + (chr(ord(msg[i]) - 32))

	elif ord(msg[i]) >= 48 and ord(msg[i]) <= 57:
		output = output + str(int(msg[i]) * 2)
	else: 
		output = output + msg[i]
	i+=1
print(output)

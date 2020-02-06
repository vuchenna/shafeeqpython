"""
msg = input("enter a message")
find = input("what are you looking for?")
count = 0
i = 0

while i < len(msg):
	if msg[i:len(find)+i] == find:
		count = count+1
	i+=1
print(count, "found")

"""

print(ord("A"))
print(chr(663))
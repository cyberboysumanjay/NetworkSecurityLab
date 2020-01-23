plain_text="DONTBUNKLABCLASS"
key="NITDELHI"

i=0
k=len(key)
while len(plain_text)!=len(key):
	key=key+key[i]
	i=(i+1)%k

print("Updated key of same length is",key)


print("Cipher text is ",end="")
for p in range(len(plain_text)):
	if plain_text[p]==" ":
		print(" ",end="")
	value=((ord(plain_text[p])+ord(key[p]))%26)+65
	print(chr(value),end="")

print()

cipher_text="QWGWFFUSYIUFPLZA"
print("Decrypted text is ",end="")
for p in range(len(cipher_text)):
	if plain_text[p]==" ":
		print(" ",end="")
	value=((ord(cipher_text[p])-ord(key[p])+26)%26)+65
	print(chr(value),end="")

key=6

def encrypt():
	plain_text=input("Enter Plain Text to Encrypt\n")
	print("Encrypted Text is: ",end="")
	for alphabet in plain_text:
		if alphabet.islower():
			value=((ord(alphabet)%96)+key)%26
			if value==0:
				value=26
			print(chr(value+96),end="")
		elif alphabet.isupper():
			value=((ord(alphabet)%64)+key)%26
			if value==0:
				value=26
			print(chr(value+64),end="")
	print("\n")

def decrypt():
	cipher_text=input("Enter Cipher Text to Decrypt\n")
	print("Decrypted Text is: ",end="")
	for alphabet in cipher_text:
		if alphabet.islower():
			if (ord(alphabet)%96)-key<1:
				value=(((ord(alphabet)%96)-key)+26)
			else:
				value=((ord(alphabet)%96)-key)%26
			print(chr(value+96),end="")
		elif alphabet.isupper():
			if (ord(alphabet)%64)-key<1:
				value=(((ord(alphabet)%64)-key)+26)
			else:
				value=((ord(alphabet)%64)-key)%26
			print(chr(value+64),end="")
	print("\n")

encrypt()
decrypt()
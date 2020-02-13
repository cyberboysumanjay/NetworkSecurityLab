from random import randint
import sboxes

def generate_64bits_key():
	keys_64bits=""
	while len(keys_64bits)!=64:
		digit=randint(0,10)
		keys_64bits=keys_64bits+str(digit%2)
	print("64 Bit Key is",keys_64bits)
	print("Length of generated Key is",len(keys_64bits))
	return keys_64bits

def generate_56bits_key(keys_64bits):
	keys_56bits=""
	while len(keys_56bits)!=56:
		digit=randint(0,56)
		while(digit%8==0):
			digit=randint(0,56)
		keys_56bits=keys_56bits+str(keys_64bits[digit-1])
	print("56 Bit Key is",keys_56bits)
	print("Length of generated Key is",len(keys_56bits))
	return keys_56bits

def split_in_half(keys_56bits):
	left_key,right_key=keys_56bits[:28],keys_56bits[28:]
	print("Splitting Keys into Half",left_key,right_key)
	print("Checking length of half keys",len(left_key),len(right_key))	
	return left_key,right_key

def apply_compression(pc2_table,keys_56bits):
	keys_48bits = ""
	for index in pc2_table:
		keys_48bits += keys_56bits[index-1]
	return keys_48bits

EXPANSION_TABLE = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

def apply_Expansion(expansion_table,bits32):
	bits48 = ""
	for index in expansion_table:
		bits48 += bits32[index-1]
	return bits48


def XOR(bit1,bit2):
	xor_result=""
	for i in range(len(bit1)):
		if bit1[i]==bit2[i]:
			xor_result=xor_result+str(0)
		else:
			xor_result=xor_result+str(1)
	return xor_result

def sbox

def main():	
	keys_64bits=generate_64bits_key()
	keys_56bits=generate_56bits_key(keys_64bits)
	left_key,right_key=split_in_half(keys_56bits)
	PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2, 41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
	subkey = apply_compression(PC2,left_key + right_key)
	print("Subkey length is",len(subkey))
	print(subkey)

	bits32 = '11110000101010101111000010101010'
	out_bits48 = apply_Expansion(EXPANSION_TABLE,bits32)
	print (out_bits48)

	print("XOR Output")
	print(XOR(out_bits48,subkey))

if __name__ == '__main__':
	main()
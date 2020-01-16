def generate_key_table(key):
	table=[]
	all_chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for char in key:
		if char not in table:
			if char=='i':
				if 'j' not in table and 'i' not in table:
					table.append(char)
			elif char=='j':
				if 'i' not in table and 'j' not in table:
					table.append(char)
			else:
				table.append(char)
	
	for char in all_chars:
		if char=='i':
			if 'j' not in table and 'i' not in table:
				table.append(char)
		elif char=='j':
			if 'i' not in table and 'j' not in table:
				table.append(char)
		elif char not in table:
			table.append(char)

	key_table=[]
	for i in range(0,len(table),5):
		key_table.append(table[i:i+5])
	return (key_table)

def playfair_encryption(plain_text,key):
	key_table=generate_key_table(key)
#playfair_encryption('instruments','monarchy')



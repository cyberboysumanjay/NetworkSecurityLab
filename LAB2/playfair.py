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
	print(key_table)
	encrypted_text=""
	if len(plain_text)%2!=0:
		plain_text=plain_text+'x'
	for i in range(0,len(plain_text),2):
		a1=plain_text[i]
		a2=plain_text[i+1]
		i1,i2=-1,-1
		tno1,tno2=-1,-1
		added_flag=False
		for table in key_table:
			if a1 in table and a2 in table:
				tno1=tno1+1
				tno2=tno2+1
				i1=table.index(a1)
				i2=table.index(a2)
				'''
				try:
					i1=table.index(a1)
				except Exception as e:
					i1=-1
				
				try:
					i2=table.index(a2)
				except Exception as e:
					i2=-1
				'''
				encrypted_text=encrypted_text+table[((i1+1)%5)]+table[((i2+1)%5)]
				added_flag=True
				break
			else:
				if not i1>0 or not i2>0:
					if i1<=0:
						tno1=tno1+1
						try:
							i1=table.index(a1)
						except Exception as e:
							i1=-1
					if i2<=0:
						tno2=tno2+1
						try:
							i2=table.index(a2)
						except Exception as e:
							i2=-1
				else:
					break
		
		print("Tnos",tno1,tno2)
		print(i1,i2)
		encrypted_text=encrypted_text+key_table[(tno1)][i2]+key_table[(tno2)][i1]
	print(encrypted_text)

playfair_encryption('instruments','monarchy')





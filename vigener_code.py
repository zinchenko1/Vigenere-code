def c_vishener():

	abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	print()

	def visualization(n):
		while n<26:
			for i in abc:
				print(i,end=" ")
			abc.append(abc[0])
			abc.remove(abc[0])
			print()
			n+=1
	visualization(0)

	print("\n1. Crypt")
	print("2. Read the Crypt-file with Key-file")

	try: 
		answer=int(input("\nChoose the Number > "))
		print()

		if answer==1: 
			key=open("key.txt","w")
			m=input("Write the text: ")
			k=input("Write the key: ")
			k*=len(m)//len(k)+1
			key.write(k)

			crypt=open("crypt.txt","w")
			c=""
			for i,j in enumerate(m):
				gg=(ord(j)+ord(k[i])) 
				c+=chr(gg%26+ord('A')) 
			print()
			print("Crypt message: "+str(c))
			crypt.write(c) 

		elif answer==2:
			decrypt_r=open("crypt.txt","r")
			readm=decrypt_r.read()
			dkey=open("key.txt","r")
			readk=dkey.read()
			v="" 
			for i,j in enumerate(readm):
				gg=(ord(j)-ord(readk[i]))
				v+=chr(gg%26+ord('A'))
			print("Decrypt message: "+str(v)+"\n")

		else: print("Number is not defined!") 
	except ValueError: print("\nError!\nWrite only integer numbers!")

c_vishener()

input("\nPress ENTER to exit")
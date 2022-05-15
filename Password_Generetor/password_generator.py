import string
import random


characters = list()




a = 1
while a==1 :

	up = input("Will there be capital letters in the password? (y/n) : ")

	if up == "y":
		characters += string.ascii_uppercase
		a -= 1
	elif up == "Y":
		characters += string.ascii_uppercase
		a -= 1
	elif up == "n":
		a -= 1
	elif up == "N":
		a -= 1
	else:
		print("just y or n")
		continue

b= 1
while b == 1:

	low = input("\nWill the password be lowercase? (y/n): ")

	if low == "y":
		characters += string.ascii_lowercase
		b -= 1
	elif low == "Y":
		characters += string.ascii_lowercase
		b -= 1
	elif low == "n":
		b -= 1
	elif low == "N":
		b -= 1
	else:
		print("just y or n")
		continue
		
	


c= 1
while c == 1:

	dig = input("\nWill there be a number in the password? (y/n): ")

	if dig == "y":
		characters += string.digits
		c -= 1
	elif dig == "Y":
		characters += string.digits
		c -= 1
	elif dig == "n":
		c -= 1
	elif dig == "N":
		c -= 1
	else:
		print("\njust (y) or (n) ")
		continue

d = 1
while d == 1:

	pun = input("\nWill there be symbols in the password? (y/n): ")

	if pun == "y":
		characters += string.punctuation
		d -= 1
	elif pun == "Y":
		characters += string.punctuation
		d -= 1	
	elif pun == "n":
		d -= 1
	elif pun == "N":
		d -= 1
	else:
		print("\njust (y) or (n) ")
		continue

t = 1
while t == 1:
	try:
		length = int(input("\nEnter password length: "))
	except:
		print("\nPlease enter number only !!")
		continue
	else:
		t -= 1


	
random.shuffle(characters)
	
	
password = []
for i in range(length):
	password.append(random.choice(characters))

	
random.shuffle(password)


print("".join(password))


password1 = ("".join(password))
e = 1
while e == 1:
	save_pass = input("\nsave password? (y/n): ")
	
	if save_pass == "y":

		where_pass = input("\nWhere will you use this password : ")


		f = open("passwords.txt","a")
		f.write(f"\nYour {where_pass} password is ---> {password1}")
		f.close()
		print(f"\nOk. your {where_pass} password is saved in the passwords.txt")
		e -= 1
	
	elif save_pass == "Y":

		where_pass = input("\nWhere will you use this password : ")

		f = open("passwords.txt","a")
		f.write(f"\nYour {where_pass} password is ---> {password1}")
		f.close()
		print(f"\nOk. your {where_pass} password is saved in the passwords.txt")
		e -= 1
	
	elif save_pass == "n":
		print("\nok bye!")
		break

	elif save_pass == "N":
		print("\nok bye!")
		break









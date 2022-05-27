#!/usr/bin/python3
#
#  [Program]
#
#	OSINTed_Pass
#
#  [Author]
#
#  Tarek Mahfoudh
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation.

import subprocess

profile = {}


## HIMSELF ##


def main():

	print ("If there's a \'*\' then the field is required !")

	name = str(input("*First Name: \n > ")).lower().strip()
	while len(name) == 0:
		print("Enter the first name !")
		name = str(input("*First Name: \n > ")).lower().strip()
	profile['name'] = name

	surname = str(input("*Surname: \n > ")).lower().strip()
	while len(surname) == 0 :
		print("Enter the Surname !")
		surname = str(input("*Surname: \n > ")).lower().strip()
	profile['surname'] = surname

	profile["nickname"] = str(input("Nickname: \n > ")).lower().strip()
	profile["phone_number"] = str(input("Phone_number: \n > ")).strip()


	birthdate = str(input("Birthdate (DDMMYYYY): \n > ").strip())
	while len(birthdate) != 0 and len(birthdate) != 8:
		print("Use the correct format !")
		birthdate = str(input("Birthdate (DDMMYYYY): \n > ").strip())
	profile["birthdate"] = str(birthdate)

	profile['birthplace_dept'] = str(input("Birthplace (Departement): \n > ").strip())
	profile['birthplace_city'] = str(input("Birthplace (City): \n > ").strip())




	## COMPANION ##
	while True :
		profile['companion'] = str(input("*Does the target have a wife/husband/companion ? [y/n]\n > ")).lower().strip()
		if profile['companion']:
			if profile['companion'][0] != 'y' and profile['companion'][0] != 'n': 
				print("Please try again !")
			else:
				break;

	if profile['companion'][0] == 'y':
		profile['companion_name'] = str(input("First Name: \n > ")).lower().strip()
		profile['companion_surname'] = str(input("Surname: \n > ")).lower().strip()
		profile['companion_nickname'] = str(input("Nickname: \n > ")).lower().strip()
		profile['companion_birthdate'] = str(input("Birthdate (DDMMYYYY): \n > ").strip())
		profile["companion_phone_number"] = str(input("Phone_number: \n > ")).strip()



	## KIDS ##

	while True:
		try:
			profile['kids'] = int(input("*How many kids does the taget have ? [0-9]\n > ").strip())
		except ValueError:
			print("Please input an integer !")
		else:
			break

	for i in range(1, profile['kids']+1):
		print ("Kid number %s" % i)
		profile["kid%s_name"% i] = str(input("First Name: \n > ")).lower().strip()
		profile["kid%s_surname"% i] = str(input("Surname: \n > ")).lower().strip()
		profile["kid%s_nickname"% i] = str(input("Nickname: \n > ")).lower().strip()
		profile["kid%s_birthdate"% i] = str(input("Birthdate (DDMMYYYY): \n > ").strip())

	## PETS ##

	while True:
		try:
			profile['pets'] = int(input("*How many pets does the taget have ? [0-9]\n > ").strip())
		except ValueError:
			print("Please input an integer !")
		else:
			break

	for i in range(1, profile['pets']+1):
		print ("Pet number %s" % i)
		profile["pet%s_name"% i] = str(input("Name: \n > ")).lower().strip()
		profile["pet%s_nickname"% i] = str(input("Nickname: \n > ")).lower().strip()
		profile["pet%s_birthdate"% i] = str(input("Birthdate (DDMMYYYY): \n > ").strip())


	nbperson=1
	nbplace=1
	nbdate=1
	nbother=1

	while True:
		try : 
			print("Any other thing that you have in mind that could matter to him ?")
			choice = str(input("1)Person: \n2)Place: \n3)Date : \n4)Other: \n5)End \n > ").strip())
			if choice == '1':
				nbperson = newPerson(nbperson)
			elif choice == '2':
				nbplace = newPlace(nbplace)
			elif choice == '3':
				nbdate = newDate(nbdate)
			elif choice == '4':
				nbother = newOther(nbother)

			else : 
				break;
		except ValueError:
			print("That was not a valid number !")
			nbperson-=1;nbdate-=1;nbplace-=1;nbother-=1;
	generate_dictionnary(profile, nbperson, nbplace, nbdate, nbother)


def newPerson(nbperson):
	profile["person%s_name"% nbperson] = str(input("First Name: \n > ")).lower().strip()
	profile["person%s_surname"% nbperson] = str(input("Surname: \n > ")).lower().strip()
	profile["person%s_nickname"% nbperson] = str(input("Nickname: \n > ")).lower().strip()
	profile["person%s_birthdate"% nbperson] = str(input("Birthdate (DDMMYYYY): \n > ").strip())
	return nbperson + 1

def newPlace(nbplace):
	profile["place_dept%s" % nbplace] = str(input("Place (Departement): \n > ").strip())
	profile["place_city%s" % nbplace] = str(input("Place (City): \n > ").strip())
	return nbplace + 1

def newDate(nbdate):
	profile["date%s"% nbdate] = str(input("Date (DDMMYYYY): \n > ").strip())
	return nbdate + 1

def newOther(nbother):
	profile["other%s"% nbother] = str(input("Other String: \n > ")).lower().strip()
	return nbother + 1


def generate_dictionnary(profile, nbperson, nbplace, nbdate, nbother):
	print(profile)
	dates = []
	names = []
	numbers = []
	places = []

	if profile['name']:
		names.append(profile['name'])
	if profile['surname']:
		names.append(profile['surname'])
	if profile['nickname']:
		names.append(profile['nickname'])
	if profile['phone_number']:
		numbers.append(profile['phone_number'])
	if profile['birthplace_dept']:
		places.append(profile['birthplace_dept'])
	if profile['birthplace_city']:
		places.append(profile['birthplace_city'])
	if profile['birthdate']:
		dates.append(profile["birthdate"][-2:])	#ddmmyyYY
		dates.append(profile["birthdate"][-4:])	#ddmmYYYY
		dates.append(profile["birthdate"][:2])	#DDmmyyyy
		dates.append(profile["birthdate"][2:4])	#ddMMyyyy
		dates.append(profile["birthdate"][:4]+profile["birthdate"][-2:])	#DDMMyyYY


	if profile['companion'][0] == 'y':
		if profile['companion_name']:
			names.append(profile['companion_name'])
		if profile['companion_surname']:
			names.append(profile['companion_surname'])
		if profile['companion_nickname']:
			names.append(profile['companion_nickname'])
		if profile['companion_phone_number']:
			numbers.append(profile['companion_phone_number'])
		if 	profile['companion_birthdate']:
			dates.append(profile["companion_birthdate"][-2:])
			dates.append(profile["companion_birthdate"][-4:])
			dates.append(profile["companion_birthdate"][:2])
			dates.append(profile["companion_birthdate"][2:4])
			dates.append(profile["companion_birthdate"][:4]+profile["companion_birthdate"][-2:])



	for i in range(1, profile['kids']+1):
		if profile['kid%s_name' % i]:
			names.append(profile['kid%s_name' % i])
		if profile['kid%s_surname' % i]:
			names.append(profile['kid%s_surname' % i])
		if profile['kid%s_nickname' % i]:
			names.append(profile['kid%s_nickname' % i])
		if profile['kid%s_birthdate' % i]:
			dates.append(profile['kid%s_birthdate' % i][-2:])
			dates.append(profile['kid%s_birthdate' % i][-4:])
			dates.append(profile['kid%s_birthdate' % i][:2])
			dates.append(profile['kid%s_birthdate' % i][2:4])
			dates.append(profile['person%s_birthdate' % i][:4]+profile['person%s_birthdate' % i][-2:])


	for i in range(1, profile['pets']+1):
		if profile['pet%s_name' % i]:
			names.append(profile['pet%s_name' % i])
		if profile['pet%s_nickname' % i]:
			names.append(profile['pet%s_nickname' % i])
		if profile['pet%s_birthdate' % i]:
			dates.append(profile['pet%s_birthdate' % i][-2:])
			dates.append(profile['pet%s_birthdate' % i][-4:])
			dates.append(profile['pet%s_birthdate' % i][:2])
			dates.append(profile['pet%s_birthdate' % i][2:4])
			dates.append(profile['pet%s_birthdate' % i][:4]+profile['pet%s_birthdate' % i][-2:])




	for i in range(1, nbperson):
		if profile['person%s_name' % i]:
			names.append(profile['person%s_name' % i])
		if profile['person%s_surname' % i]:
			names.append(profile['person%s_surname' % i])
		if profile['person%s_nickname' % i]:
			names.append(profile['person%s_nickname' % i])
		if profile['person%s_birthdate' % i]:
			dates.append(profile['person%s_birthdate' % i][-2:])
			dates.append(profile['person%s_birthdate' % i][-4:])
			dates.append(profile['person%s_birthdate' % i][:2])
			dates.append(profile['person%s_birthdate' % i][2:4])
			dates.append(profile['person%s_birthdate' % i][:4]+profile['person%s_birthdate' % i][-2:])


	for i in range(1, nbplace):
		if profile["place_dept%s" % i]:
			places.append(profile["place_dept%s" % i])
		if profile["place_city%s" % i]:
			places.append(profile["place_city%s" % i])

	for i in range(1, nbdate):
		if profile["date%s"% i]:
			dates.append(profile["date%s"% i][-2:])
			dates.append(profile["date%s"% i][-4:])
			dates.append(profile["date%s"% i][:2])
			dates.append(profile["date%s"% i][2:4])
			dates.append(profile["date%s"% i][:4]+profile["date%s"% i][-2:])


	for i in range(1, nbother):
		if profile["other%s"% i]:
			names.append(profile["other%s"% i])


	#note : dans 3/4 des cas, le mdp commence par une majuscule

	#dans password on traitera tout les cas possibles et probables, on les ajoutera ensuite aux
	#autres listes avec le format designe. On les a classe selon l'ordre de proba d'apparition.

	#note : tres peu (voire impossible) de mdp contiennent 2 prenoms/noms
	#note : 1/4 des mots de passe sont uniquements constitues de nom OU prenom

	
	#light
	password = []
	Password = []
	password1 = []
	Password1 = []

	#Heavy
	password2_9 = []
	Password2_9 = []

	#Very Heavy
	password09_09 = []

	#define places, define numbers

	for name in names:
		password.append(name)
		for date in dates:
			password.append(name+date)
			password.append(date+name)
			for date2 in dates:
				password.append(name+date+date2)
				password.append(date+date2+name)
				password.append(name+date2+date)
				password.append(date2+date+name)			
		for place in places:
			password.append(name+place)
			password.append(place+name)
		for name2 in names:
			if name != name2:
				password.append(name+name2)
		for number in numbers:
			password.append(name+number)
			password.append(number+name)

	for number in numbers:
		password.append(number)

	for place in places:
		for date in dates:
			for name in names:
				password.append(date+place)
				password.append(place+date)
				password.append(name+place+date)
				password.append(place+name+date)	

	for date in dates:
		for date2 in dates:
			if date != date2:
				password.append(date+date2)

	Password = [pas.capitalize() for pas in password]
	pass_length = 8
	with open("password.txt", "w") as output:
		for pas in password:
			if len(pas) >= pass_length:
				output.write(pas+'\n')

	with open("Password.txt", "w") as output:
		for pas in Password:
			if len(pas) >= pass_length:
				output.write(pas+'\n')

	with open("password1.txt", "w") as output:
		for pas in password:
			if len(pas)>= pass_length :
				if (not pas[-1].isnumeric()):
					output.write(pas+'1\n')

	with open("Password1.txt", "w") as output:
		for pas in Password:
			if len(pas) >= pass_length :
				if (not pas[-1].isnumeric()):
					output.write(pas+'1\n')

	
	bashCommand = "cat password.txt Password.txt password1.txt Password1.txt > pass.txt"
	process = subprocess.run(bashCommand, shell=True, check=True)

	bashCommand = "cat -n pass.txt | sort -uk2 | sort -n | cut -f2- > pass_s.txt"
	process = subprocess.run(bashCommand, shell=True, check=True)

	bashCommand = "rm pass.txt password1.txt password.txt Password.txt Password1.txt"
	process = subprocess.run(bashCommand, shell=True, check=True)


if __name__ == '__main__':
    main()
from random import randint

random_number = randint(1,10)
guess = None


while guess !=random_number:
	guess = input("Pick a number from 1 to 10: ")
	guess = int(guess)
	if guess < random_number:
		print("TOO LOW!")	
	elif guess > random_number:
		print("TOO HIGH!")
	else:
		print("YOU WON!!!!")

print(random_number)
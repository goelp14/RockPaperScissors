#!/usr/bin/env python3

import random
winInt = 0.0
loseInt = 0.0
tieInt = 0.0


def start():
	print(
	    "Welcome to Rock Paper Scissors! The Machine is guessing Purely on your last input. How well will you do against it? Lets find out!!!\n"
	)
	intermediateMode()


def intermediateMode():
	choices = ["Rock", "Paper", "Scissors"]
	continuePlaying = True
	continueGame = ""
	prevChoice = ""
	prevMachineChoice = ""
	result = ""
	streak = 0
	won = 0
	alt = 0
	numoff = 0
	choice = 3

	try:
		choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
	except ValueError:
		print("you must enter an integer \n")

	if (choice > 2 or choice < 0):
		print(
		    "You must enter an integer less than three and greater than 0. \n")
		while (choice > 2 or choice < 0):
			try:
				choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
			except ValueError:
				print("you must enter an integer \n")
	machineChoice = random.randint(0, 2)
	result = checkWin(choice, machineChoice, 2)
	if (result == "Win!"):
		won += 1
	else:
		numoff += 1
		if (numoff == 3):
			won -= 3
			numoff = 0
		if (won < 0):
			won = 0

	print("You chose %s" % choices[choice])
	print("The machine chose %s" % choices[machineChoice])
	print("You %s" % result)

	prevChoice = choice
	prevMachineChoice = machineChoice
	streak += 1

	while (continuePlaying):
		try:
			choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
		except ValueError:
			print("you must enter an integer \n")

		if ((choice > 2 or choice < 0) and choice != 5):
			print(
			    "You must enter an integer less than three and greater than 0. Or put 5 to exit \n"
			)
			while ((choice > 2 or choice < 0) and choice != 5):
				try:
					print(
					    "You must enter an integer less than three and greater than 0. Or put 5 to exit \n"
					)
					choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
				except ValueError:
					print("you must enter an integer \n")

		if (choice == 5):
			print("Thanks for Playing!")
			continuePlaying = False
		else:
			if (prevChoice == choice):
				streak += 1
			else:
				streak -= 1
				if (streak < 0):
					streak = 0
			if (streak > 3):
				machineChoice = prevChoice - 2
				if (machineChoice < 0):
					machineChoice += 3
			elif (won > 9):
				print(
				    "Yo. Stop cheating and keep your eyes off my code. Just play normally. You wouldn't be able to look at previous decisions so accurately in a real game alright? If ya continue to do dis the machine won't care anymore - it's a sore loser and hates people like you."
				)
				machineChoice = random.randint(0, 2)
			elif (won > 3 and won < 10):
				machineChoice = prevChoice
			else:
				if (result == "Win!"):
					machineChoice = prevChoice - 2
					if (machineChoice < 0):
						machineChoice += 3
				elif (result == "Lose!"):
					machineChoice = prevChoice + 1
					if (machineChoice > 2):
						machineChoice -= 3
					machineChoice -= 2
					if (machineChoice < 0):
						machineChoice += 3
				else:
					machineChoice = random.randint(0, 2)

			result = checkWin(choice, machineChoice, 2)

			if (result == "Win!"):
				won += 1
			else:
				won -= 2
				if (won < 0):
					won = 0

			print("You chose %s" % choices[choice])
			print("The machine chose %s" % choices[machineChoice])
			print("You %s" % result)
			prevChoice = choice
	main()


def checkWin(user, machine, mode):
	win = False
	tie = False
	if (user == 0):
		if (machine == 2):
			win = True
			tie = False
		elif (machine == 1):
			win = False
			tie = False
		elif (user == 0):
			tie = True
		else:
		  print ("Something wierd happened and machine was: %s" % machine)
	elif (user == 1):
		if (machine == 0):
			win = True
			tie = False
		elif (machine == 2):
			win = False
			tie = False
		elif (machine == 1):
			tie = True
		else:
		  print ("Something wierd happened and machine was: %s" % machine)
	else:
		if (machine == 1):
			win = True
			tie = False
		elif (machine == 0):
			win = False
			tie = False
		elif (machine == 2):
			tie = True
		else:
		  print ("Something wierd happened and machine was: %s" % machine)

	if (tie == True):
		checkStats(2, mode)
		return "Tied!"
	elif (win):
		checkStats(0, mode)
		return "Win!"
	else:
		checkStats(1, mode)
		return "Lose!"


def main():
	notyesorno = True
	percentWon = "{percent:.2%}".format(
	    percent=(winInt / (winInt + loseInt + tieInt)))
	print("You won %d times on Intermediate Mode! \n" % winInt)
	print("You lost %d times on Intermediate Mode! \n" % loseInt)
	print("You tied %d times on Intermediate Mode! \n" % tieInt)
	print("You have a %s win rate on Intermediate Mode! You played %s times!" %
	      (percentWon, winInt + loseInt + tieInt))
	while (notyesorno):
		continueGame = input(
		    "Do you wanna continue playing? Type Yes or No \n")
		if (continueGame == "Yes"):
			print("Coolio. \n")
			notyesorno = False
			intermediateMode()
		elif (continueGame == "No"):
			print("Aw that's too bad. :( \n")
			notyesorno = False
		else:
			print(
			    "Nah... That's not an acceptable answer. Please type Yes or No"
			)
			notyesorno = True


def continueGameCheck(ans):
	if (ans == "Yes"):
		return "Yes"
	elif (ans == "No"):
		return "No"
	else:
		return "Wrong input"


def checkStats(wlt, modeChosen):
	global winEas
	global loseEas
	global tieEas
	global winInt
	global loseInt
	global tieInt
	global winHard
	global loseHard
	global tieHard

	if (modeChosen == 1):
		if (wlt == 0):
			winEas += 1
		elif (wlt == 1):
			loseEas += 1
		else:
			tieEas += 1
	elif (modeChosen == 2):
		if (wlt == 0):
			winInt += 1
		elif (wlt == 1):
			loseInt += 1
		else:
			tieInt += 1
	else:
		if (wlt == 0):
			winHard += 1
		elif (wlt == 1):
			loseHard += 1
		else:
			tieHard += 1


start()

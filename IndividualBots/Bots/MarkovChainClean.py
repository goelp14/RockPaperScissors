#!/usr/bin/env python3

import random
winEas,loseEas,tieEas = 0.0,0.0,0.0

buildTMatrix = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
buildTMatrixL = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
buildTMatrixT = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}

n = 3
m = 3
tMatrix = [[0] * m for i in range(n)]
tMatrixL = [[0] * m for i in range(n)]
tMatrixT = [[0] * m for i in range(n)]

probabilitiesRPS = [1/3,1/3,1/3]

def markov():
  global probabilitiesRPS
  choices = ["Rock","Paper","Scissors"]
  choi = ['r','p','s']
  continuePlaying = True
  prevChoice = ""
  choice = 3
  probRock = 0
  probPaper = 0
  probScissors = 0

  try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
  except ValueError:
    print("you must enter an integer \n")

  if(choice > 2 or choice < 0):
    print ("You must enter an integer less than three and greater than 0  \n")
    while(choice > 2 or choice < 0):
      print ("You must enter an integer less than three and greater than 0 \n")
      try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
      except ValueError:
        print("you must enter an integer \n")

  machineChoice = random.randint(0, 2)
  result = checkWin(choice,machineChoice,1)
  print ("You chose %s" % choices[choice])
  print ("The machine chose %s" % choices[machineChoice])
  print("You %s" % result)

  prevChoice = choice

  while(continuePlaying):
    choice = 3
    try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
    except ValueError:
      print("you must enter an integer \n")

    if((choice > 2 or choice < 0) and choice != 5):
      print ("You must enter an integer less than three and greater than 0 or choose 5 to exit.  \n")
      while((choice > 2 or choice < 0) and choice != 5):
        print ("You must enter an integer less than three and greater than 0 or choose 5 to exit.\n")
        try:
          choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
        except ValueError:
          print("you must enter an integer \n")
    if (choice == 5):
      print ("Thanks for Playing!")
      print ("You won %d times!" % int(winEas))
      print ("You lost %d times!" % int(loseEas))
      print ("You tied %d times!" % int(tieEas))
      percentWon = "{percent:.2%}".format(percent=(winEas / (winEas+loseEas+tieEas)))
      print ("Your win percentage is %s from a total of %d games" % (percentWon,int(winEas+loseEas+tieEas)))
      continuePlaying = False
    else:
      transMatrix = buildTransitionProbabilities(prevChoice,choice,result)
      machineChoice = random.randint(1, 100)
      probabilitiesRPS[0] = transMatrix[prevChoice][0]
      probabilitiesRPS[1] = transMatrix[prevChoice][1]
      probabilitiesRPS[2] = transMatrix[prevChoice][2]
      rangeR = probabilitiesRPS[0] * 100
      rangeP = probabilitiesRPS[1] * 100 + rangeR
      if (machineChoice <= rangeR):
        machineChoice = 1
      elif (machineChoice <= rangeP):
        machineChoice = 2
      else:
        machineChoice = 0

      result = checkWin(choice,machineChoice,1)
      prevChoice = choice
      print ("You chose %s" % choices[choice])
      print ("The machine chose %s" % choices[machineChoice])
      print("You %s" % result)

  print("Your winning transition matrix is:\nr: %s\np: %s\ns: %s\n" % (tMatrix[0],tMatrix[1],tMatrix[2]))
  print("Your losing transition matrix is:\nr: %s\np: %s\ns: %s\n" % (tMatrixL[0],tMatrixL[1],tMatrixL[2]))
  print("Your tying transition matrix is:\nr: %s\np: %s\ns: %s\n" % (tMatrixT[0],tMatrixT[1],tMatrixT[2]))

def buildTransitionProbabilities(pC,c,winloss):
  global buildTMatrix
  global buildTMatrixL
  global buildTMatrixT
  choi = ['r','p','s']

  if winloss == "Win!":
    for i, x in buildTMatrix.items():
      if ('%s%s' % (choi[pC],choi[c]) == i):
        buildTMatrix['%s%s' % (choi[pC], choi[c])] += 1
  elif winloss == "Tied!":
    for i, x in buildTMatrixT.items():
      if ('%s%s' % (choi[pC],choi[c]) == i):
        buildTMatrixT['%s%s' % (choi[pC], choi[c])] += 1
  else:
    for i, x in buildTMatrixL.items():
      if ('%s%s' % (choi[pC],choi[c]) == i):
        buildTMatrixL['%s%s' % (choi[pC], choi[c])] += 1

  return buildTransitionMatrix(winloss)

def buildTransitionMatrix(winlosstwo):
  global tMatrix
  global tMatrixL
  global tMatrixT

  if winlosstwo == "Win!":
    rock = buildTMatrix['rr'] + buildTMatrix['rs'] +buildTMatrix['rp']
    paper = buildTMatrix['pr'] + buildTMatrix['ps'] +buildTMatrix['pp']
    scissors = buildTMatrix['sr'] + buildTMatrix['ss'] +buildTMatrix['sp']
    choi = ['r','p','s']
    for row_index, row in enumerate(tMatrix):
      for col_index, item in enumerate(row):
          a = int(buildTMatrix['%s%s' % (choi[row_index],choi[col_index])])
          if (row_index == 0):
            c = a/rock
          elif (row_index == 1):
            c = a/paper
          else:
            c = a/scissors
          row[col_index] = float(c)
    return (tMatrix)
  elif winlosstwo == "Tied!":
    rock = buildTMatrixT['rr'] + buildTMatrixT['rs'] +buildTMatrixT['rp']
    paper = buildTMatrixT['pr'] + buildTMatrixT['ps'] +buildTMatrixT['pp']
    scissors = buildTMatrixT['sr'] + buildTMatrixT['ss'] +buildTMatrixT['sp']
    choi = ['r','p','s']
    for row_index, row in enumerate(tMatrixT):
      for col_index, item in enumerate(row):
          a = int(buildTMatrixT['%s%s' % (choi[row_index],choi[col_index])])
          if (row_index == 0):
            c = a/rock
          elif (row_index == 1):
            c = a/paper
          else:
            c = a/scissors
          row[col_index] = float(c)
    return (tMatrixT)

  else:
    rock = buildTMatrixL['rr'] + buildTMatrixL['rs'] +buildTMatrixL['rp']
    paper = buildTMatrixL['pr'] + buildTMatrixL['ps'] +buildTMatrixL['pp']
    scissors = buildTMatrixL['sr'] + buildTMatrixL['ss'] +buildTMatrixL['sp']
    choi = ['r','p','s']
    for row_index, row in enumerate(tMatrixL):
      for col_index, item in enumerate(row):
          a = int(buildTMatrixL['%s%s' % (choi[row_index],choi[col_index])])
          if (row_index == 0):
            c = a/rock
          elif (row_index == 1):
            c = a/paper
          else:
            c = a/scissors
          row[col_index] = float(c)
    return (tMatrixL)

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

def checkStats(wlt,modeChosen):
  global winEas
  global loseEas
  global tieEas

  if (modeChosen == 1):
    if (wlt == 0):
      winEas += 1
    elif (wlt == 1):
      loseEas += 1
    else:
      tieEas += 1

markov()

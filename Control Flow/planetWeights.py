planetWeight = float(input('What is your planet weight?'))
planetNumber = int(input('Choose a Planet Number'))

if planetNumber == 1:
  destinationWeight = planetWeight * 0.38
  print('Your Destination Weight:', destinationWeight)
elif planetNumber == 2:
  destinationWeight = planetWeight * 0.91
  print('Your Destination Weight:', destinationWeight)
elif planetNumber == 3:
  destinationWeight = planetWeight * 0.38
  print('Your Destination Weight:', destinationWeight)
elif planetNumber == 4:
  destinationWeight = planetWeight * 2.53
  print('Your Destination Weight:', destinationWeight)
elif planetNumber == 5:
  destinationWeight = planetWeight * 1.07
  print('Your Destination Weight:', destinationWeight)
elif planetNumber == 6:
  destinationWeight = planetWeight * 0.89
  print('Your Destination Weight: ', destinationWeight)
elif planetNumber == 7:
  destinationWeight = planetWeight * 1.14
  print('Your Destination Weight:', destinationWeight)
else:
  print('Invalid planet Number')
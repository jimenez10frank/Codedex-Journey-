gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

question1 = int(input('Do you Like Dawn or Dusk? 1 = Dawn 2 = Dusk'))

if question1 == 1:
    gryffindor + 1
    ravenclaw + 1
elif question1 == 2:
    hufflepuff + 1
    slytherin + 1
else:
    print('wrong input')

question2 = int(input('When I’m dead, I want people to remember me as:     1) The Good 2) The Great 3) The Wise 4) The Bold'))

if question2 == 1:
    hufflepuff + 2
elif question2 == 2:
    slytherin + 2
elif question2 == 3:
    ravenclaw + 2
elif question2 == 4:
    gryffindor + 2
else:
    print('wrong input')

question3 = int(input('Which kind of instrument most pleases your ear?    1) The violin 2) The trumpet 3) The piano 4) The drum'))

if question3 == 1:
    slytherin + 4
elif question3 == 2:
    hufflepuff + 4
elif question3 == 3:
    ravenclaw + 4
elif question3 == 4:
    gryffindor + 4
else:
    print('wrong input')

print(gryffindor, slytherin, ravenclaw, hufflepuff)



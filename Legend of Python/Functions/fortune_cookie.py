import random
def fortune():
    fortunelist = random.randint(1, 5)

    if fortunelist == 1:
        print('Dont pursue happiness – create it.')
    elif fortunelist == 2:
        print('All things are difficult before they are easy')
    elif fortunelist == 3:
        print('The early bird gets the worm, but the second mouse gets the cheese.')
    elif fortunelist == 4:
        print('Someone in your life needs a letter from you.')
    elif fortunelist == 5:
        print('Dont just think. Act!')
fortune()
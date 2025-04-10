
height = int(input('What is your height? '))
credits = int(input('What is your Credit? '))

if height > 137 and credits > 10:
    answer = 'Enjou the ride'
elif height < 137 and credits > 10:
    answer = 'You are too Short'
elif height > 137 and credits < 10:
    answer = 'You dont have enough credits'
else:
    answer = 'You are too short and dont have credits'

print(answer)
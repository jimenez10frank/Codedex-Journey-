pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

pesosToDollar = pesos / 0.49
solesToDollar = soles / 0.27
reaisToDollar = reais / 0.27

dollar = pesosToDollar + solesToDollar + reaisToDollar
print(dollar)
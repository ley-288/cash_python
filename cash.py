from cs50 import get_float

while True:
    euro = get_float("Change: ")
    if euro > 0.00:
        break

cents = round(euro * 100)
coins = 0
available = [25, 10, 5, 1]

for usable in available:
    while cents >= usable: # also the formula;  coins += cents // available
        cents -= usable    #                    cents %= available
        coins += 1

print (coins)


#50 > 25,10,5,1.. subract a usable from the cent -=.. then assign 1 coin from coin +=.
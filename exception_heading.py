x = 10
try:
    print(x)
except NameError:
    print("Something went wrong")
else:
    print("The 'try except' Is finished")

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

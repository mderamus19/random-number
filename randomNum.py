import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))
    for number in range(1, 6):
        if (number in my_randoms):
            print ("My randoms list contains: ",my_randoms)
        else:
            print("My randoms list does not contain: ",number)
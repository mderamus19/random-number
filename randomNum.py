import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))

for number in range(1, 6):
    value = False
    for ran_num in my_randoms:
        if number == ran_num:
            value = True
    if value == True:
        print ("My randoms list contains: ",number)
    else:
        print("My randoms list does not contain: ",number)

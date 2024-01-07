import random

dictionary = {"simple1" : [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
              "simple2" : [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10],
              "edge1" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]} #dict of generated test_cases

edge2 = []
edge3 = []
i = 10
while i<= 300:
    if i <= 99:
        edge2.append(i)
    else:
        edge3.append(i)

    i+=1
dictionary["edge2"] = edge2
dictionary["edge3"] = edge3

random1 = []
random2 = []
random3 = []
random4 = []
i = 1
while i <= 999:
    random4.append(random.randint(1, 300))
    if i <= 499:
        random3.append(random.randint(1, 300))
    if i <= 99:
        random2.append(random.randint(1, 300))
    if i <= 50:
        random1.append(random.randint(1, 300))
    i+=1
dictionary["random1"] = random1
dictionary["random2"] = random2
dictionary["random3"] = random3
dictionary["random4"] = random4

all3 = []
i = 1
while i<= 300:
    all3.append(i)
    all3.append(i)
    all3.append(i)
    i+=1
dictionary["all3"] = all3

with open("values.txt", "w") as file:
    file.write(str(dictionary))
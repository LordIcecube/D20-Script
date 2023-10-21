import random

while True:
    input ("Press the enter key to roll.")
    d20 = random.randint (1,20)
    print (d20)

    if d20 == 1 :
        print ("Critical Fail!")
    elif d20 == 20 :
        print ("Critical Hit!")

#Source: https://www.youtube.com/watch?v=4j3iljXn2EI&t=190s&ab_channel=BrianFediuk

#Github Link: 

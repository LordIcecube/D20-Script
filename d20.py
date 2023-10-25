import random #Transfers the random function.

while True: #While the Import random is true, the system will do these functions.
    input ("Press the enter key to roll.") #Input function only accepts enter key, so it will print a message promting the user while it looks for the keyboard input.
    d20 = random.randint (1,20) #Chooses random integer between 1 and 20, creates a d20 variable
    print (d20) #printing the function

    if d20 == 1 : #If d20 = 1, system prints a critical fail message.
        print ("Critical Fail!")
    elif d20 == 20 : #If d20 = 20, system prints a critical hit message.
        print ("Critical Hit!")

#Source: https://www.youtube.com/watch?v=4j3iljXn2EI&t=190s&ab_channel=BrianFediuk

#Github Link: https://github.com/LordIcecube/D20-Script/tree/main

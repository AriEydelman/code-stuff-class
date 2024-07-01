import random


print("Welcometo Alien Game !  ")
print("You have stolen a UFO to make your way across outer space.")
print("The aliens want there UFO back and are chasing you down !")
print("Survive and out run the Aliens!")

thirst = 0
traveld = 0
tierdness = 0
alias_traveld = -20
water_left = 3


done = False

while (done == False):

    y = random.randint(7,14)
    z = random.randint(10,20)
    w = random.randint(1,2)
    g = random.randint(6,12)
    k = random.randint(5,12)
    
    print("a.  drink water")
    print("b.  speed to medium")
    print("c.  full speed")
    print("d.  rest")
    print("e.  status check")
    print("q.  quit")

    x = input("what do you wana do? :  ")

    if x == "q":
        done = True
    
    elif x == "e":
        print("water", tierdness)
        print("water left",water_left)
        print("tierdness",tierdness)
        print("traveld",traveld)
        print("alians miels behind you",traveld-alias_traveld)
    
    elif x == "d":
        print("you are rested but the alians have been on the move when you slepted")
        alias_traveld += y

    elif x == "c":
        print("you went at full speed and went", z, "but you got thirsty by 1 and got tierd by", w , "the alians moved up", y  )
        traveld += z
        thirst += 1
        alias_traveld += y
        tierdness += w

    elif x == "c":
        print("you went at medium speed and went", k ,"but you got thirsty by 0.5 and got tiered by 1", "and the alians moved up", g)
        traveld += k
        thirst += 0.5
        alias_traveld += g
        tierdness += 1

    elif x == "a":
        if water_left
        print("you drank water and now your amount of water is", water_left, "but your thirst returned to 0")

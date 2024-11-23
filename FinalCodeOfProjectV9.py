Fulldeck=[]
#heartdeck=[2,3,4,5,6,7,8,9,10, "jack", "king", "queen", "ace"]
#diamonddeck=[2,3,4,5,6,7,8,9,10, "jack", "king", "queen", "ace"]
#spadedeck=[2,3,4,5,6,7,8,9,10, "jack", "king", "queen", "ace"]
#suitdeck=[2,3,4,5,6,7,8,9,10, "jack", "king", "queen", "ace"]
#Fulldeck.append(diamonddeck)                                      #commenting out after conducting testing
#Fulldeck.append(spadedeck)
#Fulldeck.append(suitdeck)
for x in range(4):
    #this is because each deck has suits, eg hearts, spades, clubs, and diamonds
    Fulldeck.append(2)
    Fulldeck.append(3)
    Fulldeck.append(4)
    Fulldeck.append(5)
    Fulldeck.append(6)
    Fulldeck.append(7)
    Fulldeck.append(8)
    Fulldeck.append(9)
    Fulldeck.append(10)
    Fulldeck.append(11)#jack is equivalent to 11
    Fulldeck.append(12)#queen is equivalet to 12
    Fulldeck.append(13)#king is equivalent to 13
    Fulldeck.append(100)#ace can represent 1 or 14 so we'll deal with it as this
#print(Fulldeck).......this is testing
import random
import time
import statistics
random.shuffle(Fulldeck)

def funkyy(p):
    
    file = open(p,"r")
    data = file.read()
    file.close()
    scores = data.split(",")
    scores.remove("")
    scores=[int(x) for x in scores]
    #print(scores)
    x=statistics.mean(scores)
    print("The mean of all scores is ",x,)
    testy=scores#configuring the data analysis without discombobulating the original list
    #print(testy)
    testy.sort()
    if len(testy)%2==0:
        m=len(testy)//2
        mm=(testy[m-1]+testy[m])/2
    else:
        y=len(testy)//2
        mm=testy[y]
    print("The median of all scores is",mm,)
    mode=statistics.mode(scores)
    print("The mode of all scores is",mode,)


def rules():
    #Introduction to the game
    print("Higher or lower game!")
    time.sleep(1)
    print("Welcome to the higher or lower game.")
    time.sleep(1)
    print("The rules of this game are simple, the computer model will shuffle a deck of cards and display one card to begin.\nYou will then be prompted to guess either higher or lower.")
    time.sleep(1)
    print("If the next card is what you guessed compared to the previous card, you get a point and the game continues. \nIf the card drawn is equal to the previous card, you still get a point and get to play on.")
    time.sleep(1)
    print("The jack is equal to 11, the Queen is equal to 12, the King is equal to 13, and i have coded the Ace to equal 100. \nHowever no matter what your guess is it will always be correct in relation to the Ace.")
    print("\t")


#print(Fulldeck)...........more testing
#Introduction to the game
rules()
while True:
    mode=input("Please select either singleplayer(s), multiplayer(m) or simulation(sm): ")
    if mode == "s":
        break
    elif mode == "m":
        break
    elif mode == "sm":
        break
    else:
        continue

if mode == "m":
    while True:
        name=input("Please enter your username player 1: ")#validity checking
        if name.isalpha():
            print("✔️")
            break
        else:
             print("Your username must only contain letters!")
             continue
        
    while True:
        age=input("Please enter your age in numeric form: ")#validity checking
        if age.isdigit():
            print("✔️")
            break
            
        else:
            print("Invalid information, please re-submit form")
            continue
             
    while True:
        gen=input("Please enter your gender, male or female: ")#validity checking
        if gen ==("male"):
            print("✔️")
            break
        elif gen ==("female"):
            print("✔️")
            break
        else:
            print("Invalid information, please re-submit form")
            continue
    #print(playa1)
    
    
    while True:
        namey=input("Please enter your username player 2: ")
        if namey.isalpha():
            print("✔️")
            break
        else:
            print("Your username must only contain letters!")
            continue
        #validation checking
    while True:
        agey=input("Please enter your age in numeric form: ")
        if agey.isdigit():
            print("✔️")
            break
        else:
            print("Invalid information, please re-submit form")
            continue
          #validation checking    
    while True:
        geny=input("Please enter your gender, male or female: ")
        if geny ==("male"):
            print("✔️")
            break
        elif geny ==("female"):
            print("✔️")
            break
        else:
            print("Invalid information, please re-submit form")
            continue
        #print(playa2)
         #validation checking
        #game mechanics
    cardindex1=0
    cardindex2=1
    scorep1=0
    scorep2=0
    while True:
        print(Fulldeck[cardindex1])
        while True:
            g1=input("Please enter your guess player 1, higher(h) or lower(l): ")
            if g1==("h"):
                break
            elif g1==("l"):
                break
            else:
                print("Invalid input")
                continue
        print(Fulldeck[cardindex2])
        
        if Fulldeck[cardindex1] == 100: #ace
            if g1 == "h":
                rs="h"
                
            elif g1 == "l":
                rs="l"
        if Fulldeck[cardindex2] == 100: #ace
            if g1 == "l":
                rs="l"
                
            elif g1 == "h":
                rs="h"
       
        elif Fulldeck[cardindex2] >= Fulldeck[cardindex1]:
            if Fulldeck[cardindex1] == 100: #ace
                if g1 == "h":
                    rs="h"
                elif g1 == "l":
                    rs="l"
            rs="h"
                
                
        elif Fulldeck[cardindex2] == Fulldeck[cardindex1]:
            if g1 == "l":
                rs="l"
            elif g1 == "h":
                rs="h"
        
        else:
            rs="l"
           
            
        if rs == g1:
            print("your guess was correct")
            scorep1+=1
          
        else:
            print("Unlucky ",name,", you guessed incorrect")
            print("Your score was",scorep1,)
            break
        Fulldeck.pop(cardindex1)
        cardindex1+=1
        cardindex2+=1
        
    while True:
        print(Fulldeck[cardindex1])
        while True:
            g1=input("Please enter your guess player 2, higher(h) or lower(l): ")
            if g1==("h"):
                break
            elif g1==("l"):
                break
            else:
                print("Invalid input")
                continue
        print(Fulldeck[cardindex2])
        
        if Fulldeck[cardindex1] == 100:#ace
            if g1 == "h":
                rs="h"
            
            elif g1 == "l":
                rs="l"
        if Fulldeck[cardindex2] == 100:#ace
            if g1 == "l":
                rs="l"
                
            elif g1 == "h":
                rs="h"
       
        elif Fulldeck[cardindex2] >= Fulldeck[cardindex1]:
            if Fulldeck[cardindex1] == 100:#ace
                if g1 == "h":
                    rs="h"
                elif g1 == "l":
                    rs="l"
            rs="h"
                
                
        elif Fulldeck[cardindex2] == Fulldeck[cardindex1]:#draw condidition
            if g1 == "l":
                rs="l"
            elif g1 == "h":
                rs="h"
        
        else:
            rs="l"
           
            
        if rs == g1:
            print("your guess was correct")
            scorep2+=1
          
        else:
            print("Unlucky ",namey,", you guessed incorrect")
            print("Your score was",scorep2,)
            break
        Fulldeck.pop(cardindex1)
        cardindex1+=1
        cardindex2+=1
        
    file = open("MP1Scores.csv","a")
    uu=str(scorep1)
    w=(uu+",")
    file.write(w)
    file.close()
    filey = open("MP2Scores.csv","a")
    u=str(scorep2)
    ww=(u+",")
    filey.write(ww)
    filey.close()
        
    if scorep1 > scorep2:
        print("Congratulations",name,",your score was higher than",namey,)
        print("You win!")
            
    elif scorep1 < scorep2:
        print("Congratulations",namey,",your score was higher than",name,)#different conditions
        print("You win!")
            
    else:
        print("Oh my! It appears that you scored a draw")
        print("Neither of you win")
        
        
        
    import matplotlib.pyplot as plt
    import numpy as np
    file = open("MP1Scores.csv","r")
    data = file.read()
    file.close()
    scoresy = data.split(",")#sorting out the data
    scoresy.remove("")
    scoresy=[int(x) for x in scoresy]
    print(scoresy)
    filey = open("MP2Scores.csv","r")
    datay = filey.read()
    filey.close()
    scores = datay.split(",")
    scores.remove("")
    scores=[int(x) for x in scores]
    print(scores)#calculating the axises
    twa=1
    goog=[]
    googy=[]
    ttwa=1
    for x in range(len(scores)):
        tt=twa
        hh=str(tt)
        goog.append(hh)
        twa+=1
    print(goog)
    goog_axis = np.arange(len(goog))
    plt.bar(goog_axis - 0.2, scores, 0.4, label = 'Player 2')
    plt.bar(goog_axis + 0.2, scoresy, 0.4, label = 'Player 1')
    plt.xticks(goog_axis, goog)
    plt.xlabel("Attempts")
    plt.ylabel("Scores")
    plt.title("Multiplayer Graph")
    plt.legend()
    plt.show()
    #graph
    blah=input("Please enter the file you want to read: ")
    funkyy(blah)
    blah=input("Please enter the file you want to read: ")
    funkyy(blah)
    #calling twice to input both mp1 and mp2 files


        
    
                
        
        
     
    
    
    
    
elif mode == "s":
    spl=[]
    while True:
        name=input("Please enter your username: ")
        if name.isalpha():
            print("✔️")
            break
        else:
            print("Your username must only contain letters!")
            continue
         #validation checking
        
    while True:
        age=input("Please enter your age in numeric form: ")
        if age.isdigit():
            print("✔️")
            break
        else:
            print("Invalid information, please re-submit form")
            continue
         #validation checking
    while True:
        gen=input("Please enter your gender, male or female: ")
        if gen ==("male"):
            print("✔️")
            break
        elif gen ==("female"):
            print("✔️")
            break
        else:
            print("Invalid information, please re-submit form")
            continue
             #validation checking
    
  
    
    #game mechanics
    cardindex1=0
    cardindex2=1
    score=0
    rs=""
  
    
    while True:
        print(Fulldeck[cardindex1])
        while True:
            g1=input("Please enter your guess, higher(h) or lower(l): ")
            if g1==("h"):
                break
            elif g1==("l"):
                break
            else:
                print("Invalid input")
                continue
        print(Fulldeck[cardindex2])
        
        if Fulldeck[cardindex1] == 100:
            if g1 == "h":
                rs="h"
                
            elif g1 == "l":
                rs="l"
        if Fulldeck[cardindex2] == 100:#ace
            if g1 == "l":
                rs="l"
                
            elif g1 == "h":
                rs="h"
       
        elif Fulldeck[cardindex2] >= Fulldeck[cardindex1]:
            if Fulldeck[cardindex1] == 100:#ace
                if g1 == "h":
                    rs="h"
                elif g1 == "l":
                    rs="l"
            rs="h"
                
                
        elif Fulldeck[cardindex2] == Fulldeck[cardindex1]:#draw condiditon
            if g1 == "l":
                rs="l"
            elif g1 == "h":
                rs="highe"
        
        else:
            rs="l"
           
            
        if rs == g1:
            print("your guess was correct")
            score+=1
            
          
        else:
            print("Unlucky ",name,", you guessed incorrect")
            print("Your score was",score,)
            break
        Fulldeck.pop(cardindex1)
        cardindex1+=1
        cardindex2+=1
        spl.append(score)
        
        
    file = open("SingleplayerScores.csv","a")
    uu=str(score)
    w=(uu+",")
    file.write(w)
    file.close()
    
    
    import matplotlib.pyplot as plt
    file = open("SingleplayerScores.csv","r")
    data = file.read()
    file.close()
    scores = data.split(",")
    scores.remove("")#sorting data again
    scores=[int(x) for x in scores]
    #print(scores)
    gos=len(scores)
    #print(gos)
    twa=1
    goog=[]
    for x in range(len(scores)):
        tt=twa
        hh=str(tt)
        goog.append(hh)
        twa+=1
    #print(goog)
    plt.bar(goog,scores)
    plt.title("Singleplayer Graph")
    plt.xlabel("Attempt Number")
    plt.ylabel("Scores")
    plt.show()
    blah=input("Please enter the file you want to read: ")

    funkyy(blah)
    #calling my data analysis function
    
        
   
elif mode == "sm":
    
    
    #game mechanics
    cardindex1=0
    cardindex2=1
    score=0
    rs=""
    guess=["higher","lower"]
    
    
    print()
    
    while True:
        print(Fulldeck[cardindex1])
        if (Fulldeck[cardindex1]) < 7:
            g1=guess[0]
            print(g1)
            time.sleep(1)
            print(Fulldeck[cardindex2])
        else:
            g1=guess[1]
            print(g1)
            time.sleep(1)
            print(Fulldeck[cardindex2])
            
        
        if Fulldeck[cardindex1] == 100:#ace
            if g1 == "higher":
                rs="higher"
                
            elif g1 == "lower":
                rs="lower"
        if Fulldeck[cardindex2] == 100:#ace
            if g1 == "lower":
                rs="lower"
                
            elif g1 == "higher":
                rs="higher"
       
        elif Fulldeck[cardindex2] >= Fulldeck[cardindex1]:
            if Fulldeck[cardindex1] == 100:#ace
                if g1 == "lower":
                    rs="lower"
                elif g1 == "higher":
                    rs="higher"
            rs="higher"
                
                
        elif Fulldeck[cardindex2] == Fulldeck[cardindex1]:#draw condition
            if g1 == "lower":
                rs="lower"
            elif g1 == "higher":
                rs="higher"
        
        else:
            rs="lower"
           
            
        if rs == g1:
            print("your guess was correct")#mechanics
            score+=1
          
        else:
            print("Unlucky computer, you guessed incorrect")
            print("Your score was",score,)
            break
        Fulldeck.pop(cardindex1)
        cardindex1+=1
        cardindex2+=1
        
    file = open("SimulationScores.csv","a")#csv file extraction
    uu=str(score)
    w=(uu+",")
    file.write(w)
    file.close()
    
    
    
    
    import matplotlib.pyplot as plt
    
    file = open("SimulationScores.csv","r")
    data = file.read()
    file.close()
    scores = data.split(",")
    scores.remove("")
    scores=[int(x) for x in scores]#more csv work with data
    print(scores)
    twa=1
    goog=[]
    for x in range(len(scores)):
        tt=twa
        hh=str(tt)
        goog.append(hh)
        twa+=1
    print(goog)
    plt.bar(goog,scores)
    plt.title("Simulation Graph")
    plt.xlabel("Attempt Number")
    plt.ylabel("Scores")
    plt.show()
    blah=input("Please enter the file you want to read: ")

    funkyy(blah)

    
   
        
    

else:
    print("Invalid selection, please try again")



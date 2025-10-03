# 1 - Import packages, libraries 
import pygame, pygwidgets, sys, random


# 2 - Define constants 
GEEN = (88,137,105)
REHD = 	(103,11,11)
WHITE = (255,255,255)
WHITish = (225,225,225)
WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 800
FPS = 30
 

# 3 - Initialise the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets - Images/Sounds

# 5 - Initialise Variables
turn = "Player"
rounds = 1
balance = 20
betamount = 0
playerSelected = ""
computerSelected = ""
allCards = ["2C", "2D", "2H", "2S", "3C", "3D", "3H", "3S", "4C", "4D", "4H", "4S", "5C", "5D", "5H", "5S",
            "6C", "6D", "6H", "6S", "7C", "7D", "7H", "7S", "8C", "8D", "8H", "8S", "9C", "9D", "9H", "9S",
            "10C", "10D", "10H", "10S", "AC", "AD", "AH", "AS", "JC", "JD", "JH", "JS", "KC", "KD", "KH", "KS", "QC", "QD", "QH", "QS"]

selectedCards = random.sample(allCards, k=5)
selectedCards.append("cheese")
random.shuffle(selectedCards)

title = pygwidgets.DisplayText(window, (555, 50), "Find The Cheese",  fontName= "bodoni", fontSize= 35, textColor=REHD)
buttonStart = pygwidgets.TextButton(window, (575, 120), "Start", width= 100, fontName="bodoni", fontSize= 25, textColor= REHD, upColor=WHITE, overColor=WHITish )
roundes = pygwidgets.DisplayText(window, (100,120), f"Rounds: {rounds}", fontName= "bodoni", fontSize= 25, textColor=REHD)
balanceText = pygwidgets.DisplayText(window, (1000,120), f"Balance: ${balance}", fontName= "bodoni", fontSize= 25, textColor=REHD)
whosTurnIsIt = pygwidgets.DisplayText(window, (100, 170), f"Turn: {turn}",  fontName= "bodoni", fontSize= 25, textColor=REHD)
playNext = pygwidgets.TextButton(window, (545,655),"Next Round", width=200, fontName= "bodoni", fontSize= 25, textColor=REHD, height=50, upColor=WHITE, overColor=WHITish )
getOUTUTUUTUT = pygwidgets.TextButton(window, (900, 50), "GET OUT!",  fontName= "bold", fontSize= 60, textColor=REHD)
getOUT = pygwidgets.Image(window, (0, 100), "cardsImages/getOUT.jpg")
noMoney = pygwidgets.Image(window, (0, 100), "cardsImages/nomoney.jpg")
cardOne = pygwidgets.Image(window, (50,350), f"cardsImages/backcard.jpg")
cardTwo = pygwidgets.Image(window, (250,350), f"cardsImages/backcard.jpg")
cardThree = pygwidgets.Image(window, (450,350), f"cardsImages/backcard.jpg")
cardFour = pygwidgets.Image(window, (650,350), f"cardsImages/backcard.jpg")
cardFive = pygwidgets.Image(window, (850,350), f"cardsImages/backcard.jpg")
cardSix = pygwidgets.Image(window, (1050,350), f"cardsImages/backcard.jpg")
winText = pygwidgets.DisplayText(window, (500,700), "",  fontName= "bodoni", fontSize= 25, textColor=REHD)
howMuchYouWantLoseQuePasa = pygwidgets.DisplayText(window, (100,250), "How much of your lifespan's money would you like to waste?", fontName= "bodoni", fontSize= 25, textColor=REHD)
howMuchYouWantLose = pygwidgets.InputText(window, (820, 250), fontName= "bodoni", fontSize= 25, textColor=REHD, backgroundColor=WHITE)
p2wButton = pygwidgets.TextButton(window, (1090, 245), "Play 2 Win", fontName= "bodoni", fontSize= 25, textColor=REHD)
playerWin = pygwidgets.DisplayText(window, (500, 200), "PLAYER WINS", fontName= "bodoni", fontSize= 50, textColor=REHD)
computerWin = pygwidgets.DisplayText(window, (455, 200), "COMPUTER WINS", fontName= "bodoni", fontSize= 50, textColor=REHD)
comPick = pygwidgets.DisplayText(window, (0,0), "", fontName= "bodoni", fontSize= 20, textColor=WHITish)
playerPick = pygwidgets.DisplayText(window, (0,0), "", fontName= "bodoni", fontSize= 20, textColor=WHITish)

gamestate = "introcheebs"
# 6 - Look forever
while True:

    # 7 - check and handle for events
    for event in pygame.event.get():

        # Clicked the close button? 2 pygame and end program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

        if getOUTUTUUTUT.handleEvent(event):
            pygame.quit()
            sys.exit()

        if buttonStart.handleEvent(event):
            gamestate= "coolplayguytime"

        if howMuchYouWantLose.handleEvent(event):
            betamount = howMuchYouWantLose.getValue()

        if p2wButton.handleEvent(event) and int(betamount) > 0 and int(betamount) <= balance:
            gamestate="playerselect"
            balance = balance -  int(betamount)
            balanceText.setValue(f"Balance: ${balance}")
            howMuchYouWantLose.setValue("")

        if cardOne.handleEvent(event) and gamestate == "playerselect":
            cardOne = pygwidgets.Image(window, (50,350), f"cardsImages/{selectedCards[0]}.jpg") 
            playerPick = pygwidgets.DisplayText(window, (80,620), "Player's Pick", fontName= "bodoni", fontSize= 20, textColor=WHITish)
            if selectedCards[0] == "cheese":
                gamestate = "playerselectedcheese"
                playerPick.show()
            else:
                playerSelected = selectedCards[0]
                gamestate = "computerselect"
                turn = "Computer"
                comPick.show()

        if cardTwo.handleEvent(event) and gamestate == "playerselect":
            cardTwo = pygwidgets.Image(window, (250,350), f"cardsImages/{selectedCards[1]}.jpg") 
            playerPick = pygwidgets.DisplayText(window, (280,620), "Player's Pick", fontName= "bodoni", fontSize= 20, textColor=WHITish)
            if selectedCards[1] == "cheese":
                gamestate = "playerselectedcheese"
                playerPick.show()
            else:
                playerSelected = selectedCards[1]
                gamestate = "computerselect"
                turn = "Computer"
                comPick.show()

        if cardThree.handleEvent(event) and gamestate == "playerselect":
            cardThree = pygwidgets.Image(window, (450,350), f"cardsImages/{selectedCards[2]}.jpg")
            playerPick = pygwidgets.DisplayText(window, (480,620), "Player's Pick", fontName= "bodoni", fontSize= 20, textColor=WHITish)
            if selectedCards[2] == "cheese":
                gamestate = "playerselectedcheese"
                playerPick.show()
            else:  
                playerSelected = selectedCards[2]
                gamestate = "computerselect"
                turn = "Computer"
                comPick.show()

        if cardFour.handleEvent(event) and gamestate == "playerselect":
            cardFour = pygwidgets.Image(window, (650,350), f"cardsImages/{selectedCards[3]}.jpg") 
            playerPick = pygwidgets.DisplayText(window, (680,620), "Player's Pick", fontName= "bodoni", fontSize= 20, textColor=WHITish)
            if selectedCards[3] == "cheese":
                gamestate = "playerselectedcheese"
                playerPick.show()
            else:
                playerSelected = selectedCards[3] 
                gamestate = "computerselect"
                turn = "Computer"  
                comPick.show()     

        if cardFive.handleEvent(event) and gamestate == "playerselect":
            cardFive = pygwidgets.Image(window, (850,350), f"cardsImages/{selectedCards[4]}.jpg")
            playerPick = pygwidgets.DisplayText(window, (880,620), "Player's Pick", fontName= "bodoni", fontSize= 20, textColor=WHITish)
            if selectedCards[4] == "cheese":
                gamestate = "playerselectedcheese"
                playerPick.show()
            else:
                playerSelected = selectedCards[4]
                gamestate = "computerselect"
                turn = "Computer"
                comPick.show()

        if cardSix.handleEvent(event) and gamestate == "playerselect":
            cardSix = pygwidgets.Image(window, (1050,350), f"cardsImages/{selectedCards[5]}.jpg")
            playerPick = pygwidgets.DisplayText(window, (1080,620), "Player's Pick", fontName= "bodoni", fontSize= 20, textColor=WHITish)
            if selectedCards[5] == "cheese":
                gamestate = "playerselectedcheese"
                playerPick.show()
            else:
                playerSelected =selectedCards[5]       
                gamestate = "computerselect"
                turn = "Computer"
                comPick.show()

        if playNext.handleEvent(event):
            rounds = rounds+1
            roundes.setValue(f"Rounds: {rounds}")
            cardOne.hide()
            cardTwo.hide()
            cardThree.hide()
            cardFour.hide()
            cardFive.hide()
            cardSix.hide()
            gamestate = "introcheebs"

                 

        
    
    if gamestate == "introcheebs":
        selectedCards = random.sample(allCards, k=5)
        selectedCards.append("cheese")
        random.shuffle(selectedCards)
        cardOne = pygwidgets.Image(window, (50,350), f"cardsImages/backcard.jpg")
        cardTwo = pygwidgets.Image(window, (250,350), f"cardsImages/backcard.jpg")
        cardThree = pygwidgets.Image(window, (450,350), f"cardsImages/backcard.jpg")
        cardFour = pygwidgets.Image(window, (650,350), f"cardsImages/backcard.jpg")
        cardFive = pygwidgets.Image(window, (850,350), f"cardsImages/backcard.jpg")
        cardSix = pygwidgets.Image(window, (1050,350), f"cardsImages/backcard.jpg")
        cardOne.hide()
        cardTwo.hide()
        cardThree.hide()
        cardFour.hide()
        cardFive.hide()
        cardSix.hide()
        howMuchYouWantLose.hide()
        howMuchYouWantLoseQuePasa.hide()
        p2wButton.hide()
        whosTurnIsIt.show()
        playNext.hide()
        playerWin.hide()
        computerWin.hide()
        buttonStart.show()
        whosTurnIsIt.setValue(f"Turn: Player")
        winText.hide()
        comPick.hide()
        playerPick.hide()
        noMoney.hide()
        getOUT.hide()
        getOUTUTUUTUT.hide()
        

    if gamestate == "coolplayguytime":
       
        howMuchYouWantLose.show()
        howMuchYouWantLoseQuePasa.show()
        p2wButton.show()
        whosTurnIsIt.show()
        buttonStart.hide()

    if gamestate == "playerselect":
        cardOne.show()
        cardTwo.show()
        cardThree.show()
        cardFour.show()
        cardFive.show()
        cardSix.show()
        howMuchYouWantLose.hide()
        howMuchYouWantLoseQuePasa.hide()
        p2wButton.hide()

    if gamestate == "playerselectedcheese":
       
        balance = balance + (int(betamount)*3)
        balanceText.setValue(f"Balance: ${balance}")
        gamestate = "nextround"
       
    if gamestate == "nextround":
        playNext.show()
        winText.show()
        winText.setValue("You picked the cheese card!!!!!!!")
        
       

        
       
    if gamestate == "computerselect":
        whosTurnIsIt.setValue(f"Turn: {turn}")
        computerSelected = random.choice(selectedCards)
        if computerSelected == playerSelected:
            gamestate = "computerselect"
        else:   
            gamestate = "winnercheck"
          
            if computerSelected == selectedCards[0] : 
                cardOne = pygwidgets.Image(window, (50,350), f"cardsImages/{selectedCards[0]}.jpg") 
                comPick = pygwidgets.DisplayText(window, (70,620), "Computer's Pick", fontName= "bodoni", fontSize= 20, textColor=WHITish)
            if computerSelected == selectedCards[1]:
                cardTwo = pygwidgets.Image(window, (250,350), f"cardsImages/{selectedCards[1]}.jpg") 
                comPick = pygwidgets.DisplayText(window, (270,620), "Computer's Pick", fontName= "bodoni", fontSize= 20, textColor=WHITish)
            if computerSelected == selectedCards[2]:
                cardThree = pygwidgets.Image(window, (450,350), f"cardsImages/{selectedCards[2]}.jpg")
                comPick = pygwidgets.DisplayText(window, (470,620), "Computer's Pick", fontName= "bodoni", fontSize= 20, textColor=WHITish)
            if computerSelected == selectedCards[3]:
                cardFour = pygwidgets.Image(window, (650,350), f"cardsImages/{selectedCards[3]}.jpg") 
                comPick = pygwidgets.DisplayText(window, (670,620), "Computer's Pick", fontName= "bodoni", fontSize= 20, textColor=WHITish)
            if computerSelected == selectedCards[4]:
                cardFive = pygwidgets.Image(window, (850,350), f"cardsImages/{selectedCards[4]}.jpg")
                comPick = pygwidgets.DisplayText(window, (870,620), "Computer's Pick", fontName= "bodoni", fontSize= 20, textColor=WHITish)
            if computerSelected == selectedCards[5]:
                cardSix = pygwidgets.Image(window, (1050,350), f"cardsImages/{selectedCards[5]}.jpg")
                comPick = pygwidgets.DisplayText(window, (1070,620), "Computer's Pick", fontName= "bodoni", fontSize= 20, textColor=WHITish)


    if gamestate == "winnercheck":
        if computerSelected != "cheese":
           
            if allCards.index(computerSelected) > allCards.index(playerSelected):
                
                computerWin.show()
                gamestate = "winnerscreen"
            else:
              
                playerWin.show()
                balance = balance + (int(betamount)*3)
                balanceText.setValue(f"Balance: ${balance}")
            gamestate = "winnerscreen"
        else :
            
            computerWin.show()
            gamestate = "winnerscreen"

    if  gamestate == "winnerscreen":
         playNext.show()

    if balance <= 0 and gamestate == "introcheebs":
        gamestate = "getkickedoutbozo" 

    if gamestate == "getkickedoutbozo":
        cardOne.hide()
        cardTwo.hide()
        cardThree.hide()
        cardFour.hide()
        cardFive.hide()
        cardSix.hide()
        buttonStart.hide()
        roundes.hide()
        balanceText.hide()
        howMuchYouWantLose.hide()
        howMuchYouWantLoseQuePasa.hide()
        p2wButton.hide()
        whosTurnIsIt.hide()
        playNext.hide()
        title.setValue("Get Kicked Out Bozo")
        noMoney.show()
        getOUT.show()
        getOUTUTUUTUT.show()

        
        
        
   

 
       

        

    
        
    
            


        
        

        


    # 8 - Do any "per frame" actions


    # 9 - Clear the window 
    window.fill(GEEN)

    # 10 - Draw all window elements
    cardOne.draw()
    cardTwo.draw()
    cardThree.draw()
    cardFour.draw()
    cardFive.draw()
    cardSix.draw()
    title.draw()
    buttonStart.draw()
    roundes.draw()
    balanceText.draw()
    howMuchYouWantLose.draw()
    howMuchYouWantLoseQuePasa.draw()
    p2wButton.draw()
    whosTurnIsIt.draw()
    winText.draw()
    playNext.draw()
    playerWin.draw()
    computerWin.draw()
    comPick.draw()
    playerPick.draw()
    getOUT.draw()
    noMoney.draw()
    getOUTUTUUTUT.draw()
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down

    clock.tick(FPS)



# "introcheebs" ---> click on start button ----> "coolplayguytime" ---> betamount and click on play ---> "playerselect"
# player can select the card and if it was cheese card ---> "playerselectedcheese" ---> "nextround"---> you click on next round button ---> "introcheebs"
#                 if it was not a cheesecard          ----> "computerselect" ---> "winnercheck" ---> "winnerscreen" ---> "nextround"---> you click on next round button ---> "introcheebs"

# homework : Add text right under the cards: computer picked this, player picked this
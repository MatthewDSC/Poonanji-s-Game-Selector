import random

def newlist():
    gameslist = []
    numberOfGames = input("How many games do you want to pick from? ")
    gamesnumber = int(numberOfGames)

    for i in range(gamesnumber):
         gameslist.append(input("Enter a game: "))
    print("New list created successfully. ")
    return gameslist

def choosegame(listofgames):
    selectedGame = random.choice(listofgames)
    print(selectedGame + " won.")
    return selectedGame

print("Welcome to Poonanji's game selector. For a list of commands, type 'help'.\nFirst, create a new list. ")
currentlist = newlist()
while 1 == 1 : 
        if len(currentlist) < 2:
            print("You need more than one game in your list.")
            currentlist = newlist()
            
        else:
            userinput = input("Enter command: ")

            if userinput == "help":
                print("Here's a list of commands:\nnew\nchoose\nexit" )

            elif userinput == "new":
                currentlist = newlist()

            elif userinput == "choose":
                veto = "y"
                while veto == "y":
                    selectedGame = choosegame(currentlist)
                    veto = input("Does anyone veto " + selectedGame + " ? y/n ")
                    if veto == "y":
                            makenewlistquestion = input("Select from a new list? y/n ")
                            if makenewlistquestion == "y":
                                currentlist = newlist()
    
            elif userinput == "exit":
                exit()
        


        

    





#-- This code is written by Shubham Lingayat (www.github.com/shubhzz5/)
# This Python program is used to calculate "Man of The Match" in cricket

#Points are assigned for individual player initially it is zero
points = 0 

#batting function is defined
def batting (runs,four,six,balls,field):
    "runs = Total runs by player, four = Fours by player, six = Sixers by player "
    "balls = total number of balls played by player, field = total fielding wickets"
    
    #initially points are zero for a player    
    points = 0
    #1 point for two runs
    points = runs/2
    
    #5 points for half century
    #additionaly 10 points of for a century
    if runs>=50:
        points = points + 5
        if runs>=100:
            points = points + 10
    
    #strike rate is calculated by total runs made by player divide by number of balls played by player multiply by 100
    strike_rate = (runs/balls)*100
    
    #2 points for strike rate greater than or equal to 80
    #additionaly 4 points for strike rate is greater than 100
    if strike_rate>=80:
        points = points + 2
        if strike_rate>100:
            points = points + 4
            
    #1 point for each boundary play (four runs)
    #2 points for each sixer
    #10 points for making each run-out/catch-out opponent player in the fielding
    points = points + four
    points = points + (six*2)
    points = points + (field*10)
    
    #return the points of player by batting function
    return points

#bowling function is defined
def bowling (wkts,overs,runs,field):
    "wkts = Wickets, overs = Total over, runs = Total run, field = total fielding wickets"
    
    #initially points of player is zero
    points = 0
    #10 points for each wicket
    points = points + (10*wkts)
    
    #5 points for 3 wickets
    #additionally 10 points for 5 wickets
    if wkts>=3:
        points = points + 5
        if wkts>=5:
            points = points + 10
            
    #economy rate is calculated by total number of runs divide by total overs played by player
    economy_rate = runs/overs
    
    #4 points for economy rate between 3.5 and 4.5
    #7 points for economy rate between 2 and 3.5
    #10 points for economy rate less than 2
    if (economy_rate<=4.5) & (economy_rate>=3.5):
        points = points + 4 
    elif (economy_rate<3.5) & (economy_rate>=2):
        points = points + 7  
    elif (economy_rate<2):
        points = points + 10
    
    #10 points for making each run-out/catch-out/stump-out opponent player in the fielding
    points = points + (field*10)  
    
    #return the points of player by bowling function
    return points

#get the number of players to input from user 
num = int(input("Enetr number of players: "))

#dictionary is created to save player information
player = {}

#dictionary is created to save player name and there respective points
player_points = {}

#for loop is created to get input of multiple players 
for i in range(num):
    #get the inputs from user
    name = input("Enter player name: ")
    role = input("Enter player Role (bat/bowl): ")
    #inputs are assigned in the player dictionary
    player["Name"] = name
    player["Role"] = role
    
    #if in the input player Role is batting (bat) then take belwo inputs from user
    if player["Role"] == "bat":
        runs = int(input("Enter the Runs made by player: "))
        four = int(input("Enetr the number of Foures made by player: "))
        six = int(input("Enter the number of sixers made by player: "))
        balls = int(input("Enter number of balls played by player: "))
        field = int(input("Enetr the number of wickets taken by player in the fielding: "))
        print("\n")
        #inputs are assigned in the player dictionary
        player["Runs"] = runs
        player["Four"] = four
        player["Six"] = six
        player["Balls"] = balls
        player["Field"] = field
        
        #batting function is called to calculate each player points
        x = batting(player["Runs"],player["Four"],player["Six"],player["Balls"],player["Field"])
        #points of each player with respective player name is assigned to player_points dictionary
        player_points[name] = x
    
    #if in the input player Role is bowling (bowl) then take belwo inputs from user
    elif player["Role"] == "bowl":
        wkts = int(input("Enetr the total number of wickets taken by player: "))
        overs = int(input("Enter the total number of overs played by player: "))
        runs = int(input("Enter the total number of runs made by opponent player: "))
        field = int(input("Enetr the number of wickets taken by player in the fielding: "))
        print("\n")
        #inputs are assigned in the player dictionary
        player["Wkts"] = wkts
        player["Overs"] = overs
        player["Runs"] = runs
        player["Field"] = field
        
        #bowling function is called to calculate each player points
        y = bowling(player["Wkts"],player["Overs"],player["Runs"],player["Field"])
        #points of each player with respective player name is assigned to player_points dictionary
        player_points[name] = y
        
    #else block if the given input is incorrect
    else:
        print("Please enter \"bat\" or \"bowl\".")

#print the dictionary which conatains player names and there respective points
print(player_points,"\n")

#print the final output
print("Man of the Match: ", list(player_points.keys())
      [list(player_points.values()).index(max(player_points.values()))])

# ---- Thank You ---- #

# default inputs are:
    # Enetr number of players: 5
    # Enter player name: Virat Kohli
    # Enter player Role (bat/bowl): bat
    # Enter the Runs made by player: 112
    # Enetr the number of Foures made by player: 10
    # Enter the number of sixers made by player: 0
    # Enter number of balls played by player: 119
    # Enetr the number of wickets taken by player in the fielding: 0
    
    # Enter player name: du Plessis
    # Enter player Role (bat/bowl): bat
    # Enter the Runs made by player: 120
    # Enetr the number of Foures made by player: 11
    # Enter the number of sixers made by player: 2
    # Enter number of balls played by player: 112
    # Enetr the number of wickets taken by player in the fielding: 0
    
    # Enter player name: Bhuvneshwar Kumar
    # Enter player Role (bat/bowl): bowl
    # Enetr the total number of wickets taken by player: 1
    # Enter the total number of overs played by player: 10
    # Enter the total number of runs made by opponent player: 45
    # Enetr the number of wickets taken by player in the fielding: 1
    
    # Enter player name: Yuzvendra Chahal
    # Enter player Role (bat/bowl): bowl
    # Enetr the total number of wickets taken by player: 2
    # Enter the total number of overs played by player: 10
    # Enter the total number of runs made by opponent player: 23
    # Enetr the number of wickets taken by player in the fielding: 0
    
    # Enter player name: Kuldeep Yadav
    # Enter player Role (bat/bowl): bowl
    # Enetr the total number of wickets taken by player: 3
    # Enter the total number of overs played by player: 10
    # Enter the total number of runs made by opponent player: 15
    # Enetr the number of wickets taken by player in the fielding: 0
    
# defaults output is:
    # {'Virat Kohli': 83.0, 'du Plessis': 96.0, 'Bhuvneshwar Kumar': 24, 'Yuzvendra Chahal': 27, 'Kuldeep Yadav': 45}
    
    # Man of the Match:  du Plessis
    
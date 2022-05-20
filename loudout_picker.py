# Call of Duty: Warzone loudout randomizer based on the user's playstyle.
import random



def get_loadout():
    run_and_gun = ["Mac10", "PPSH", "Milano", "XM4"]
    run_and_gun_equipment = ["Throwing Knife", "Snap-shot Grenade", "Flash Bang", "Stun Grenade"]
    run_and_gun_counter = 0

    cower_and_hide = ["Street-Sweeper", "Riot Shield", "RPG", "Gallo12"]
    cower_and_hide_equipment = ["Heartbeat Sensor", "Bouncy Betty Mine", "Claymore Mine"]
    cower_and_hide_counter = 0

    team_player = ["Bren LMG", "MG42", "Kar98K", "Krig6"]
    team_player_equipment = ["Snap-shot Grenade", "C4", "Smoke Grenade"]
    team_player_counter = 0

    long_range = ["kar98k", "Swiss", "ZRG", "SPR"]
    long_range_equipment = ["Smoke Grenade", "Claymore", "Stim Pack"]
    long_range_counter = 0
    playagain = True

    while playagain == True:
        try:
            choice_a =input("Do you run towards the sound of gunfire?\n>>>").lower()
            if choice_a == "yes":
                run_and_gun_counter += 1.5
                team_player_counter += .8
            if choice_a == "no":
                cower_and_hide_counter += .3 
                long_range_counter += .3 
        except:
            print("invalid input")         

        choice_c =input("Do you feel teamwork is critical to your success?\n>>>").lower()
        if choice_c == "yes":
            team_player_counter += 1.4
            long_range_counter += .5
        if choice_c == "no":
            run_and_gun_counter +=.2
            cower_and_hide_counter +=.3

        choice_d =input("Do you continue to loot while your teammates are actively in a gunfight?\n>>>").lower()
        if choice_d == "yes":
            cower_and_hide_counter +=1.3
            long_range_counter +=.6
        if choice_d == "no":
            run_and_gun_counter +=.2
            team_player_counter +=.3  

        choice_f =input("Do you prefer a more tactical approach to a gunfight?\n>>>").lower()
        if choice_f == "yes":
            long_range_counter += 1.6
            team_player_counter += .7

        if choice_f == "no":
            run_and_gun_counter +=.3
            cower_and_hide_counter +=.2

        choice_g =input("Do you share your ammunition and armor with your teammates?\n>>>").lower()   
        if choice_g == "yes":
            team_player_counter + 1.9
            long_range_counter + .9
        if choice_g == "no":
            cower_and_hide_counter + .6
            run_and_gun_counter + .4     

        print(run_and_gun_counter)
        print(cower_and_hide_counter)
        print(long_range_counter)
        print(team_player_counter)

        if run_and_gun_counter > long_range_counter and run_and_gun_counter > cower_and_hide_counter and run_and_gun_counter > team_player_counter:
            primary =  random.choice(run_and_gun)
            equipment = random.choice(run_and_gun_equipment)
            print("You are a run and gun style player. Shoot first, ask questions later! Here is your suggested loadout:\n ") 
            print("Weapon: " + primary)
            print("Equipment: " + equipment)  
        
        elif long_range_counter > run_and_gun_counter and long_range_counter > team_player_counter and long_range_counter > cower_and_hide_counter:
            primary = random.choice(long_range)
            equipment = random.choice(long_range_equipment)
            print("You are a Sniper support player.  All perched up in your little nest of saftey.  Here is your suggested loadout:\n ") 
            print("Weapon: " + primary)
            print("Equipment: " + equipment)

        elif cower_and_hide_counter > run_and_gun_counter and cower_and_hide_counter > long_range_counter and cower_and_hide_counter > team_player_counter:
            primary = random.choice(cower_and_hide)
            equipment = random.choice(cower_and_hide_equipment)
            print("You like to cower and hide.  Bro....  MAN UP SOLDIER!  Here is your suggested loadout:\n ") 
            print("Weapon: " + primary)
            print("Equipment: " + equipment)

        elif team_player_counter > long_range_counter and team_player_counter > cower_and_hide_counter and team_player_counter > run_and_gun_counter:
            primary = random.choice(team_player)
            equipment = random.choice(team_player_equipment)
            print("You are a team player.  The best kind of player!  Here is your suggested loadout:\n  ")
            print("Weapon: " + primary)
            print("Equipment: " + equipment)
        
        quit = input("\nEnter [q] to quit or [y] to run again: \n>>>").lower()
        if quit == "q":
            playagain = False
            print("quitting......")
            break
        elif quit =="y": 
            print("Ok, lets go one more time.")
            get_loadout()
        else:
            print("Invalid input")    









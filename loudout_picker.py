# Call of Duty: Warzone loudout randomizer based on the user's playstyle.
import random
import sys





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

    long_range = ["kar98k", "Swiss Sniper Rifle", "ZRG Sniper Rifle", "SPR Sniper Rifle"]
    long_range_equipment = ["Smoke Grenade", "Claymore", "Stim Pack"]
    long_range_counter = 0
    play_again = True

    while play_again == True:
        try:
            choice_a =int(input("Do you run towards the sound of gunfire? [1]=yes, [2]=no\n>>>"))
            if choice_a == 1:
                run_and_gun_counter += 1.5
                team_player_counter += .8
            if choice_a == 2:
                cower_and_hide_counter += .3 
                long_range_counter += .3   
        except ValueError:
            print("Invalid input. Please enter [1] for yes or [2] for no.")    
            continue

        try:
            choice_c =int(input("Do you feel teamwork is critical to your success? [1]=yes, [2]=no\n>>>"))
            if choice_c == 1:
                team_player_counter += 2
                long_range_counter += .5
            if choice_c == 2:
                run_and_gun_counter +=.2
                cower_and_hide_counter +=.3
        except ValueError: 
            print("Invalid input.  Please enter [1] for yes or [2] for no.")  
            continue 
            
        try:
            choice_d =int(input("Do you continue to loot while your teammates are actively in a gunfight? [1]=yes, [2]=no\n>>>"))
            if choice_d == 1:
                cower_and_hide_counter +=1.3
                long_range_counter +=.6

            if choice_d == 2:
                run_and_gun_counter +=.2
                team_player_counter +=.3 
        except ValueError:
            print("Invalid input.  Please enter [1] for yes or [2] for no.")  
            continue

        try:
            choice_f =int(input("Do you prefer a more tactical approach to a gunfight? [1]=yes, [2]=no\n>>>"))
            if choice_f == 1:
                long_range_counter += 1.6
                team_player_counter += .7

            if choice_f == 2:
                run_and_gun_counter +=.3
                cower_and_hide_counter +=.2
        except ValueError:
            print("Invalid input.  Please enter [1] for yes or [2] for no.")
            continue
        
        try:
            choice_g =int(input("Do you share your ammunition and armor with your teammates? [1]=yes, [2]=no\n>>>"))
            if choice_g == 1:
                team_player_counter + 1.9
                long_range_counter + .9

            if choice_g == 2:
                cower_and_hide_counter + .6
                run_and_gun_counter + .4 
        except ValueError:
            print("Invalid input.  Please enter [1] for yes or [2] for no.") 
            continue    

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

        try:
            quit = int(input("\nEnter [1] to quit or [2] to run again: \n>>>"))
            if quit == 1:
                play_again = False
                print("quitting......")
                sys.exit()
            
            elif quit ==2: 
                print("Ok, lets go one more time.")
                get_loadout()
            else:
                print("Invalid input.  Please enter [1] for yes or [2] for no.") 
        except ValueError:
            print("Invalid input.  Please enter [1] for yes or [2] for no.")

get_loadout()            









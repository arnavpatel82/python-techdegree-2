from constants import PLAYERS
from constants import TEAMS


def clean_height(height):
    """ cleans up player height by changing it into an integer value """ 

    height = int(height.replace(' inches', ''))

    return height


def clean_experience(experience_level):
    """ cleans up player experience level by changing it into an boolean value """ 

    if experience_level == 'YES':
            experience_level = True 
    else:
        experience_level = False

    return experience_level


def clean_guardians(guardians):
    """ cleans up player guardians by changing the string of guardians to a list """

    guardian_list = guardians.split(' and ')

    return guardian_list


def clean_data(player_list):
    """cleans up the player list"""

    for dic in player_list:
       dic['height'] = clean_height(dic['height'])
       dic['experience'] = clean_experience(dic['experience'])
       dic['guardians'] = clean_guardians(dic['guardians'])

        
def balance_teams(team_list, player_list):
    """balances the experienced and inexperienced players across the three teams equally"""

    team_dict = {}
    team_temp = team_list.copy()

    players_temp = player_list.copy()

    experienced_players = []
    inexperienced_players = []

    for i in players_temp:
        if i['experience'] == True:
            experienced_players.append(i)
        
        elif i['experience'] == False:
            inexperienced_players.append(i)
            
    exp_players_per_team = int(len(experienced_players) / len(team_list))
    inexp_players_per_team = int(len(inexperienced_players) / len(team_list))

    for team in team_temp:
        team_dict[team] = []

    start1 = 0
    stop1 = exp_players_per_team

    start2 = 0
    stop2 = inexp_players_per_team

    for team in team_temp:
        for i in range(start1, stop1):
            team_dict[team].append(experienced_players[i])
        start1 += exp_players_per_team
        stop1 += exp_players_per_team

        for i in range(start2, stop2):
            team_dict[team].append(inexperienced_players[i])
        start2 += inexp_players_per_team
        stop2 += inexp_players_per_team

    return team_dict, exp_players_per_team, inexp_players_per_team


def main():
    players_copy = PLAYERS.copy()
    teams_copy = TEAMS.copy()

    clean_data(players_copy)
    balanced_list, exp_per_team, inexp_per_team = balance_teams(teams_copy, players_copy)
    print("")
    print("BASKETBALL TEAM STATS TOOL")
    print("")

    while True:
        print("---- MENU----")
        print("")
        print("Here are your choices:")
        print(" 1) Display Team Stats")
        print(" 2) Quit")
        print("")
        
        choice = input("Enter an option >")
        if choice == 'Quit' or choice == '2':
            break

        elif choice == 'Display Team Stats' or choice == '1':
            count = 1
            for team in balanced_list:
                print(f"{count}) {team}")
                count = count + 1
            
            team_choice = input("Enter an option >")
            
            while True:
                if team_choice.isdigit() == False or int(team_choice) not in range(1, len(balanced_list) + 1):
                    print("you must enter a number within the correct range")
                    team_choice = input("Enter an option >")
                    continue
                else:
                    break
            
            listified_team = list(balanced_list)
            print("")
            total_players = len(balanced_list[listified_team[int(team_choice) - 1]])

            print(f"Team: {listified_team[int(team_choice) - 1]}")
            print("--------------------")
            print(f"Total players: {total_players}")
            print(f"Total experienced: {exp_per_team}")
            print(f"Total inexperienced: {inexp_per_team}")

            total_height = 0

            for i in balanced_list[listified_team[int(team_choice) - 1]]:
                total_height = total_height + i['height']

            average_height = total_height / total_players

            print(f"Average height: {average_height}")

            string_of_names = ""

            for i in balanced_list[listified_team[int(team_choice) - 1]]:
                string_of_names = string_of_names + i['name'] + ', '
            
            string_of_names = string_of_names[:-2]
            
            print("")
            print("Players:")
            print(string_of_names)

            list_of_guardians = []

            for i in balanced_list[listified_team[int(team_choice) - 1]]:
                list_of_guardians = list_of_guardians + i['guardians']

            print("")
            print("Guardians:")
            print(', '.join(list_of_guardians))
            print("")

        else:
            print("")
            print("you must enter a number within the correct range")
            continue




if __name__ == "__main__":

    # players_copy = PLAYERS.copy()
    # teams_copy = TEAMS.copy()

    # clean_data(players_copy)
    # balanced_list, exp_per_team, inexp_per_team = balance_teams(teams_copy, players_copy)

    # for i in balanced_list:
    #     print(f"{i}:{balanced_list[i]}")

    # print(f'experienced: {exp_per_team} // unexperienced: {inexp_per_team}')

    main()
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

    print("BASKETBALL TEAM STATS TOOL")
    print("")

    while True:
        print("---- MENU----")
        print("")
        print("Here are your choices:")
        print(" 1) Display Team Stats")
        print(" 2) Quit")
        print("")
        
        choice = input(">")
        if choice == 'Quit' or choice == '1':
            break

        elif choice == 'Display Team Stats' or choice == '2':
            for team in balanced_list:
                pass

        else:
            continue




if __name__ == "__main__":

    players_copy = PLAYERS.copy()
    teams_copy = TEAMS.copy()

    clean_data(players_copy)
    balanced_list, exp_per_team, inexp_per_team = balance_teams(teams_copy, players_copy)

    for i in balanced_list:
        print(f"{i}:{balanced_list[i]}")

    print(f'experienced: {exp_per_team} // unexperienced: {inexp_per_team}')
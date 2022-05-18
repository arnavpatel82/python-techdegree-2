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
    elif experience_level == 'NO':
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

        

# def balance_teams(team_list, player_list):
#     """balances the players across the three teams"""

#     player_list.shuffle()
#     players_per_team = len(player_list) / len(team_list)

    




if __name__ == "__main__":

    players_copy = PLAYERS.copy()
    teams_copy = TEAMS.copy()

    clean_data(players_copy)
    print(players_copy)
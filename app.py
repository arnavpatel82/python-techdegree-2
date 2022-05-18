from constants import PLAYERS


def clean_data(player_list):
    for dic in player_list:

        # cleans up player height
        dic['height'] = int(dic['height'].replace(' inches', ''))

        # cleans up player experience
        if dic['experience'] == 'YES':
            dic['experience'] = True
        elif dic['experience'] == 'NO':
            dic['experience'] = False
        



        
    

if __name__ == "__main__":
    PLAYERS_COPY = PLAYERS.copy()
    clean_data(PLAYERS_COPY)
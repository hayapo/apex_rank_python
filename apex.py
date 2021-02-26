import emoji
import requests

def set_platform(platform: str) -> str:
    Apex_platform = {\
    'Origin' : 'origin',\
    'PS' : 'ps',\
    'XBOX ' : 'xbox'\
}
    return Apex_platform[platform]

def set_rankname(rank_status: int) -> str:
    Apex_rank = {\
    'Bronze' : emoji.emojize(':3rd_place_medal:'),\
    'Silver' : emoji.emojize(':2rd_place_medal:'),\
    'Gold' : emoji.emojize(':1rd_place_medal:'),\
    'Platinum' : emoji.emojize(':trophy:'),\
    'Diamond' : emoji.emojize(':gem_stone:'),\
    'Master' :  emoji.emojize(':atom_symbol:'),\
    'Predator' : emoji.emojize(':ogre:')\
    }

    if 0 <= rank_status['value']  < 1200:
        return Apex_rank['Bronze'] #🥉
    elif 1200 <= rank_status['value'] < 2800:
        return Apex_rank['Silver'] #🥈
    elif 2800 <= rank_status['value'] < 4800:
        return Apex_rank['Gold'] #🥇
    elif 4800 <= rank_status['value'] < 7200:
        return Apex_rank['Platinum'] #🏆
    elif 7200 <= rank_status['value'] < 10000:
        return Apex_rank['Diamond']  #💎
    elif 10000 <= rank_status['value']:
        if rank_status['rank'] is not None:
            if rank_status['rank'] <= 750:
                return Apex_rank['Predator'] #👹
            else:
                return Apex_rank['Master'] #⚛️
        else:
            return Apex_rank['Master'] #⚛️
    else:
        return emoji.emojize(':zzz:')

def create_endpoint(platform: str, user_identifier: str) -> str:
    return "https://public-api.tracker.gg/v2/apex/standard/profile/{}/{}".format(platform,user_identifier)


def get_status(api_key: str, platform: str, user_identifier: str) -> dict:
    url = create_endpoint(platform,user_identifier)
    header = {"TRN-Api-Key":api_key}
    
    return requests.get(url, headers=header)
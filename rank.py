import emoji

Apex_platform = {\
    'Origin' : 'origin',\
    'PS' : 'ps',\
    'XBOX ' : 'xbox'\
}

def set_platform(platform):
    return Apex_platform[platform]

Apex_rank = {\
    'Bronze' : emoji.emojize(':3rd_place_medal:'),\
    'Silver' : emoji.emojize(':2rd_place_medal:'),\
    'Gold' : emoji.emojize(':1rd_place_medal:'),\
    'Platium' : emoji.emojize(':diamond_with_a_dot:'),\
    'Diamond' : emoji.emojize(':gem_stone:'),\
    'Master' :  emoji.emojize(':atom_symbol:'),\
    'Predator' : emoji.emojize(':ogre:')\
    }

def set_rankname(stat):
    if 0 <= stat.value  < 1200:
        return Apex_rank['Bronze']
    elif 1200 <= stat.value < 2800:
        return Apex_rank['Silver']
    elif 2800 <= stat.value < 4800:
        return Apex_rank['Gold']
    elif 4800 <= stat.value < 7200:
        return Apex_rank['Platinum']
    elif 7200 <= stat.value < 10000:
        return Apex_rank['Diamond']
    elif 10000 <= stat.value:
        rank = stat.rank
        if rank <= 750:
            return Apex_rank['Predator']
        else:
            return Apex_rank['Master']
    else:
        return Apex_rank['Master']

def create_endpoint(platfrom, user_identifier):
    return "https://public-api.tracker.gg/v2/apex/standard/profile/{}/{}".format(platfrom,user_identifier)


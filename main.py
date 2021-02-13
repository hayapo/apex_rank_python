import json, math, logging, twitter
import apex,env
from pprint import pprint


def main():
    logger = logging.getLogger('LoggingTest')
    logger.setLevel(10)
    sh = logging.StreamHandler()
    logger.addHandler(sh)       
    logger.debug('debug')
    #TRACKER NETWORKのAPIを叩いた結果をJSONの辞書で取得
    res = apex.get_status(
        env.trn_api_key,
        apex.set_platform('Origin'),
        env.apex_user_identifier
    ).json() 

    #rank_status -> rankScore以下を保持した辞書型のJSON
    rank_status = res["data"]["segments"][0]["stats"]["rankScore"]
    #rank_emoji -> ランク位置のアイコンを絵文字で取得
    rank_emoji = apex.set_rankname(rank_status)
    #rank_point -> ランクポイント
    rank_point = math.floor(res["data"]["segments"][0]["stats"]["rankScore"]["value"])

    #twitter_user_name_templateの{}の部分にrank_emojiとrank_pointを埋め込む
    name = env.twitter_user_name_template.replace('{}','{}{}'.format(rank_emoji, str(rank_point)))
    print(name)
    
    
    #Twitterのユーザー名を変更
    api = twitter.api(env.CK, env.CS, env.AT, env.AS)
    api.UpdateProfile(name=name)

if __name__ == "__main__":
    main()
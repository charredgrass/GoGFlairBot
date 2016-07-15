import re, praw

app_id = "-CW-pzNvWiIbXw"
f = open('secrets.txt','r')
app_secret = re.sub('\n', '', f.readline())
app_uri = 'http://127.0.0.1:65010/authorize_callback'
app_ua = "/u/charredgrass /r/GiftOfGames flair thing"
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = 'Uf49qGT2IjRMaie7oBECQVjNNNo'
app_refresh = re.sub('\n', '', f.readline())

def login():
    r = praw.Reddit(app_ua)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(app_refresh)
    return r

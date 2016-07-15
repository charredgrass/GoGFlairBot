import praw, re
r = praw.Reddit()

f = open('secrets.txt','r')
pword = re.sub('\n', '', f.readline())
secret = re.sub('\n', '', f.readline())
r.set_oauth_app_info(client_id='-CW-pzNvWiIbXw',
    client_secret=secret,
    redirect_uri='http://127.0.0.1:65010/authorize_callback')
url = r.get_authorize_url('uniqueKey','identityKey', True)
import url

import praw, re, obot
from pprint import pprint

r = obot.login()

submission = r.get_submission(submission_id='4sxzn5')

pprint(submission.comments)

def parseComment(c):
    #if c isn't a comment object we have bigger problems
    currflair = c.author_flair_text
    currflair_class = c.author_flair_text
    text = c.body
    #check body against regex. if fails, return.
    re_correct_post = re.compile(r"^Gifted or Grabbed: (?:Gifted|Grabbed)\n\nGame received\/gifted: [a-zA-Z ]+\n\nLink to your steam profile: http(?:s)?:\/\/steamcommunity\.com(?:\/id\/[a-zA-Z]+)\n\nLinks to \[GoG\] \+ giveaway: .*\n\nTotal Grabbed now: \d+")
    print(c.body)
    if re_correct_post.match(text):
        print("REEEE")
    else:
        print("ROOOO")

for x in submission.comments:
    parseComment(x)

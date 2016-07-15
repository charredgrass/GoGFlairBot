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

for x in submission.comments:
    parseComment(x)

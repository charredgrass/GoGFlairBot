import praw, re, obot
from pprint import pprint

r = obot.login()

submission = r.get_submission(submission_id='4sxzn5')
subreddit = r.get_subreddit('charredgrass')
me = "CharredBot"
mods_who_may_have_done_flair = [""]

def parseComment(c):
    #if c isn't a comment object we have bigger problems
    for n in c.replies:
        if (me == str(n.author)):
            print("RIP")
            return
    currflair = c.author_flair_text
    currflair_class = c.author_flair_text
    text = c.body
    #check body against regex. if fails, return.
    yoofted = re.compile("[Gg]ifted or [Gg]rabbed: ([a-zA-Z]+)")
    tgn = re.compile("Total [Gg]rabbed now: (\d+)")
    grabbedinflair = re.compile("Grabbed (\d+)?")
    pprint(yoofted.search(text).group(1))
    if (yoofted.search(text).group(1) == "Grabbed"):
        #keep going
        num = int(tgn.search(text).group(1))
        #check against flair grabbed
        c.reply("Doing your flair.")
        #check for gifted and stuff
        ft = lambda f, n: ("Gifted | " if "Gifted" in f else "") + "Grabbed" + (" " + str(n) if n > 1 else "")
        fc = lambda f: "giftedgrabbed" if "Gifted" in f else "grabbed"
        r.set_flair(subreddit, c.author, ft(currflair, num), fc(currflair))


for x in submission.comments:
    parseComment(x)

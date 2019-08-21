#For the purposes of this homework, we define three types of Twitter users.
    #Layman: Users with less than 100 followers
    #Expert: Users with 100-1000 followers
    #Celebrity: Users with more than 1000 followers

#Using the Twitter API, and starting with the @WUSTL twitter user, answer the following:

import imp
import tweepy
import time
twitter = imp.load_source('twit', '/Users/jorda/OneDrive/Documents/Secrets/start_twitter_jordan.py')
api = twitter.client
limit = api.rate_limit_status()
limit.keys()
limit["resources"].keys()
limit["resources"]["friends"]
limit["resources"]["followers"]
limit["resources"]["tweets"]
#creates a connection to WUSTL's twitter feed
wu = api.get_user('WUSTL')
wu.statuses_count
wu.followers_count
wu.friends_count
#creates a connection to WUSTLPoliSci's twitter feed
wups = api.get_user('WUSTLPoliSci')
wups.statuses_count
wups.followers_count
wups.friends_count

#One degree of separation:
#Among the followers of @WUSTL, who has the greatest number of total tweets?
#Among the followers of @WUSTL, who has the greatest number of followers?

#creates lists for followers, followers' tweets, and followers' followers
wufollowers = []
wufollowerstweets = []
wufollowersfollowers = []
#begins function to append information to lists
def followers():
    for follower in tweepy.Cursor(api.followers, 'WUSTL').items():
        try:
            wufollowers.append(follower.screen_name)
            wufollowerstweets.append(follower.statuses_count)
            wufollowersfollowers.append(follower.followers_count)
        except tweepy.TweepError:
            pass

#calls the followers function
followers()
#checks to make sure all followers were appended
len(wufollowers)
#asks for the follower who has the greatest number of tweets
wufollowers[wufollowerstweets.index(max(wufollowerstweets))]
#asks for the highest tweeting follower's number of tweets
max(wufollowerstweets)
#asks for the follower who has the greatest number of followers
wufollowers[wufollowersfollowers.index(max(wufollowersfollowers))]
#asks for the highest followed follower's number of followers
max(wufollowersfollowers)

    #Among those who @WUSTL follows, who has the greatest number of followers?
    #Among those who @WUSTL follows, who has the greatest number of tweets by group: layman, expert and celebrity?

#creates lists for the followed, the followed's tweets, and the followed's followers
wufollows = []
wufollowstweets = []
wufollowsfollowers = []
#begins function to append information to lists
def follows():
    for follow in tweepy.Cursor(api.friends, 'WUSTL').items():
        try:
            wufollows.append(follow.screen_name)
            wufollowstweets.append(follow.statuses_count)
            wufollowsfollowers.append(follow.followers_count)
        except tweepy.TweepError:
          pass

#calls the follows function
follows()
#checks to make sure all the followed were appended
len(wufollows)
#asks for the followed who has the greatest number of followers
wufollows[wufollowsfollowers.index(max(wufollowsfollowers))]
#asks for the highest followed followed's number of followers
max(wufollowsfollowers)
#creates lists for layman, expert, and celebrity
layman = []
expert = []
celebrity = []
#sorts the followed into layman if less than 100 followers, expert if less than 1000 followers, and celebrity if over 1000 followers
for i in range(0,len(wufollows)):
    if wufollowsfollowers[i] < 100:
        layman.append(i)
    if 100 <= wufollowsfollowers[i] and wufollowsfollowers[i] <= 1000:
        expert.append(i)
    if 1000 < wufollowsfollowers[i]:
        celebrity.append(i)

#creates dictionary for layman, expert, and celebrity tweets
laymantweets = {}
experttweets = {}
celebritytweets = {}
#appends to layman dictionary the name of each layman and his/her number of tweets
for j in range(0,len(layman)):
    laymantweets.update({wufollows[layman[j]]: wufollowstweets[layman[j]]})

#appends to the expert dictionary the name of each expert and his/her number of tweets
for j in range(0,len(expert)):
    experttweets.update({wufollows[expert[j]]: wufollowstweets[expert[j]]})

#appends to the celebrity dictionary the name of each celebrity and his/her number of tweets
for j in range(0,len(celebrity)):
    celebritytweets.update({wufollows[celebrity[j]]: wufollowstweets[celebrity[j]]})

#asks for the followed with the highest number of tweets per group
for k in (laymantweets, experttweets,celebritytweets):
    print([l for l, m in k.items() if m == max(k.values())])

#HAVE NOT HAD TIME TO FINISH RUNNING WITH WUSTL'S DATA...BUT TRIED FUNCTION ON TWITTER USER WITH LESS FOLLOWERS/FOLLOWED AND THE CODE ABOVE WORKED AS EXPECTED

#Two degrees of separation:
#(For the following questions, limit your searches to laymen and experts.)
    #Among the followers of @WUSTLPoliSci and their followers, who has the greatest number of tweets?
    #Among those who @WUSTLPoliSci follows and those who they follow, who has the greatest number of tweets?

#creates lists for the WUPS's followers, its followers' number of tweets, its followers' number of followers, its followers' followers, its followers' followers' number of tweets, and its followers' followers'
#number of followers
wupsfollowersids = []
wupsfollowerstweets = []
wupsfollowers_followers = []
wupsfollowers_followersids = []
wupsfollowers_followerstweets = []
wupsfollowers_followersfollowers = []
#begins function to append information to lists (restricting to those with fewer than 1000 followers)
def followers2():
    for follower2 in tweepy.Cursor(api.followers, 'WUSTLPoliSci').items():
        if follower2.followers_count < 1000:
            try:
                wupsfollowersids.append(follower2.screen_name)
                wupsfollowerstweets.append(follower2.statuses_count)
                wupsfollowers_followers.append(follower2.followers_count)
            except tweepy.TweepError:
                pass
                for follower_follower in tweepy.Cursor(api.followers, follower2.screen_name).items():
                    if follower_follower.followers_count < 1000:
                        try:
                            wupsfollowers_followersids.append(follower_follower.screen_name)
                            wupsfollowers_followerstweets.append(follower_follower.statuses_count)
                            wupsfollowers_followersfollowers.append(follower_follower.followers_count)
                        except tweepy.TweepError:
                            pass

#calls the followers2 function
followers2()
#asks for the follower who has the greatest number of tweets
wupsfollowersids[wupsfollowerstweets.index(max(wupsfollowerstweets))]
#asks for the highest tweeting follower's number of tweets
max(wupsfollowerstweets)
#asks for the followers' follower who has the greatest number of tweets
wupsfollowers_followersids[wupsfollowers_followerstweets.index(max(wupsfollowers_followerstweets))]
#asks for the highest tweeting followers' follower's number of tweets
max(wupsfollowers_followerstweets)

#creates lists for the WUPS's followed, its followed's number of tweets, its followed's number of followers, its followed's followed, its followed's followed's number of tweets, and its followed's followed's
#number of followers
wupsfollowsids = []
wupsfollowstweets = []
wupsfollows_followers = []
wupsfollows_followsids = []
wupsfollows_followstweets = []
wupsfollows_followsfollowers = []
#begins function to append information to lists (restricting to those with fewer than 1000 followers)
def follows2():
    for follow2 in tweepy.Cursor(api.friends, 'WUSTLPoliSci').items():
        if follow2.followers_count < 1000:
            try:
                wupsfollowsids.append(follow2.screen_name)
                wupsfollowstweets.append(follow2.statuses_count)
                wupsfollows_followers.append(follow2.followers_count)
            except tweepy.TweepError:
                pass
                for follow_follow in tweepy.Cursor(api.friends, follow2.screen_name).items():
                    if follow_follow.followers_count < 1000:
                        try:
                            wupsfollows_followsids.append(follow_follow.screen_name)
                            wupsfollows_followstweets.append(follow_follow.statuses_count)
                            wupsfollows_followsfollowers.append(follow_follow.followers_count)
                        except tweepy.TweepError:
                            pass

#calls the follows2 function
follows2()
#asks for the followed who has the greatest number of tweets
wupsfollowsids[wupsfollowstweets.index(max(wupsfollowstweets))]
#asks for the highest tweeting followed's number of tweets
max(wupsfollowstweets)
#asks for the followed's followed who has the greatest number of tweets
wupsfollows_followsids[wupsfollows_followstweets.index(max(wupsfollows_followstweets))]
#asks for the highest tweeting followed's followed's number of tweets
max(wupsfollows_followstweets)

#FIRST PART OF BOTH FORUMLAE WORKS, BUT SECOND PART FAILS TO EXECUTE BECAUSE IT SAYS IT IS STILL AN EMPTY LIST

#When you're scraping followers you may hit a wall at 5,000 users. This is the limit of users you can grab in a single API
#call. You should be able to get more than 5,000 by issuing multiple API calls across multiple pages. To do this you should
#follow the very last example in today's script, which used a Cursor object to iterate over multiple pages. The trick will
#be figuring out how to keep storing followers after the rate limit kicks in. I suggested that you can do this using the
#try-except #workflow we learned in class 03. Patrick suggested an alternate approach that involves specifying one of
#tweepy's options to implement a wait time between re-tries. I'll leave it to you to determine what works best for your
#use case. Again, to clarify: at one point I indicated that it would be okay to stop at the first 5,000 followers. Disregard that.
#You should collect all of the available followers (remembering that users with extreme privacy settings may not turn up
#in API calls).

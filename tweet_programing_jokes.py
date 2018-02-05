import requests
from bs4 import BeautifulSoup
from tweepy  import OAuthHandler, API
import time


r=requests.get("https://worstjokesever.com/programming?sort=date")
c = r.content

jokes = []     #creating list for storing jokes


soup = BeautifulSoup(c, "html.parser")

jocking=soup.find_all("section",{"class":"Article__content"})

#getting jokes from website
for item in jocking:
    jokes.append(item.find_all("p"))





#now code for tweeting
# Credentials to access Twitter API
ACCESS_TOKEN    = 'paste your access token here'
ACCESS_SECRET   = 'paste your access secret here'
CONSUMER_KEY    = 'paste your consumer key here'
CONSUMER_SECRET = 'paste your consumer secret here'

#authenticating twitter API
Auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
Auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
TwitterBot = API(Auth)


num=0
while (num<len(jokes)):

    try:

        if len(jokes[num]) == 1:
            TwitterBot.update_status(jokes[num][0].text)


        elif len(jokes[num]) == 2:
            TwitterBot.update_status(str(jokes[num][0].text+' \n'+jokes[num][1].text))


        elif len(jokes[num]) == 3:
            TwitterBot.update_status(str(jokes[num][0].text + ' \n' + jokes[num][1].text+ jokes[num][2].text))

    except:
        print("Error occured while tweeting")

    #increment num
    num+=1

    #give duration between tweets
    time.sleep(60)



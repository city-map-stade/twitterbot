from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

x = input("(I)nstagram or (T)witter? ")
if x in ['i', 'I', 'instagram', 'Instagram']:
    class InstagramBot:
        def __init__(self, username, password):
            self.username = username 
            self.password = password
            self.bot = webdriver.Firefox()

        def login(self):
            bot = self.bot
            bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
            time.sleep(3)
            email =  bot.find_element_by_name('username')
            password = bot.find_element_by_name('password')
            email.clear()
            password.clear()
            email.send_keys(self.username)
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
            time.sleep(2)

        def getFollower(self):
            bot = self.bot

    insta = InstagramBot('test','test')
    insta.login()    

elif x in ['t', 'T', 'twitter', 'Twitter']:
    class TwitterBot:
        def __init__(self, username, password):
            self.username = username 
            self.password = password
            self.bot = webdriver.Firefox()

        def login(self):
            bot = self.bot
            bot.get('https://twitter.com')
            time.sleep(3)
            email = bot.find_element_by_class_name('email-input')
            password = bot.find_element_by_name('session[password]')
            email.clear()
            password.clear()
            email.send_keys(self.username)
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
            time.sleep(2)


        def like_tweet(self, hashtag):
            bot = self.bot
            bot.get('https://twitter.com/search?q='+ hashtag +'&src=tyah')
            time.sleep(2)
            for i in range(1,5):
                bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(2)
                tweets = bot.find_elements_by_class_name('tweet')
                links = [elem.get_attribute('data-permalink-path') for elem in tweets]
                for link in links:
                    bot.get('https://twitter.com/' + link)
                    try:
                        bot.find_element_by_class_name('HeartAnimation').click()
                        time.sleep(2)
                    except Exception as ex:
                        time.sleep(10)
    x = input("Welchen Hashtag: ")            
    tw = TwitterBot('m.seir@city-map.de', 'twiMw95iSg.')
    tw.login()
    tw.like_tweet(x)
else:   
    print("Ungültig")
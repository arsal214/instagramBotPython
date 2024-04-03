from instabot import Bot
bot=Bot()
bot.login(username="", password="")
bot.follow('username') # follow the other account
bot.upload_photo('path',caption='Picture Caption')  # For single image upload

bot.unfollow('username')   # unfollow the specific account


bot.send_message('Hi, Message From InstaBot',['senderUsername1','senderUsername2']) # for sending message to muliple user

followers=bot.get_user_follower('username')   #get info of user follower

for follower in followers:
    print(bot.get_user_info(follower))



followings=bot.get_user_following('username')   #get info of user following

for following in followings:
    print(bot.get_user_info(following))    
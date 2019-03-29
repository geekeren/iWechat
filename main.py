import os
from wxpy import *

env_dist = os.environ
bot = Bot(cache_path=True, console_qr=2)
tuling = Tuling(api_key=env_dist.get('Tuling_API_KEY'))

@bot.register(Friend, TEXT)
def reply_my_friend(msg):
    tuling.do_reply(msg)
    print(msg)


@bot.register(Group, TEXT)
def reply_my_group(msg):
    if msg.is_at:
        tuling.do_reply(msg)
    print(msg)

@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    new_friend = msg.card.accept()

embed()

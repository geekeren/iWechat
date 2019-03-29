import os
from wxpy import *

env_dist = os.environ
bot = Bot(cache_path=True, console_qr=1)
tuling = Tuling(api_key=env_dist.get('Tuling_API_KEY'))

# 使用图灵机器人自动与指定好友聊天

@bot.register(Friend, TEXT)
def reply_my_friend(msg):
    tuling.do_reply(msg)
    print(msg)


@bot.register(Group, TEXT)
def reply_my_group(msg):
    if msg.is_at:
        tuling.do_reply(msg)
    print(msg)

embed()

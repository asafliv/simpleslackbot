import threading
from flask import Flask
from rtmbot import RtmBot
from users import UsersDict

__author__ = 'asafliv'

def start_bot():
    config = {
        "SLACK_TOKEN": "xoxb-331718210816-SgOVGToKscF1VQANhxvak8DS",
        "ACTIVE_PLUGINS": ["plugins.printall.MyPlugin"]
    }
    bot = RtmBot(config)
    print "starting bot"
    bot.start()

app = Flask('slackserver')
user_data = UsersDict()

#running the bot in a thread.
bot_thread = threading.Thread(target=start_bot)
bot_thread.daemon = True
bot_thread.start()

@app.route('/process_msg/<msg_string>')
def process_bot_msg(msg_string):
    # identify user
    # is new user
    # is only digit then add to it's sum
    return "new bot msg recieved!!"


@app.route('/average')
def get_total_avg():
    return user_data.get_all_users_avg_string()


@app.route('/asaf')
def test():
    return "asaf"


@app.route('/average/<string:user_name>')
def get_specific_avg(user_name):
    return user_data.get_specific_user_avg(user_name)


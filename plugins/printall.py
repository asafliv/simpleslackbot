from __future__ import print_function
from rtmbot.core import Plugin
import requests


class MyPlugin(Plugin):
    def catch_all(self, data):
        print(data)
        # response = requests.get('localhost:5000/process_msg', data=data)
        # print(response.text)

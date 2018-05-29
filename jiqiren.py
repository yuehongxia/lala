import requests
import itchat
# import re
# from itchat.content import *

# KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
KEY = '04f44290d4cf462aae8ac563ea7aac16'
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    print(msg)
    print(msg['Text'])
    reply = get_response(msg['Text'])
    return reply or defaultReply


# @itchat.msg_register([PICTURE,RECORDING,VIDEO,SHARING])
# def other_reply(msg):
#     itchat.send(('那我就祝你狗年大吉大利，新的一年事事顺心'),msg['FromUserName'])
itchat.auto_login(hotReload=True)
itchat.run()

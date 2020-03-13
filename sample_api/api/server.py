from flask import Flask, request
import json
import ast

app = Flask(__name__)

FB_API_URL = 'https://graph.facebook.com/v6.0/me/messages'
VERIFY_TOKEN = 'any_password'
PAGE_ACCESS_TOKEN = 'daa86080cd49f275113af7198fe4fe0a'



def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"


@app.route("/webhook", methods = ['GET', 'POST'])
def listen():
    if request.method == 'GET':
        return verify_webhook(request)

    if request.method == 'POST':
        output = request.get_json()
 #       entry_val = output['entry']
 #       entry_list = entry_val[0]
 #       changes_val = entry_list['changes']
  #      changes_list = changes_val[0]
   #     value_val = changes_list['value']
        print(output)
        return 'im here'
        



if __name__=="__main__":
    app.run()
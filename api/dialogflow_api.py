import json

import apiai

import message_generator
import security


def call_small_talk(message):
    try:
        request = apiai.ApiAI(security.DIALOG_FLOW_TOKEN).text_request()
        request.lang = 'en'
        request.session_id = 'BayaBot'
        request.query = message
        response = json.loads(request.getresponse().read().decode('utf-8'))
        return response['result']['fulfillment']['speech'] + " " + message_generator.Emoji.smile
    except Exception as e:
        raise Exception('Can not get information' + str(e))

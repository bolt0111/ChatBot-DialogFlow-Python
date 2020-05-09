import json

import apiai

import security


def call_small_talk(message):
    try:
        request = apiai.ApiAI(security.DIALOG_FLOW_TOKEN).text_request()
        request.lang = 'en'
        request.session_id = 'BayaBot'
        request.query = message
        response = json.loads(request.getresponse().read().decode('utf-8'))
        return response['result']['fulfillment']['speech']
    except Exception:
        raise Exception('Can not get information')

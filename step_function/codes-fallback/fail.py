import requests


def fail(event, context):

    alerta = "La step fallo en su ejecución"
    telegram_bot_sendtext(alerta)


def telegram_bot_sendtext(bot_message):
    bot_token = "1314762060:AAFvTjHCuMOSGH4cFnU9CzXc6sN0cG3jhlM"
    bot_chatID = '-457266763'
    send_text = ('https://api.telegram.org/bot' + bot_token +
                 '/sendMessage?chat_id=' + bot_chatID +
                 '&parse_mode=Markdown&text=' + bot_message)
    response = requests.get(send_text)
    return response.json()

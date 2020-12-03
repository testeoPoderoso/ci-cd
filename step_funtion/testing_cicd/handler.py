from send_message_module import telegram_bot_sendtext


def handler1(event, context):
    """
    Esta es la lambda que mandara los mensajes

    """
    message = "uno .."
    print(message)
    telegram_bot_sendtext(message)


def handler2(event, context):
    """
    Esta es la lambda que mandara los mensajes

    """
    message = "dos ..."
    print(message)
    telegram_bot_sendtext(message)


def handler3(event, context):
    """
    Esta es la lambda que mandara los mensajes

    """
    message = "https://www.youtube.com/watch?v=xiqpouJsFM4&ab_channel=ElMega"
    telegram_bot_sendtext(message)

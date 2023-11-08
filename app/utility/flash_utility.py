from flask import flash

def flash_message(message, messageType):
    return flash(message, messageType)
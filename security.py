import configparser

config = configparser.ConfigParser()
config.read('bot.ini')

TOKEN = config['Telegram']['token']
PROXY = config['Telegram']['proxy']

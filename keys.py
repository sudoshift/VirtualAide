import telebot, openai, time

openai.api_key = 'YOUR TOKEN OPENAI' #Use a key do seu openai api
admin = [] # O id da sua conta no telegram
token = 'YOUR TOKEN TELEGRAM' # O ID do seu bot
bot = telebot.TeleBot(token)
comp = ', responda apenas em português brasileiro, e não me envie links ou script. Estamos no ano de 2023.' #Para evitar bugs de envio de script do nada, altere dependendo da sua necessidade, é com está variavel que você irá controlar a personalidade do bot


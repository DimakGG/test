import telebot

tg = telebot.TeleBot(token='8002746811:AAFLy8g5DZBItg_Xt_qAuRvZSAMiJyyn9ws')

@tg.message_handler(commands='start')
def ans(message):
    tg.reply_to(message, "hello")

tg.infinity_polling()
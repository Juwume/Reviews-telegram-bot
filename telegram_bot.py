import telebot
from telebot import types

from telebot import apihelper


token = '5415375546:AAHBuj3TcEuU89J0YouYZYVgCQHI7ODvtCQ'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Product info', 'Words Cloud', 'Topics')
    keyboard.row('ALERTS subscribtion', 'User subscribtions')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)
'''
@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=5))
    bot.send_message(message.chat.id, text="Какая средняя оценка была у Вас в школе?", reply_markup=markup)
'''
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'product info':
        bot.send_message(message.chat.id, 'Hi! This bot can help you to analyse reviews about products.')
    elif message.text.lower() == 'user subscribtions':
        bot.send_message(message.chat.id, 'You are subscribed to:')
    elif message.text.lower() == 'words cloud':
        platform_choosing(message)
    

@bot.message_handler(content_types = ['text'])
def platform_choosing(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Wildberries', callback_data='wildberries'))
    markup.add(telebot.types.InlineKeyboardButton(text='Yandex Market', callback_data='yandex market'))
    bot.send_message(message.chat.id, text="Please choose platform", reply_markup=markup)
    #bot.register_next_step_handler(message,segment_choosing)
    segment_choosing(message)

def segment_choosing(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Cats', callback_data='cats'))
    markup.add(telebot.types.InlineKeyboardButton(text='Dogs', callback_data='dogs'))
    bot.send_message(message.chat.id, text="Please choose segment", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    #bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    answer = ''
    if call.data == 'wildberries':
        answer = 'Super!'
    elif call.data == 'yandex market':
        answer = 'Super!'
    elif call.data == 'cats':
        answer = 'Super!'
    elif call.data == 'dogs':
        answer = 'Super!'

    bot.send_message(call.message.chat.id, 'You chose '+ call.data)
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.polling()
#bot.polling(none_stop=True, interval=0)
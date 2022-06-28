from telebot import types, telebot
import telebot
import os
from main import main


bot = telebot.TeleBot(os.getenv('TOKEN'), parse_mode=None)

urls = {
    'apple': 'https://www.ebay.com/b/Apple/bn_21819543',
    'samsung': 'https://www.ebay.com/b/Samsung/bn_21834655',
    'sony': 'https://www.ebay.com/b/Sony/bn_21835731'
}


@bot.message_handler(['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Apple')
    itembtn2 = types.KeyboardButton('Samsung')
    itembtn3 = types.KeyboardButton('Sony')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, 'Choose category:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def catch_all(message):
    if message.text not in ('Apple', 'Samsung', 'Sony'):
        bot.send_message(message.chat.id, 'Choose one of the categories')

    bot.send_message(message.chat.id, 'Scraping...')

    file = ''
    if message.text == 'Apple':
        file = main(urls['apple'])
    elif message.text == 'Samsung':
        file = main(urls['samsung'])
    elif message.text == 'Sony':
        file = main(urls['sony'])

    if file:
        bot.send_document(message.chat.id, open(file, 'rb'))
        os.remove(file)


bot.infinity_polling()

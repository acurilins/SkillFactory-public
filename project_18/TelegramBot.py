import telebot
from config import TOKEN, keys
from extensions import ConversionException, CryptoConverter
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    print(message.text)
    if message.from_user.username != None:
        bot.reply_to(message.chat.id, f'Welcome, {message.chat.username},'
                                      f'\nplease type "/help" to see the instructions')
    else:
        bot.send_message(message.chat.id, f'Welcome, '
                                          f'please type "/help" to see the instructions')


@bot.message_handler(commands=['help'])
def help_menu(message: telebot.types.Message):
    text = 'To get the current price, please type the conversion command as follows:\n\n<Currency name> \
<currency to convert in> <amount>. \n\nType "/values" to see available currencies.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def currency_list(message):
    text = 'Available currencies:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', '\
                                    location', 'contact', 'sticker'])
def handle_other_types(message: telebot.types.Message):
    bot.reply_to(message, 'Unfortunately, media files are not supported, \
please type "/help" to see the instructions')


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConversionException('Too less or too many parameters.')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConversionException as e:
        bot.reply_to(message, f'The following error caused by user.\n{e}')
    except Exception as e:
        bot.reply_to(message, f"Couldn't complete the request\n{e}")
    else:
        text = f'{amount} {quote} in {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

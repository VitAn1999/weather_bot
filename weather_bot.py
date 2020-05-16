import pyowm
import telebot

owm = pyowm.OWM('797b9317f2d48c064ea264fb0ab5d070', language='ru')
bot = telebot.TeleBot('1231682294:AAFk6KRgBXiq0O-VyrihTLYg4AS-3-ckw7c')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "В каком городе ты живешь?")


@bot.message_handler(content_types = 'text')
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp']
    max_temp = w.get_temperature('celsius')['temp_max']
        
    answer = 'В ' + message.text + ' сейчас ' + w.get_detailed_status()+'\n'
    answer += 'Температура сейчас  ' + str(temp) + ' градусов Цельсия.' + ' Днем ожидается до ' + str(max_temp) + ' градусов'+'\n\n'
    if temp<5:
        answer += 'На улице жуть как холодно, хозяин собаку не выпустил бы на улицу, но к сожалению тебе на работу, поэтому я бы посоветовал одеться потеплее'
    elif temp<12:
        answer += 'Снаружи не май месяц, одевай шапку и куртку'
    elif temp<20:
        answer += 'На улице достаточно свежо, накинь ветровку или кардиган'
    elif temp<27:
        answer += 'На улице кайфово, иди грей кости'
    else:
        answer += 'Такая жарень, сейчас бы холодного пивка, а не это все, да?'
    bot.send_message(message.chat.id, answer)
        
bot.polling(none_stop = True)

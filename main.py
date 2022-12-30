from telebot.async_telebot import AsyncTeleBot, types
import asyncio
import random
from congrat_lists import list_1, list_2, list_3


TOKEN = ''
bot = AsyncTeleBot(TOKEN)


def get_random_congrat(cong_list_1, cong_list_2, cong_list_3):
    rand_cong_1 = random.choice(cong_list_1)
    rand_cong_2 = random.choice(cong_list_2)
    rand_cong_3 = random.choice(cong_list_3)
    full_random_congrat = f"С Новым годом, {rand_cong_1} \nЯ желаю {rand_cong_2} \nИ пусть {rand_cong_3}"
    return full_random_congrat


@bot.message_handler(commands=['start'])
async def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Сгенерировать поздравление!')
    markup.add(btn1)
    msg = '<b>ГЕНЕРАТОР ПОЗДРАВЛЕНИЙ НА 2023!</b>' \
          '\n\nЖМИ НА КНОПКУ внизу экрана!' \
          '\n\nпонравился бот?' \
          '\nавтору на пивко - по № тел :)'
    await bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=markup)


@bot.message_handler()
async def get_user_text(message):
    if message.text.lower() == "сгенерировать поздравление!":
        msg = get_random_congrat(list_1, list_2, list_3)
        await bot.send_message(message.chat.id, msg)


async def run():
    await bot.polling(none_stop=True)

asyncio.run(run())



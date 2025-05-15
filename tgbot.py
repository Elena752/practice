import requests, json, random, telebot, string, time, threading
from datetime import datetime, timedelta

#@practicettit_bot

token = '7889538323:AAGaJsCDZ99wmKzgh1o8cLNDqJSnkL1amc8'
bot = telebot.TeleBot(token)
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row('Случайный мем', 'Сгенерировать пароль', 'Угадай столицу', 'Напомни', 'Гороскоп')

countries = {"Россия": "Москва", "Франция": "Париж", "Германия": "Берлин", "Италия": "Рим", "Испания": "Мадрид", "Португалия": "Лиссабон", "Великобритания": "Лондон",
    "Япония": "Токио", "Китай": "Пекин", "Индия": "Нью-Дели", "США": "Вашингтон", "Канада": "Оттава", "Бразилия": "Бразилиа", "Аргентина": "Буэнос-Айрес",
    "Египет": "Каир", "ЮАР": "Претория", "Австралия": "Канберра", "Турция": "Анкара", "Украина": "Киев", "Беларусь": "Минск", "Польша": "Варшава", "Нидерланды": "Амстердам", "Бельгия": "Брюссель",
    "Швейцария": "Берн", "Швеция": "Стокгольм", "Норвегия": "Осло", "Финляндия": "Хельсинки", "Дания": "Копенгаген", "Греция": "Афины", "Чехия": "Прага"}
user_games = {}
reminders = {}
user_reminders = {}
horoscopes = ["Вам сегодня стоит проявить инициативу.", "Сегодня ваш день, действуйте смело!", "Рекомендуется сосредоточиться на финансах.", "Сегодня хороший день для планирования.", "Вам нужно быть внимательными - вас ждёт успех.", "Сегодня день неожиданных возможностей."]

def get_random_meme():
    headers = {'User-Agent': 'MemeBot/0.1'}
    response = requests.get('https://www.reddit.com/r/dankmemes/hot.json?limit=100', headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        posts = [post['data'] for post in data['data']['children']
                 if not post['data']['over_18'] and post['data']['url'].endswith(('jpg', 'jpeg', 'png'))]
        if posts:
            return random.choice(posts)['url']

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + '!@#$%^&*()_+-=[]{}|;:,.<>?'
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        if (any(c.isdigit() for c in password) and  any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password)):
            return password

def start_capital_game(chat_id):
    country = random.choice(list(countries.keys()))
    user_games[chat_id] = {'country': country, 'attempts': 3}
    return f"Назовите столицу страны: {country}"


def check_capital_answer(chat_id, user_answer):
    if chat_id not in user_games:
        return None
    game = user_games[chat_id]
    answer = countries[game['country']]
    user_answer = user_answer.strip().lower()
    if user_answer == answer.lower():
        del user_games[chat_id]
        return True, f"Верно! Столица {game['country']} - {answer}"
    else:
        game['attempts'] -= 1
        if game['attempts'] <= 0:
            del user_games[chat_id]
            return False, f"Игра окончена. Правильный ответ: {answer}"
        return False, f"Неверно! Осталось попыток: {game['attempts']}"

def parse_time_input(text):
    try:
        parts = text.split()
        hours = 0
        minutes = 0
        for i, part in enumerate(parts):
            if part.isdigit():
                num = int(part)
                if i + 1 < len(parts):
                    next_part = parts[i + 1].lower()
                    if 'час' in next_part:
                        hours = num
                    elif 'минут' in next_part:
                        minutes = num
        return timedelta(hours=hours, minutes=minutes)
    except:
        return None
def schedule_reminder(chat_id, reminder_text, delay):
    def send_reminder():
        time.sleep(delay.total_seconds())
        bot.send_message(chat_id, f"Напоминание: {reminder_text}")
    thread = threading.Thread(target=send_reminder)
    thread.start()
    reminders[chat_id] = {
        'thread': thread,
        'time': datetime.now() + delay,
        'text': reminder_text
    }

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет!",
        reply_markup=keyboard)
@bot.message_handler(func=lambda message: message.text == 'Случайный мем')
def send_meme(message):
    meme_url = get_random_meme()
    bot.send_photo(message.chat.id, meme_url)

@bot.message_handler(func=lambda message: message.text == 'Сгенерировать пароль')
def send_password(message):
    password = generate_password()
    bot.send_message(
        message.chat.id,
        password)

@bot.message_handler(func=lambda message: message.text == 'Угадай столицу')
def start_game(message):
    question = start_capital_game(message.chat.id)
    bot.send_message(message.chat.id, question)

@bot.message_handler(func=lambda message: message.chat.id in user_games)
def check_game_answer(message):
    chat_id = message.chat.id
    result, reply = check_capital_answer(chat_id, message.text)
    bot.send_message(chat_id, reply)
    if not result and chat_id in user_games:
        country = user_games[chat_id]['country']
        answer = countries[country]
        hint = f"Подсказка: столица начинается на '{answer[0]}'"
        bot.send_message(chat_id, hint)

@bot.message_handler(func=lambda message: message.text == 'Напомни')
def start_reminder(message):
    msg = bot.send_message(
        message.chat.id,
        "Через какое время напомнить?\n"
        "Пример: '2 часа 30 минут' или '45 минут'"
    )
    user_reminders[message.chat.id] = {}
    bot.register_next_step_handler(msg, process_reminder_time)

def process_reminder_time(message):
    chat_id = message.chat.id
    time_delta = parse_time_input(message.text)
    if not time_delta or time_delta.total_seconds() <= 0:
        bot.send_message(chat_id, "Неверный формат времени. Попробуйте снова.")
        return
    user_reminders[chat_id]['time_delta'] = time_delta
    msg = bot.send_message(chat_id, "Что напомнить?")
    bot.register_next_step_handler(msg, process_reminder_text)

def process_reminder_text(message):
    chat_id = message.chat.id
    reminder_text = message.text.strip()
    if chat_id not in user_reminders or 'time_delta' not in user_reminders[chat_id]:
        bot.send_message(chat_id, "Ошибка: время не указано.")
        return
    time_delta = user_reminders[chat_id]['time_delta']
    schedule_reminder(chat_id, reminder_text, time_delta)
    reminder_time = datetime.now() + time_delta
    bot.send_message(
        chat_id,
        f"Напоминание установлено на {reminder_time.strftime('%H:%M')}:\n"
        f"{reminder_text}"
    )
    del user_reminders[chat_id]

@bot.message_handler(func=lambda message: message.text.lower() == 'гороскоп')
def ask_zodiac_sign(message):
    msg = bot.send_message(
        message.chat.id,
        "Для какого знака зодиака вы хотите гороскоп?\n"
        "Введите один из знаков: овен, телец, близнецы, рак, лев, дева, весы, скорпион, стрелец, козерог, водолей, рыбы"
    )
    bot.register_next_step_handler(msg, send_horoscope)

def send_horoscope(message):
    sign = message.text.strip().lower()
    if sign not in {'овен', 'телец', 'близнецы', 'рак', 'лев', 'дева', 'весы', 'скорпион', 'стрелец', 'козерог', 'водолей', 'рыбы'}:
        bot.send_message(message.chat.id, "Неизвестный знак зодиака. Попробуйте снова.")
        return
    bot.send_message(
        message.chat.id,
        f"Гороскоп для {sign.capitalize()} на сегодня:\n\n{random.choice(horoscopes)}\n\n"
        f"Характеристика дня: {random.choice(['благоприятный', 'нейтральный', 'сложный'])}"
    )

bot.polling(none_stop=True)
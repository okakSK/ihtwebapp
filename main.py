from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
import telebot

bot = telebot.TeleBot("7870584540:AAG8isfT89Vi3RXVKFuZcH_gXk6Wm6pl5Go")

# -------------------------------
# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    gallery_btn = KeyboardButton("🖼 Открыть галерею",
                                 web_app=WebAppInfo("https://komronbek-urinboev.github.io/ihtwebapp/"))
    markup.add(gallery_btn)

    inline = InlineKeyboardMarkup()
    inline.add(
        InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        InlineKeyboardButton("📚 About", callback_data="about"),
    )
    inline.add(
        InlineKeyboardButton("👨‍💻 Dev", callback_data="dev"),
        InlineKeyboardButton("🛠 Admin", callback_data="admin"),
    )

    bot.send_message(message.chat.id, "Добро пожаловать в IHT Gallery!", reply_markup=markup)
    bot.send_message(message.chat.id, "Выберите команду:", reply_markup=inline)


# -------------------------------
# Inline кнопки (callback)
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "help":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id,
                         "ℹ️ Помощь:\n\n/browse — открыть галерею\n/help — справка\n/about — о проекте\n/admin — контакты администрации\n/dev — разработчики")
    elif call.data == "about":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📚 Этот бот показывает галерею учеников IHT с 1994 по 2025 год.")
    elif call.data == "dev":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "👨‍💻 Разработчики:\n- Samir Khamzin\n- Urinboev Komron")
    elif call.data == "admin":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🛠 Authors: Samir Khamzin, Urinboev Komron")


# -------------------------------
# Команды через /
@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.send_message(message.chat.id,
                     "ℹ️ Помощь:\n\n/browse — открыть галерею\n/help — справка\n/about — о проекте\n/admin — контакты администрации\n/dev — разработчики")


@bot.message_handler(commands=['about'])
def about_cmd(message):
    bot.send_message(message.chat.id, "📚 Этот бот показывает галерею учеников IHT с 1994 по 2025 год.")


@bot.message_handler(commands=['dev'])
def dev_cmd(message):
    bot.send_message(message.chat.id, "👨‍💻 Разработчики:\n- Samir Khamzin\n- Urinboev Komron")


@bot.message_handler(commands=['admin'])
def admin_cmd(message):
    bot.send_message(message.chat.id, "🛠 Authors: Samir Khamzin, Urinboev Komron")


# -------------------------------
# Бот запускается
bot.polling()

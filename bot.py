import telebot
from config import token
from logic import analyze_text

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Напиши фразу на русском или английском, а я определю её тональность.")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Отправь текст на русском или английском языке, например: Мне очень нравится этот фильм!")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        label, confidence = analyze_text(message.text)
        label_translation = {
            "POSITIVE": "положительная",
            "NEGATIVE": "отрицательная",
            "NEUTRAL": "нейтральная",
        }.get(label, label)
        bot.send_message(
            message.chat.id,
            f"Тональность: {label_translation}\nУверенность: {confidence:.0%}",
        )
    except Exception:
        bot.send_message(message.chat.id, "Не удалось проанализировать текст. Попробуйте написать другую фразу.")

bot.polling()

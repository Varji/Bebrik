import openai
import telebot

openai.api_key = "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"
bot = telebot.TeleBot('6032536935:AAGUhTTg-udaq6Hd9v1ZLHNAxZDK6N1-y-4')

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    return response

@bot.message_handler(commands=['start'])
def start(message):
    greeting = "Привет! Меня зовут Бебрик и я разработан для помощи людям! Скорее задавай мне свой вопрос,я знаю ответы на всё!"
    bot.send_message(chat_id=message.chat.id, text=greeting)

@bot.message_handler(content_types=['text'])
def handle_message(message):
    prompt = message.text
    response = generate_response(prompt)
    bot.send_message(chat_id=message.chat.id, text=response)

bot.polling(none_stop=True)

import telebot
import random
bot = telebot.TeleBot("659885740:AAHzZCQHsJmlEkIf7tU2ofxlQ1W-1qaj6Qw")
def last(msg,num):
    return msg[len(msg)-num:]
def first(msg,num):
    return msg[:len(msg) - num]
def answer(num,text):
    bot.send_message(num,text)
    print(text)
@bot.message_handler(content_types= ["text"])
def handle_command(message):
    text = message.text
    id = message.chat.id

    print(message.chat.id)
    print("написал мне ")
    print(message.text)
    print("И я ответил ему...")

    if(text[:7] == "отправь"):
        answer(214583870,text[8:len(text)])
    elif(last(text, 1) == "а"):
        answer(id,"Да уже ж вроде женский... ну ладно.." + first(text,1) + "ичка.. или " + first(text,1) + "ша")
    elif(last(text,2) == "ст"):
        answer(id, text + "ка")
    elif(last(text,2) == "ик"):
        answer(id, first(text,2) + "ица")
    else:
        answer(id, text + "есса")

    print("---------------")
bot.polling(none_stop=True, interval=0)
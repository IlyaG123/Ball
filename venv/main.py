import telebot
from telebot import types
import random
token="6040671471:AAHAfgoU8lKx7kO6JQRIEsBhkjFpfr1pzes"
bot=telebot.TeleBot(token)
hp=dmg=0
ras={"elf":{"hp":50,"dmg":70},
     "gnom":{"hp":75,"dmg":40},
     "hobbit":{"hp":100,"dmg":125},
     "org":{"hp":110,"dmg":170}}
prof={"warrior":{"hp":60,"dmg":80},
      "medical":{"hp":100,"dmg":35},
      "mag":{"hp":90,"dmg":130},
      "archer":{"hp":45,"dmg":60}}
monsters=["ghost","vampire","dracula","joker","trol"]
def create_monsters():
    rndname=random.choice(monsters)
    rndhp=random.randint(50,90)
    rnddmg=random.randint(45,110)
    return[rndname,rndhp,rnddmg]
def race_menu():
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    for race in ras.keys():
        keyboard.add(types.KeyboardButton(text=race))
    return keyboard
def proff_menu():
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    for proff in prof.keys():
        keyboard.add(types.KeyboardButton(text=proff))
    return keyboard
def quest():
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn4=types.KeyboardButton("go")
    btn5=types.KeyboardButton("back")
    keyboard.add(btn4,btn5)
    return keyboard
@bot.message_handler(commands=["start"])
def start(message):
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton("play")
    btn2=types.KeyboardButton("info")
    keyboard.add(btn1,btn2)
    bot.send_message(message.chat.id,"Do you wanna play?",reply_markup=keyboard)
@bot.message_handler(content_types=["text"])
def main(message):
    global hp,dmg
    victim=create_monsters()
    if message.text=="play":
        bot.send_message(message.chat.id,"Выберете расу",reply_markup=race_menu())
    if message.text=="elf":
        hp+=ras["elf"]["hp"]
        dmg+=ras["elf"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали эльфа, у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=proff_menu())
        image=open("5cd8c777035969f08488dd2aac1d8ebe--elves-fantasy-fantasy-rpg.jpg", "rb")
        bot.send_photo(message.chat.id, image)
    if message.text=="gnom":
        hp+=ras["gnom"]["hp"]
        dmg+=ras["gnom"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали гнома у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=proff_menu())
        image=open("1663292575_10-phonoteka-org-p-gnom-art-krasivo-10.png", "rb")
        bot.send_photo(message.chat.id, image)
    if message.text=="hobbit":
        hp+=ras["hobbit"]["hp"]
        dmg+=ras["hobbit"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали хоббита у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=proff_menu())
        image=open("1645247048_1-adonius-club-p-khobbit-art-1.png", "rb")
        bot.send_photo(message.chat.id, image)
    if message.text=="org":
        hp+=ras["org"]["hp"]
        dmg+=ras["org"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали орга у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=proff_menu())
        image=open("ab950a3e504b83c244eac37bfdefed36.png", "rb")
        bot.send_photo(message.chat.id, image)
    if message.text=="warrior":
        hp+=prof["warrior"]["hp"]
        dmg+=prof["warrior"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали воина у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=quest())
        image=open("voin-80-foto-8.jpg", "rb")
        bot.send_photo(message.chat.id, image)
    if message.text=="medical":
        hp+=prof["medical"]["hp"]
        dmg+=prof["medical"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали лечащий у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=quest())
        image=open("tony-foti-heal-scaled.png", "rb")
        bot.send_photo(message.chat.id, image)
    if message.text=="mag":
        hp+=prof["mag"]["hp"]
        dmg+=prof["mag"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали мага у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=quest())
        image=open("2dfbd347f0ac5fa946a11adc2acaac88.png", "rb")
        bot.send_photo(message.chat.id, image)
    if message.text=="archer":
        hp+=prof["archer"]["hp"]
        dmg+=prof["archer"]["dmg"]
        bot.send_message(message.chat.id,f"Вы выбрали лучника у вас столько здоровья {hp}, у вас столько урона {dmg}",reply_markup=quest())
        image=open("devushka-ryzhaia-fantasticheskii-art-art-luchnitsa-grud-zele.png", "rb")
        bot.send_photo(message.chat.id, image)
    if message.text=="back":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("play")
        btn2=types.KeyboardButton("info")
        keyboard.add(btn1,btn2)
        bot.send_message(message.chat.id,"Do you wanna play?",reply_markup=keyboard)
    if message.text=="go":
        event=random.randint(1,4)
        if event==1 or event==2 or event==3:
            keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn4=types.KeyboardButton("go")
            btn5=types.KeyboardButton("back")
            keyboard.add(btn4,btn5)
            bot.send_message(message.chat.id,"Вам никто не встретился. Хотите ли вы продолжить?",reply_markup=keyboard)
        elif event==4:
            keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn5=types.KeyboardButton("back")
            btn6=types.KeyboardButton("attack")
            btn7=types.KeyboardButton("run")
            keyboard.add(btn5,btn6,btn7)
            bot.send_message(message.chat.id,f"Вам встретился монстр! Его зовут {victim[0]} Его здоровье {victim[1]} Его урон {victim[2]}",reply_markup=keyboard)
    if message.text=="attack":
        victim[1]-=dmg
        if victim[1]<=0:
            hp+=20
            dmg+=35
            bot.send_message(message.chat.id,f"Вы победили врага! Ваше здоровье {hp} Ваш урон {dmg}",reply_markup=quest())
        elif victim[1]>0:
            hp-=victim[2]
            bot.send_message(message.chat.id,"Вас атакуют!")
            if hp<=0:
                keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn5=types.KeyboardButton("back")
                keyboard.add(btn5)
                bot.send_message(message.chat.id,"Вас победили",reply_markup=keyboard)
            elif hp>0:
                keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn5=types.KeyboardButton("back")
                btn6=types.KeyboardButton("attack")
                btn7=types.KeyboardButton("run")
                keyboard.add(btn5,btn6,btn7)
                bot.send_message(message.chat.id,f"Вам встретился монстр! Его зовут {victim[0]} Его здоровье {victim[1]} Его урон {victim[2]} Ваше здоровье{hp} Ваш урон{dmg}",reply_markup=keyboard)                
    if message.text=="run":
        plan=random.randint(1,4)
        if plan==1 or plan==2 or plan==3:
            hp-=victim[2]
            bot.send_message(message.chat.id,f"Вам не удалось сбежать. Вас атакуют!")
            if hp<=0:
                keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn5=types.KeyboardButton("back")
                keyboard.add(btn5)
                bot.send_message(message.chat.id,"Вас победили",reply_markup=keyboard)
            elif hp>0:
                keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn5=types.KeyboardButton("back")
                btn6=types.KeyboardButton("attack")
                btn7=types.KeyboardButton("run")
                keyboard.add(btn5,btn6,btn7)
                bot.send_message(message.chat.id,f"Вам встретился монстр! Его зовут {victim[0]} Его здоровье {victim[1]} Его урон {victim[2]} Ваше здоровье{hp} Ваш урон{dmg}",reply_markup=keyboard)
        if plan==4:
            keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn4=types.KeyboardButton("go")
            btn5 = types.KeyboardButton("back")
            keyboard.add(btn4,btn5)
            bot.send_message(message.chat.id,f"Вам удалось сбежать.",reply_markup=keyboard)
    if message.text=="info":
        bot.send_message(message.chat.id,f" Этот бот текстовая RPG игра. Выберите своего персонажа и деритесь с врагами.")
bot.polling(non_stop=True)
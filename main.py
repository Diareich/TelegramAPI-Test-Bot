import telebot

token = '6085361037:AAEG268pi7LDoEZ9kaZ_o07_NMQ0TiUY5qs'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id, "Привет ✌️ ")


@bot.message_handler(content_types=['text'])
def new_message(message):
  if message.text.lower() == "hello":
    bot.send_message(message.chat.id, "Hello, Phillip!")
  elif message.text.lower() == "send cat":
    bot.send_photo(
      message.chat.id,
      photo=
      "https://images.pexels.com/photos/8478515/pexels-photo-8478515.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    )
  elif message.text.lower() == "send dog":
    bot.send_photo(
      message.chat.id,
      photo=
      "https://images.pexels.com/photos/14720746/pexels-photo-14720746.jpeg?auto=compress&cs=tinysrgb&w=1600"
    )
  elif message.text.lower() == "send meme":
    bot.send_photo(
      message.chat.id,
      photo=
      "https://images.pexels.com/photos/10575129/pexels-photo-10575129.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    )
  elif message.text == "/gif":
    bot.send_animation(
      message.chat.id,
      "https://media.giphy.com/media/xT8qBsOjMOcdeGJIU8/giphy.gif")
  elif message.text == "/sticker_love":
    bot.send_sticker(
      message.chat.id,
      "CAACAgIAAxkBAAEHpzFj5OF5ldH2Io2TVmInMujrm_xN4AAC8hAAAowt_QetcAKw4n6WFy4E"
    )
  elif message.text == "/sticker_tired":
    bot.send_sticker(
      message.chat.id,
      "CAACAgIAAxkBAAEHpzNj5OGbFMPOPrOqF0bEHWbQSESZ6wAC_hAAAowt_QcENP-UWc9s_i4E"
    )
  elif message.text == "/sticker_offended":
    bot.send_sticker(
      message.chat.id,
      "CAACAgIAAxkBAAEHpzVj5OHABDSkJgIq7kRac587CoMmyAAC9RAAAowt_QeMK-R5ws9Zyi4E"
    )
  elif message.text == "/sticker_teases":
    bot.send_sticker(
      message.chat.id,
      "CAACAgIAAxkBAAEHpzdj5OHYDHdw9dnTGrVjgcTVf5jsTQAC-BAAAowt_QeyqAYcDETDrS4E"
    )
  elif message.text == "/sticker_nerd":
    bot.send_sticker(
      message.chat.id,
      "CAACAgIAAxkBAAEHp0Jj5OKHHZDylvXwovEAAbC-WhF-GHQAAv8QAAKMLf0HdRH3l21zNSsuBA"
    )
  elif message.text.lower() == "привет":
    bot.send_message(message.chat.id, "И тебе привет!")
  elif message.text.lower() == "Как дела?".lower():
    bot.send_message(message.chat.id, "Хорошо, а как у вас?")
  elif message.text.lower() == "Где ты живешь?".lower():
    bot.send_message(message.chat.id, "В Минас Тирите, а вы откуда?")
  else:
    bot.send_message(message.chat.id, "Извините, я вас не понимаю")


bot.polling(none_stop=True)

#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import telebot
import random
token = input("Введите токен: ")



print("Бот начал работу: ")



bot = telebot.TeleBot(token)

name = ["Марина", "Августа", "Жанна", "Оксана", "Злата", "Полина", "Кира", "Алиса", "Алла", "Альбина", "Анастасия", "Анфиса", "Виола", "Влада", "Зарина", "Катерина", "Кристина", "Ксения", "Лариса", "Каролина", "София", "Мария", "Надежда", "Надя", "Юлия", "Кристина", "Вика", "Наталия", "Марина", "Анна", "Наталья", "Елена", "Евгения", "Диана", "Регина", "Ева", "Жасмин", "Зарина", "Инесса", "Мэри", "Олеся", "Ульяна", "Хана", "Хельга", "Яна", "Эля", "Маринет", "Азалия", "Виктория", "Элла"]
photo = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.jpg", "11.jpg", "12.jpg", "13.jpg", "14.jpg", "15.jpg", "16.jpg", "17.jpg", "18.jpg", "19.jpg", "20.jpg", "21.jpg", "22.jpg", "23.jpg", "24.jpg", "25.jpg", "26.jpg", "27.jpg", "28.jpg", "29.jpg", "30.jpg", "31.jpg", "32.jpg", "33.jpg", "34.jpg", "35.jpg", "36.jpg", "37.jpg", "38.jpg", "39.jpg", "40.jpg", "41.jpg", "42.jpg", "43.jpg", "44.jpg", "45.jpg", "46.jpg", "47.jpg", "48.jpg", "49.jpg", "50.jpg", ]
desc = [
	"Хрупкая и ласковая девочка💃, жаждет ласки и страсти! Давай встретимся и сгорим в огне безумства 🔥! Приезжай ко мне или зови меня в гости! Я приеду быстро!",
	"Дорого, красиво, развратно! Для порядочных и достойных! Стройная и ухоженная, всегда загорелая и вкуснопахнущая! Всегда в хорошем настроении.Самый нежный и долгий минет сочными губками и горячим ротиком;-)💋",
	"Очаровательная девушка с прекрасной искренней улыбкой подарит настоящее наслаждение, формы Дианы не смогут оставить равнодушным настоящего мужчину.", "Со мной Вы сможете осуществить самое сокровенное, и, самое экстремальное свое желание и воплотить любую Вашу эксклюзивную фантазию!!!",
	"Мега женственна и сексапильна👯! Утончённая фигурка, сладкая и вкусная киска🍒) Я приглашаю тебя в гости для незабываемых оргазмов и громких криков))💋",
	"Прекрасная Транссексуальная девушка с восточной внешностью , готова подарить массу удовольствия , может быть послушной шлюшкой , либо напористой активной , ты не сможешь забыть этой встречи надолго",
	"Я милая, сексуальная, похотливая кошечка, Обожаю секс и отдаюсь с наслаждением🍒!", "Милая, нежная и очень ласковая кошечка, с роскошным телом и покладистым нравом... люблю доставлять удовольствие...!!!.",
	"Молодая, стройная, сочная и очень страстная девчонка, создана для любви и ласки. Обожаю секс и люблю им заниматься!!! Жду тебя!!!)))))))",
	"Сексапильная, ухожена, приятная и легкая в общении! Фотографии мои ! Встречаюсь всегда с желанием и замечательным настроением )!Допы обсуждаю💋",
	"Страстная и нежная, темпераментная кошечка приедет к вам в гости! Встреча со мной доставит вам огромное удовольствие! Люблю секс и умею им заниматься.",
	"Прекрасная Транссексуальная девушка с метиской внешностью , готова подарить массу удовольствия , может быть послушной шлюшкой , либо напористой активной , ты не сможешь забыть этой встречи надолго .",
	"Ну очень горячая малышка!) И ты обязательно в этом убедишься после нашей встречи.) Молодая, подтянутая, горячая кошечка с удовольствием скрасит твой досуг.)💋💋💋",
	"Нежная, молодая красавица, яркая и сексуальная, страстная кошечка, доставит вам незабываемое удовольствие и массу наслаждений!!!!",
	"Яркая и сладкая шалунья, воплощу в реальность твои самые откровенные желания и фантазии…",
	"Пускай ты требовательный и капризный мужчина. Для меня нет нечего неразрешимого. Любой каприз я выполню без всяких проблем. С удовольствием расслаблю и подарю тебе сладкие мгновения нашей встречи.💋",
	"Я доставлю Вам массу наслаждения🍓 и остроту новых ощущений. Ваши чувства обостряться до предела, а тело расслабится💆‍♂️... Обилие ласк, подводящих Вас к полному пробуждению эротического потенциала всего Вашего организма...💋",
	"Я игривая кошечка , приглашаю на приятный и страстный релакс в моем исполнении , я очень манящая , отведав раз , захочешь еще и еще 💋)",
	"Моя горячая кровь выжмет из тебя все соки сладкий Я круче любых гор , красивее и возбудительнее И усею перевоплощаться в любой образ) Если ты готов к незабываемому вечеру Я жду тебя )",
	"Сексуальность, грация, роскошная фигурка💃-если выберешь меня, никогда не пожалеешь... свидание со мной, будет прокручиваться у тебя в голове😱снова и снова...💋",
	"Мои губки и подтянутое тело порадуют глаза, а способности в постели удивят даже самого прихотливого и требовательного. Неутомимая и темпераментная я сделаю твой вечер незабываемым. Атмосферу, удовольствие и релакс я гарантирую.",
	"Устрою максимально яркий, эмоциональный, стрaстный и незабываемый релакс!!! Позволь своим фантазиям сбыться...рядом со мной. Я почти идеальная талия 60 , бедра 90",
	"💋Я Яркая, страстная и ненасытная блондинка.💋",
	"молодая, но опытная. возьми меня за волосы и натолкай в ротик - это было бы хорошим началом дня ;)",
	"Мои внутренности сжимаются от горячего, жадного, растекающегося по всему телу желания💋. Почувствуй меня. Посмотри как твоему телу нравится то, что я делаю🍒. Со мной ты точно сможешь получить то что ты жаждешь 🍌",
	"Очень люблю секс и реально получаю удовольствие от встреч 💦 Ухоженная, стройная, юная)",
	"Ласка, нежность, приятные запахи и прикосновения, море удовольствия 💋 от прелюдии и эстетики - вот что я гарантирую 💯 своему партнеру при встрече♥️."]
@bot.message_handler(commands=['website'])
def open_website(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Начать знакомство", url="https://leylarelax.com"))
	bot.send_message(message.chat.id,
			"Сотни девушек ждут вашего сообщения, напишите им!",
			parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['insta'])
def instagram(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти в Инстаграм", url="https://www.instagram.com/leylarelax_com/"))
	bot.send_message(message.chat.id, "Нажмите на кнопку ниже и погрузитесь в мир разврата и похоти прямо сейчас", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['https://vk.com/sexkiev0'])
def vk(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Посетить группу Вк", url="https://vk.com/prog_life"))
	bot.send_message(message.chat.id, "Нажмите на кнопку ниже и погрузитесь в мир разврата и похоти прямо сейчас", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton('Киев')
	btn2 = types.KeyboardButton('Львов')
	btn3 = types.KeyboardButton('Одесса')
	btn4 = types.KeyboardButton('Харьков')
	markup.add(btn1, btn2, btn3, btn4)
	send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nСотни девушек ждут тебя, выбери свой город?"
	img = open("32.jpg", 'rb')
	bot.send_photo(message.chat.id, img)
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "вернуться":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Киев')
		btn2 = types.KeyboardButton('Львов')
		btn3 = types.KeyboardButton('Одесса')
		btn4 = types.KeyboardButton('Харьков')

		markup.add(btn1, btn2, btn3, btn4)
		final_message = "Куда же вы, девушки ждут вашего сообщения!"
		img = open("43.jpg", 'rb')
		bot.send_photo(message.chat.id, img)

	#ГОРОДА
	elif get_message_bot == "киев":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Случайная модель')
		btn2 = types.KeyboardButton('Все модели')
		btn3 = types.KeyboardButton("Вернуться")
		markup.add(btn1, btn2, btn3)

		final_message = "Отлично, эта девушка ищет себе мужчину, напишем ей?\n          <b>Имя:</b> " + random.choice(name) + "\n          <b>Обо мне:</b> " + random.choice(desc) + "\n          <b>Связь со мной:</b> " + "<a href=\"https://leylarelax.com\">Анкета</a>"
		img = open(random.choice(photo), 'rb')
		bot.send_photo(message.chat.id, img)
	#ГОРОДА
	elif get_message_bot == "львов":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Случайная модель')
		btn2 = types.KeyboardButton('Все модели')
		btn3 = types.KeyboardButton("Вернуться")
		markup.add(btn1, btn2, btn3)

		final_message = "Отлично, эта девушка ищет себе мужчину, напишем ей?\n          <b>Имя:</b> " + random.choice(name) + "\n          <b>Обо мне:\n</b> " + random.choice(desc) + "\n          <b>Связь со мной:</b> " + "<a href=\"https://leylarelax.com\">Анкета</a>"
		img = open(random.choice(photo), 'rb')
		bot.send_photo(message.chat.id, img)
	#ГОРОДА
	elif get_message_bot == "одесса":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Случайная модель')
		btn2 = types.KeyboardButton('Все модели')
		btn3 = types.KeyboardButton("Вернуться")
		markup.add(btn1, btn2, btn3)

		final_message = "Отлично, эта девушка ищет себе мужчину, напишем ей?\n          <b>Имя:</b> " + random.choice(name) + "\n          <b>Обо мне:</b> " + random.choice(desc) + "\n          <b>Связь со мной:</b> " + "<a href=\"https://leylarelax.com\">Анкета</a>"
		img = open(random.choice(photo), 'rb')
		bot.send_photo(message.chat.id, img)
	#ГОРОДА
	elif get_message_bot == "харьков":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Случайная модель')
		btn2 = types.KeyboardButton('Все модели')
		btn3 = types.KeyboardButton("Вернуться")
		markup.add(btn1, btn2, btn3)

		final_message = "Отлично, эта девушка ищет себе мужчину, напишем ей?\n          <b>Имя:</b> " + random.choice(name) + "\n          <b>Обо мне:</b> " + random.choice(desc) + "\n          <b>Связь со мной:</b> " + "<a href=\"https://leylarelax.com\">Анкета</a>"
		img = open(random.choice(photo), 'rb')
		bot.send_photo(message.chat.id, img)
	elif get_message_bot == "случайная модель":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Случайная модель')
		btn2 = types.KeyboardButton('Все модели')
		btn3 = types.KeyboardButton("Вернуться")
		markup.add(btn1, btn2, btn3)
		final_message = "Отлично, эта девушка ищет себе мужчину, напишем ей?\n          <b>Имя:</b> " + random.choice(name) + "\n          <b>Обо мне:</b> " + random.choice(desc) + "\n          <b>Связь со мной:</b> " + "<a href=\"https://leylarelax.com\">Анкета</a>"
		img = open(random.choice(photo), 'rb')
		bot.send_photo(message.chat.id, img)
	elif get_message_bot == "все модели":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Посмотреть всех моделей", url="https://leylarelax.com/all-model/"))
		final_message = "Посмотреть всех моделей можно на нашем сайте!"
	# Здесь различные дополнительные проверки и условия
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Киев')
		btn2 = types.KeyboardButton('Львов')
		btn3 = types.KeyboardButton('Одесса')
		btn4 = types.KeyboardButton('Харьков')
		markup.add(btn1, btn2, btn3, btn4)
		final_message = "Так, так, так\nПостой, лучше нажми на одну из интерактивных кнопок ниже"
	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)

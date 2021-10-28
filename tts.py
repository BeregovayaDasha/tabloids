#pip install pyttsx3

import pyttsx3

name = {" Даша": 19, " Ваня": 17, " Вика": 18, " Илья": 20," Бабушка": 65, " Степа": 11}
anim = {" Даша": "собака", " Ваня": "Ёж", " Вика": "Кот", " Илья": "Енот"," Бабушка": "Хомяк", " Степа": "сам как животное"}
#name = [1,2,3,4,5];
while True:
    text = input("Введите имя")

    engine = pyttsx3.init()
    engine.say(name[text])
    engine.runAndWait()

    text1 = input("Введите имя")

    engine = pyttsx3.init()
    engine.say(anim[text1])
    engine.runAndWait()

    print("Возраст:", name[text], "лет")
    print("Дома живет:", anim[text1])

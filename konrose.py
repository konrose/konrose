import os, random, time
os.system("clear")
print("Здравствуй, добро пожаловать в игрушку!))")
name = input("Введи своё имя, рядовой : ")
time.sleep(1)

# Звания
ranks = ["Рядовой", "Ефрейтор", "Мл. Сержант", "Сержант", "Ст. Сержант", "Старшина", "Прапорщик", "Ст. Прапорщик", "Мл. Лейтенант", "Лейтенант", "Ст. Лейтенант"]
ranks_num = 0

level = 0
exp = 0
max_exp = 50

settings = None

risk = None
mission = 0

shans = 0

uprank = 0
uprank_risk = 0
uprank_max = 5

if name == "admin" :
    ranks_num = 10
    level = 100
    exp = 100000

start = True
while start == True :
    os.system("clear")

    max_rank = uprank_max - uprank
    if ranks_num == 10 :
        max_rank = "||| Максимальное звание |||"

    if uprank >= uprank_max :
        uprank_max = uprank_max + 5
        ranks_num = ranks_num + 1
    if exp >= max_exp :
        max_exp = exp + (int(max_exp * 20 / 100))
        level = level + 1
    if exp < 0 :
        exp = exp - exp

    print("=========================")

    print("Имя : " + name)
    print("Ранг : " + ranks[ranks_num] + " [" + str(ranks_num) + "] До повышения : " + str(max_rank))
    print("Уровень : " + str(level) + "  [" + str(exp) + "/" + str(max_exp) + " exp.]")

    print("=========================")

    risk = int(random.uniform(-1,101))

    shans = int(random.uniform(-1, 101))

    print("[1] - отправится на задание. Шанс : " + str(risk) + "%. При успешном прохождении ты получишь : " + str(int((100 - risk) / 2 )) + " exp.")
    print("[2] - пропустить задание. -" + str(int((100 - risk) / 2) - 5) + " exp.")
    print(" ")
    settings = int(input("Выберите действие : "))

    if settings == 1 :
        os.system("clear")
        print("Выполняется...")
        time.sleep(2)

        if shans <= risk :
            os.system("clear")
            print("Задание выполнено! + " + str(int((100 - risk) / 2)) + " exp.")
            exp = exp + (int((100 - risk)/2))
            uprank = uprank + 1
            time.sleep(2)
        if shans > risk :
            os.system("clear")
            print("Задание провалено...")
            print("Вы потеряли " + str(int(((100 - risk) / 2) - 5)) + " exp.")
            if exp > 0 :
                exp = exp - (int(((100 - risk) / 2) - 5))
            uprank_risk = uprank_risk + 1
            if uprank_risk == 2 :
                uprank = uprank - 1
                uprank_risk = 0
            time.sleep(2)

    if settings == 2 :
        os.system("clear")
        print("Вы пропустили задание и потеряли " + str(int((100 - risk) / 2) - 5) + " exp.")
        exp = exp - (int((100 - risk) / 2) - 5)
        uprank = uprank - 1
        if uprank_risk == 2 :
            uprank = uprank - 1
            uprank_risk = 0

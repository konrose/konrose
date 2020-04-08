import os, random, time
try: # Если файл data.py есть, то срабатывает этот блок кода
    import data
    name = data.name
    level = data.level
    ranks_num = data.ranks_num
    exp = data.exp
    money = data.money
    max_exp = data.max_exp
    uprank = data.uprank
    uprank_risk = data.uprank_risk
    uprank_max = data.uprank_max
    playing = data.playing
    p_max = data.p_max
except: # Иначе этот
    os.system("clear")
    print("Здравствуй, добро пожаловать в игрушку!))")

    name = input("Введи своё имя, рядовой : ")

    name_f_t = True
    name_num = []
    i = 0

    for i in range(10) :
        name_num.append(i)
        i = i + 1

    while name_f_t == True :
        if name[0] in str(name_num) or len(name) < 4:
            name = input("Имя не корректно! Введите снова :")
        if name[0] not in str(name_num) and len(name) > 4 :
            name_f_t = False


    time.sleep(1)

    ranks_num = 0

    level = 0
    exp = 0
    max_exp = 50

    uprank = 0
    uprank_risk = 0
    uprank_max = 5

    playing = 0
    p_max = 10
    
    money = 100

def save_data():
    f = open('data.py', 'w') # Создание/перезапись файла
    f.write('name = "' + name + '"\n')
    f.write('level = ' + str(level) + '\n')
    f.write('ranks_num = ' + str(ranks_num) + '\n')
    f.write('exp = ' + str(exp) + '\n')
    f.write('money = ' + str(money) + '\n')
    f.write('max_exp = ' + str(max_exp) + '\n')
    f.write('uprank = ' + str(uprank) + '\n')
    f.write('uprank_risk = ' + str(uprank_risk) + '\n')
    f.write('uprank_max = ' + str(uprank_max) + '\n')
    f.write('playing = ' + str(playing) + '\n')
    f.write('p_max = ' + str(p_max) + '\n')
    f.close()

# Звания
ranks = ["Рядовой", "Ефрейтор", "Мл. Сержант", "Сержант", "Ст. Сержант", "Старшина", "Прапорщик", "Ст. Прапорщик", "Мл. Лейтенант", "Лейтенант", "Ст. Лейтенант", "Капитан", "Майор", "Подполковник", "Полковник", "Генерал майор", "Генерал лейтенант", "Генерал полковник", "Генерал армии", "Маршал России"]

money_list = []

settings = None

risk = None
mission = 0

shans = 0

stamina = 10

#if name == "admin" :
    #ranks_num = 10
    #level = 100
    #exp = 100000

start = True
while start == True :
    os.system("clear")

    max_rank = uprank_max - uprank
    if max_rank > 9 :
        uprank_max = 5
        if ranks_num > 0 :
            ranks_num = ranks_num - 1

    if ranks_num == 19 :
        max_rank = "||| Максимальное звание |||"

    if uprank >= uprank_max and playing >= p_max :
        uprank_max = uprank_max + 5
        p_max = p_max + 10
        ranks_num = ranks_num + 1
        print("Вас повысили! Теперь Вы : " + str(ranks[ranks_num]) + "!")
        time.sleep(0.3)
        if ranks_num not in money_list :
            money_list.append(ranks_num)
            print("Вы получаете 200$ за новое звание!")
            money = money + 200
            time.sleep(2)
            os.system("clear")

    if exp >= max_exp :
        max_exp = max_exp + (int(max_exp * 40 / 100))
        level = level + 1
    if exp < 0 :
        exp = exp - exp
    if stamina == 0 :
        os.system("clear")
        print("Вы отдохнули, но пропустили задание.")
        time.sleep(1)
        settings = 3
        stamina = 10

    print("*=========================*")

    print("Имя : " + name)
    print("Ранг : " + ranks[ranks_num] + " [" + str(ranks_num) + "]")
    print("Уровень : " + str(level) + "  [" + str(exp) + "/" + str(max_exp) + " exp.]")
    print("Стамина [" + str("*" * stamina) + "] " + str(stamina * 10) + "%")
    print("Деньги : " + str(money) + "$")

    print("*=========================*")

    risk = int(random.uniform(2, 101))

    shans = int(random.uniform(2, 101))

    skip = int((100 - risk) / 4 )

    print(" ")
    print("[1] - отправится на задание. Шанс : " + str(risk) + "%. При успешном прохождении ты получишь : " + str(int((100 - risk) / 2 )) + " exp.")
    print("[2] - отправится на задание с шансом +15% за " + str(skip) + "$")
    print("[3] - пропустить задание. -" + str(int((100 - risk) / 2) + 5) + " exp.")
    print("[4] - сохранить и выйти.")
    print(" ")

    try: # Обход ошибок при не корректном вводе
        settings = int(input("Выберите действие : "))

    except KeyboardInterrupt: # При нажатии Ctrl+C завершается цикл и сохраняются данные
        save_data()
        os.system("clear")
        break

    except: # При любой другой ошибке запускается следующая итерация, код ниже НЕ ВЫПОЛНЯЕТСЯ
        print('Видимо ты делаешь что-то не то в своей жизни :c')
        exp -= 10
        if exp < 0:
            exp = 0

    if settings == 2 :
        if money >= skip :
            money = money - skip
            risk = risk + 15
            settings = 1
        if money < skip :
            os.system("clear")
            print("Не достаточно средств!")
            time.sleep(1)
            settings = 1

    if settings == 1 :
        os.system("clear")
        print("Выполняется...")
        playing = playing + 1
        stamina = stamina - 2
        time.sleep(2)

        if shans <= risk :
            os.system("clear")
            print("Задание выполнено! + " + str(int((100 - risk) / 2)) + " exp.")
            exp = exp + (int((100 - risk)/2))
            uprank = uprank + 1
            time.sleep(2)
        if shans > risk :
            os.system("clear")
            print("Задание провалено... Шанс был : " + str(risk) + "%")
            print("Вы потеряли " + str(int(((100 - risk) / 2) - 5)) + " exp.")
            if exp > 0 :
                exp = exp - (int(((100 - risk) / 2) - 5))
            uprank_risk = uprank_risk + 1
            if uprank_risk == 2 :
                uprank = uprank - 1
                uprank_risk = 0
            time.sleep(2)

    elif settings == 3 :
        os.system("clear")
        print("Вы пропустили задание и потеряли " + str(int((100 - risk) / 2) + 5) + " exp.")
        playing = playing - 1
        exp = exp - (int((100 - risk) / 2) + 5)
        uprank = uprank - 1
        if uprank_risk == 2 :
            uprank = uprank - 1
            uprank_risk = 0
    
    elif settings == 4:
        save_data()
        os.system("clear")
        break
    else:
        print('Видимо ты делаешь что-то не то в своей жизни :c')
        exp -= 10
        if exp < 0:
            exp = 0
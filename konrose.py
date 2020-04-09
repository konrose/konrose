import os, random, time

from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def encrypt(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }

def decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])


    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted

def save_data():
    f = open('data.txt', 'w') # Создание/перезапись файла
    f.write(str(encrypt(name, password)) + '\n')
    f.write(str(encrypt(str(level), password)) + '\n')
    f.write(str(encrypt(str(ranks_num), password)) + '\n')
    f.write(str(encrypt(str(exp), password)) + '\n')
    f.write(str(encrypt(str(money), password)) + '\n')
    f.write(str(encrypt(str(max_exp), password)) + '\n')
    f.write(str(encrypt(str(uprank), password)) + '\n')
    f.write(str(encrypt(str(uprank_risk), password)) + '\n')
    f.write(str(encrypt(str(uprank_max), password)) + '\n')
    f.write(str(encrypt(str(playing), password)) + '\n')
    f.write(str(encrypt(str(p_max), password)) + '\n')
    f.close()

password = 'C9G#@|S9WSus1A6hyygko*y$0K8SuAhEieBZE#FvQehx@qYJm#6Oi}9InC1vXaSo'

try: # Если файл data.txt есть, то срабатывает этот блок кода
    f = open('data.txt', 'r')
    lines = []
    for line in f:
        line = line.split('\n')[0]
        line = list(line)
        line.pop(0)
        line.pop(-1)
        line = ''.join(line)
        args = line.split(', ')
        _args = []
        for arg in args:
            arg = arg.split(': ')[1]
            _args.append(arg)
        lines.append({'cipher_text': _args[0], 'salt': _args[1], 'nonce': _args[2], 'tag': _args[3]})
    f.close()
    _vars = []
    for i, el in enumerate(lines):
        _vars.append(bytes.decode(decrypt(el, password)))

    name = _vars[0]
    level = int(_vars[1])
    ranks_num = int(_vars[2])
    exp = int(_vars[3])
    money = int(_vars[4])
    max_exp = int(_vars[5])
    uprank = int(_vars[6])
    uprank_risk = int(_vars[7])
    uprank_max = int(_vars[8])
    playing = int(_vars[9])
    p_max = int(_vars[10])
    os.system("clear")
    print("WELCOME TO")
    time.sleep(0.2)
    print(" ____             _        _   _ ____  ")
    time.sleep(0.2)
    print("|  _ \ __ _ _ __ | | _____| | | |  _ \ ")
    time.sleep(0.2)
    print("| |_) / _` | '_ \| |/ / __| | | | |_) |")
    time.sleep(0.2)
    print("|  _ < (_| | | | |   <\__ \ |_| |  __/ ")
    time.sleep(0.2)
    print("|_| \_\__,_|_| |_|_|\_\___/\___/|_|   ")
    time.sleep(0.2)
    print("")
    print("Добро пожаловать, " + name + "!")
    time.sleep(2)
except: # Иначе этот
    os.system("clear")
    print("WELCOME TO")
    time.sleep(0.2)
    print(" ____             _        _   _ ____  ")
    time.sleep(0.2)
    print("|  _ \ __ _ _ __ | | _____| | | |  _ \ ")
    time.sleep(0.2)
    print("| |_) / _` | '_ \| |/ / __| | | | |_) |")
    time.sleep(0.2)
    print("|  _ < (_| | | | |   <\__ \ |_| |  __/ ")
    time.sleep(0.2)
    print("|_| \_\__,_|_| |_|_|\_\___/\___/|_|   ")
    time.sleep(0.2)
    print("")

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
        if name[0] not in str(name_num) and len(name) >= 4 :
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

shop = ["+20 exp", "+60% энергии", "Сменить имя", "VIP статус на [30] ходов", "Выйти"]
shop_num = 0
shop_inp = None
shop_money = [20, 30, 200, 500]

start = True
while start == True :
    os.system("clear")

    max_rank_str = " "

    if ranks_num == 19 :
        max_rank_str = "||| Максимальное звание |||"

    max_rank = uprank_max - uprank
    if max_rank > 9 :
        uprank_max = 5
        if ranks_num > 0 :
            ranks_num = ranks_num - 1

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
        exp = 0
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
    print("Ранг : " + ranks[ranks_num] + " [" + str(ranks_num) + "] " + str(max_rank_str))
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
    print("[3] - пропустить задание. -" + str(int((100 - risk) / 4) + 5) + " exp.")
    print("[4] - Магазин (NEW)")
    print("[5] - сохранить и выйти.")
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
        time.sleep(1)

    if settings == 2 :
        if money >= skip :
            money = money - skip
            risk = risk + 15
            if risk > 100 :
                risk = 100
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
            exp = exp + (int((100 - risk) / 2 ))
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
        exp = exp - (int((100 - risk) / 4) + 5)
        uprank = uprank - 1
        if uprank_risk == 2 :
            uprank = uprank - 1
            uprank_risk = 0

    elif settings == 4 :
        os.system("clear")
        stamina -= 2

        print("[1] - [" + shop[0] + "] Стоимость : " + str(shop_money[0]) + "$")
        print("[2] - [" + shop[1] + "] Стоимость : " + str(shop_money[1]) + "$")
        print("[3] - [" + shop[2] + "] Стоимость : " + str(shop_money[2]) + "$")
        print("[4] - [" + shop[3] + "] Стоимость : " + str(shop_money[3]) + "$ (СКОРО)")
        print(" ")
        print("Ваш баланс : " + str(money) + "$")
        print(" ")
        print("[5] - [" + shop[4] + "]")
        print(" ")
        shop_inp = int(input("Выберите действие : "))

        if shop_inp == 1 :
            if money >= shop_money[0] :
                money -= shop_money[0]
                exp += 20
                print("Успешно приобретено +20 exp!")
                time.sleep(1)
            elif money < shop_money[0] :
                print("Не достаточно средств!")
                time.sleep(1)
        elif shop_inp == 2 :
            if money >= shop_money[1] :
                money -= shop_money[1]
                stamina += 6
                print("Успешно приобретено +60% энергии!")
                time.sleep(1)
            elif money < shop_money[1] :
                print("Не достаточно средств!")
                time.sleep(1)
        elif shop_inp == 3 :
            if money >= shop_money[2] :
                money -= shop_money[2]
                name = input("Введите новое имя : ")
                print("Успешно приобретено новое имя! [" + name + "]")
                time.sleep(1)
            elif money < shop_money[1] :
                print("Не достаточно средств!")
                time.sleep(1)

    elif settings == 5:
        save_data()
        os.system("clear")
        break
    else:
        print('Видимо ты делаешь что-то не то в своей жизни :c')
        exp -= 10
        if exp < 0:
            exp = 0
        time.sleep(1)

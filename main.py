from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import sys
from from_sqlite import get_dz, add_to_bd, desc
from datetime import datetime
from random import randint
import pendulum
import from_sqlite
import tks


vk = vk_api.VkApi(
    token=token.tok)

vk._auth_token()

vk.get_api()

longpoll = VkBotLongPoll(vk, 202239778)

loh = 0

loh_mode = True


def send(id, text):
    vk.method('messages.send', {
        'chat_id': id, 'message': text, 'random_id': 0})


def send_sticker(id, sticker):
    vk.method('messages.send', {
        'chat_id': id, 'sticker_id': sticker, 'random_id': 0})


for event in longpoll.listen():
    d_t = datetime.now()
    msg = event.object.text.lower()
    try:
        print(event, f'msg = {msg}', sep='\n')
        sys.stdout.flush()
    except:
        pass

    if event.type == VkBotEventType.MESSAGE_NEW and event.object.text:
        try:

            id = event.chat_id
            if event.object.from_id == 183143105 and loh == 12 and loh_mode:
                send(id, 'слава лох')
                loh = 0
            elif event.object.from_id == 183143105 and loh != 12 and loh_mode:
                loh += 1
            if msg == 'привет':
                send(id, 'дарова')
            elif msg == 'кто лучший бот?':
                send(id, 'я, мазафака')
            elif msg == 'Весьма сомнительно':
                send(id, 'хмммм....')

            elif msg == 'б-уроки':
                vk.method('messages.send', {
                    'chat_id': id, 'message': '.', 'random_id': 0, 'attachment': 'photo308565232_457246201'})
            elif msg == 'включить режим лох':
                loh_mode = True
                send(id, 'режим кибербулинга Славы включен')
            elif msg == 'выключить режим лох':
                loh_mode = False
                send(id, 'режим кибербулинга Славы выключен. Слава, живи')
            elif msg == 'завтра есть кр?':
                if randint(1, 2) == 1:
                    send(id, 'да, иди учи')
                else:
                    send(id, 'нет. пожезло, повезло')
            elif 'лох' in msg or msg == 'лох':
                send(id, from_sqlite.loh[randint(0, len(from_sqlite.loh) - 1)])
            elif '((' in msg:
                send(id, from_sqlite.sad)
            elif 'лучше не рассказывать' in msg or 'весьма сомнительно' in msg or 'сконцентрируйся и спроси опять' in msg:
                send(id, from_sqlite.dontk[randint(
                    0, len(from_sqlite.dontk) - 1)])
            elif msg == 'перспективы не очень хорошие':
                send(id, 'бывалo и хуже))')
            elif msg == '/kb' or msg == '/game' or '/%' in msg:
                send(id, from_sqlite.cmda[randint(
                    0, len(from_sqlite.cmda) - 1)])

            elif msg == 'бот':
                send(id, 'что?')
            elif msg == 'бт инфо':
                send(id, desc)
            elif msg.split()[0] == 'бт' and msg.split()[1] == 'ддз':
                try:
                    add_to_bd(" ".join(msg.split()[3::]), msg.split()[2])
                    send(id, 'Добавлено &#128077;')
                except:
                    send(id, 'Ошибка, что-то пошло не так')
                    send_sticker(id, 9131)

            elif msg.split()[0] == 'бт' and msg.split()[1] == 'дз' and msg.split()[2] == 'на':
                if msg.split()[3] == 'сегодня':
                    if d_t.month < 10:
                        date = float(str(d_t.day) + '.0' + str(d_t.month))
                    else:
                        date = float(str(d_t.day) + '.' + str(d_t.month))
                elif msg.split()[3] == 'завтра':
                    date = float(pendulum.tomorrow(
                        'Europe/Moscow').format('DD.MM'))
                else:
                    date = msg.split()[3]
                print(date)
                m = get_dz(date)
                print(m)
                if not m:
                    send(id, 'Ничего не задано !')
                    send_sticker(id, 6069)
                else:
                    s = ''
                    for i in range(len(m)):
                        s += str(m[i][0]) + '\n'
                    send(id, s)
            elif msg.split()[0].lower() == 'герцевич' or msg.split()[0].lower() == 'герцыч' or msg.lower() == 'герц' or msg.split()[0].lower() == 'герц' or msg.split()[0].lower() == 'Герц' or 'герц' in msg or 'Герц' in msg:
                send(id, from_sqlite.gerz[randint(
                    0, len(from_sqlite.gerz) - 1)])
            elif msg.split()[0] == 'бт' and msg.split()[1] == 'гдз' and msg.split()[2] == 'по' and msg.split()[3] == 'русскому':
                print('gdz')
                x = 'https://megaresheba.ru/gdz/russkij-yazyk/10-klass/grekov/' + \
                    str(msg.split()[4]) + '-nomer'
                send(id, x)
            elif msg.split()[0] == 'бт' and msg.split()[1] == 'гдз' and msg.split()[2] == 'по' and msg.split()[3] == 'алгебре':
                print('gdz')
                x = 'https://megaresheba.ru/publ/reshebnik/algebra/10_11_klass_alimov/34-1-0-1964/' + \
                    str(msg.split()[4]) + '-nomer'
                send(id, x)
            elif msg.split()[0] == 'бт' and msg.split()[1] == 'гдз' and msg.split()[2] == 'по' and msg.split()[3] == 'геометрии':
                print('gdz')
                x = 'https://gdz.ru/class-10/geometria/atanasyan-10-11/10-class-' + \
                    str(msg.split()[4]) + '/'
                send(id, x)
            elif msg == 'обновления':
                send(id, from_sqlite.updates)
            elif 'валентина вениаминовна' in msg or 'веньк' in msg:
                send(id, from_sqlite.val[randint(
                    0, len(from_sqlite.val) - 1)] + '\n https://m.vk.com/video358497250_456239683')
            elif 'что задано' in msg:
                send(id, get_dz(float(pendulum.tomorrow(
                    'Europe/Moscow').format('DD.MM'))))
            elif 'с какого урока' in msg:
                send(id, from_sqlite.lessons[randint(
                    0, len(from_sqlite.lessons) - 1)])
            elif 'хах' in msg or 'аха' in msg or 'ахха' in msg:
                send_sticker(id, from_sqlite.st_ah[randint(
                    0, len(from_sqlite.st_ah) - 1)])

        # except AttributeError:
        #     print(' ', 'ошибка lower()', f'msg = {event.object.text}', sep='\n')

        except:
            print('а хуй знает что там не работает')

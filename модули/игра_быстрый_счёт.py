from datetime import datetime
import random
import os

этот_файл = __file__
эта_папка = os.path.dirname(этот_файл)



def запросить_информацию(вопрос):
    ответ = input(f'{вопрос}=')
    return ответ

def отправить_сообщение(сообщение):
    print(сообщение)

def игра_быстрый_счёт(айди_пользователя, имя_пользователя):
    def вычислить_ответ(число1, число2, знак):
        if знак == "+":
            ответ = число1 + число2
        elif знак == "-":
            ответ = число1 - число2
        elif знак == "*":
            ответ = число1 * число2
        return str(ответ)

    def игра():
        число1 = random.randint(1, 10)
        число2 = random.randint(1, 10)
        знак = random.choice(['+', '-', '*'])

        вопрос = f'{число1}{знак}{число2}'
        правильный_ответ = вычислить_ответ(число1, число2, знак)
        ответ_пользователя = запросить_информацию(вопрос)
        return правильный_ответ == ответ_пользователя


    def проверить_падеж(счёт):
        if счёт == 1:
            return "правильный ответ"
        if счёт in [2, 3, 4]:
            return "правильных ответа"
        return "правильных ответов"

    def сформировать_итоговое_сообщение(счёт):
        падеж = проверить_падеж(счёт)
        if счёт == 0:
            return "Ни одного правильного ответа. Как так то?"
        if счёт in range(1, 5):
            return f"Всего {счёт} {падеж}. Ну такое."
        if счёт in range(5, 10):
            return f"Ну неплохо! Целых {счёт} {падеж}."
        if счёт in range(10, 15):
            return f"Весьма неплохо! {счёт} {падеж}."
        if счёт == 15:
            return "Идеальный результат! Все 15 ответов верны!"

    def считать_результаты():
        # если файла с результатамии не существует, то надо вернуть пустой словарь
        if not os.path.exists(f'{эта_папка}\\игра_быстрый_счёт_статистика.txt'):
            return {}

        # открыть файл в режиме чтения
            # указываем путь
            # r - режим чтения
            # encoding - кодировка
        # file - временная переменная, название файла (as - как)
        with open(f'{эта_папка}\\игра_быстрый_счёт_статистика.txt', 'r', encoding='utf-8') as file:
            содержимое = file.read()

        юзеры = содержимое.splitlines()
        результаты = {}

        for юзер in юзеры:
            инфа = юзер.split('///')
            айди = int(инфа[0].split(':', 1)[1])
            имя = инфа[1].split(':', 1)[1]
            количество = int(инфа[2].split(':', 1)[1])
            время = int(инфа[3].split(':', 1)[1])

            результаты[айди] = {
                "имя" : имя,
                "количество" : количество,
                "время" : время
            }
        return результаты
            
            

    def сохранить_результаты(общие_результаты):
        текст = ""
        for айди in общие_результаты:
            результаты = общие_результаты[айди]
            имя = результаты["имя"]
            количество = результаты["количество"]
            время = результаты["время"]
            строка = f'айди:{айди}///имя:{имя}///количество:{количество}///время:{время}\n'
            текст += строка
        
        файл_статистики = f'{эта_папка}\\{"игра_быстрый_счёт_статистика.txt"}'
        with open(f'{эта_папка}\\игра_быстрый_счёт_статистика.txt', 'w', encoding='utf-8') as игра_БС:
            игра_БС.write('')

    def сравнить_результаты(айди):
        pass

    счёт = 0
    время_начала_игры = datetime.now()
    # for i in range(15):
    #     ответ_верен = игра()
    #     if ответ_верен:
    #         счёт += 1
    время_окончания_игры = datetime.now()
    продолжительность_игры = (время_окончания_игры - время_начала_игры).seconds

    общие_результаты = считать_результаты()
    результаты_пользователя = {
            "имя": имя_пользователя,
            "количество": счёт,
            "время": продолжительность_игры
    }

    if айди_пользователя in общие_результаты.keys():
        прошлый_счёт = общие_результаты[айди_пользователя]['количество']
        прошлое_время = общие_результаты[айди_пользователя]['время']
        if счёт > прошлый_счёт or (счёт == прошлый_счёт and продолжительность_игры < прошлое_время):
            общие_результаты[айди_пользователя] = результаты_пользователя
            сохранить_результаты(общие_результаты)
            статус_рекорда = "Рекорд_побит!"
        else:
            статус_рекорда = "Раньше было лучше..."
    else:
        общие_результаты[айди_пользователя] = результаты_пользователя
        сохранить_результаты(общие_результаты)
        статус_рекорда = "Welcome to the Club Buddy!"

    def отсортировать_список(общие_результаты):

        общие_результаты = {
            2: {'имя': 'Никита', 'количество': 15, 'время': 30},
            4: {'имя': 'Степан', 'количество': 12, 'время': 33},
            3: {'имя': 'Михаил', 'количество': 15, 'время': 30},
            1: {'имя': 'Виктор', 'количество': 15, 'время': 29},
        }
        
        список = list(общие_результаты.items())
        список_отсортирован = False
        while not список_отсортирован:
            список_отсортирован = True
            for индекс in range(len(список)):
                if индекс == len(список) - 1:
                    break
                этот_игрок = список[индекс]
                результаты_этого_игрока = этот_игрок[1]
                количество_этого_игрока = результаты_этого_игрока["количество"]
                время_этого_игрока = результаты_этого_игрока["время"]
            
                след_игрок = список[индекс + 1]
                результаты_след_игрока = след_игрок[1]
                количество_след_игрока = результаты_след_игрока["количество"]
                время_след_игрока = результаты_след_игрока["время"]

                if количество_след_игрока > количество_этого_игрока or (количество_этого_игрока == количество_след_игрока and время_след_игрока < время_этого_игрока):
                    список[индекс], список[индекс + 1] = список[индекс + 1], список[индекс]
                    список_отсортирован = False
                    break
        return список
    отсортированный_список = отсортировать_список(общие_результаты)
    print()










    # отправить_сообщение(f'{сформировать_итоговое_сообщение(счёт)} И у на это ушло {продолжительность_игры.seconds} сек.')


игра_быстрый_счёт("+100500", "nqbtw")
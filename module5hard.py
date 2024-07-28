import time 

# Свой YouTube

# Каждый объект класса User должен обладать следующими атрибутами и методами:
# Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число),
# age(возраст, число)

# Каждый объект класса Video должен обладать следующими атрибутами и методами:
# Атриубуты: title(заголовок, строка), duration(продолжительность, секунды),
# time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту,
# bool (False по умолчанию))

# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#  Атриубты: users(список объектов User), videos(список объектов Video),
#  current_user(текущий пользователь, User)


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return str(self.nickname)
class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    current_user = None

    def __init__(self):
        self.users = []
        self.videos = []

    def log_in(self, login, password):
        for usr in self.users:
            if login == str(usr) and hash(password) == hash(usr.password):
                self.current_user = usr
                break
            elif login == str(usr) and hash(password) != hash(usr.password):
                print("Неверный пароль")
                break
            else:
                print("Такого пользователя не существует")

# log_in пытается найти пользователя в users с такими же логином и паролем. Если такой
# пользователь существует, то current_user меняется на найденного. Помните, что
# password передаётся в виде строки, а сравнивается по хэшу.

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        user.nickname = nickname
        user.password = password
        user.age = age

        if not self.users:
            self.users.append(user)
            self.current_user = user
        else:
            for u in self.users:
                if str(user) == str(u):
                    print(f'Пользователь {nickname} уже существует.')
                    break
                else:
                    self.users.append(user)
                    self.current_user = user
                    break

# register добавляет пользователя в список, если пользователя не существует (с таким же nickname).
# Если существует, выводит на экран: "Пользователь {nickname} уже существует".
# После регистрации, вход выполняется автоматически.

    def log_out(self):
        current_user = None

# log_out для сброса текущего пользователя на None

    def add(self, *args):
        for vid in args:
            vid_is_exists = False
            for v in self.videos:
                if vid.title == v.title:
                    print('существует')
                    vid_is_exists = True
                    break
            if vid_is_exists:
                break
            else:
                self.videos.append(vid)

# add принимает неограниченное кол - во объектов класса Video и все добавляет в videos,
# если с таким же названием видео ещё не существует. В противном случае ничего не происходит

    def get_videos(self, word):
        search_list = []
        for vid in self.videos:
            str_lower = str(vid.title).lower()
            if word.lower() in str_lower:
                search_list.append(vid.title)
        if not search_list:
            print('Ничего не найдено')
        else:
            return search_list

# get_videos принимает поисковое слово и возвращает список названий всех видео, содержащих
# поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке
# 'Urban the best'(не учитывать регистр).

    def watch_video(self, title_for_play):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for vid in self.videos:
                if vid.title == title_for_play:
                    if vid.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    else:
                        while vid.time_now < vid.duration:
                            print(vid.time_now + 1, end=' ')
                            vid.time_now += 1
                            time.sleep(1)
                        print('Конец видео')

# принимает название фильма, если не находит точного совпадения(вплоть
# до пробела), то ничего не воспроизводится, если же находит - ведётся
# отчёт в консоль на какой секунде ведётся просмотр.После текущее время просмотра
# данного видео сбрасывается

# Для метода watch_video так же учитывайте следующие особенности:
# Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
# В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре,
# т.к. есть ограничения 18+. Должно выводиться сообщение:
# "Вам нет 18 лет, пожалуйста покиньте страницу"
# После воспроизведения нужно выводить: "Конец видео"


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
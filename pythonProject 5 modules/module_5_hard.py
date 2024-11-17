import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def __str__(self):
        return f"User(nickname='{self.nickname}', age={self.age})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
        return False

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"

    def __repr__(self):
        return str(self)

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        user = next((u for u in self.users if u.nickname == nickname and u.password_hash == hashlib.sha256  #перенос на след строку
                                                                         (password.encode()).hexdigest()), None)
        if user:
            self.current_user = user
            print(f"Успешный вход, {nickname}!")
            return True
        else:
            print("Неверный логин или пароль.")
            return False

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
            return False

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Регистрация успешна, {nickname}!")
        return True

    def log_out(self):
        self.current_user = None
        print("Вы вышли из системы.")

    def add(self, *videos):
        for video in videos:
            if not isinstance(video, Video):
                print("Ошибка: Переданный объект не является видео.")
                continue
            if video.title.lower() in [v.title.lower() for v in self.videos]:
                print(f"Видео '{video.title}' уже существует.")
                continue
            self.videos.append(video)
            print(f"Видео '{video.title}' добавлено.")

    def get_videos(self, search_term):
        return [video.title for video in self.videos if search_term.lower() in video.title.lower()]

    def watch_video(self, video_title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if v.title.lower() == video_title.lower()), None)
        if not video:
            print("Видео не найдено.")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print("Начало видео...")
        for i in range(1, video.duration + 1):
            print(i, end=" ")
            time.sleep(0.1)  # уменьшил задержку
        print("\nКонец видео")
        video.time_now = 0



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





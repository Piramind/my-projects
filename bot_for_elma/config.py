TOKEN = "ваш токен"
SOCCER_API_URL = ""
SOCCER_API_HEADERS = {
    'x-rapidapi-key': "ваш ключ апи",
    'x-rapidapi-host': "football-pro.p.rapidapi.com"
}
SOCCER_API_PARAMS = {
    "tz": "Europe/Moscow",
    "include": "localTeam,visitorTeam"
}
BOT_VERSION = 0.3
# База данных хранит выбранные юзером лиги
BOT_DB_NAME = "users_leagues"
# Тестовые данные поддерживаемых лиг
BOT_LEAGUES = {
    "82": "Немецкая Бундеслига",
    "384": 
}
# Флаги для сообщений, emoji-код
BOT_LEAGUE_FLAGS = {
    "82": ":Germany:",
    "384": ":Italy:",
    "564": ":Spain:",
    "462": ":Portugal:",
    "72": ":Netherlands:",
    "2": ":European_Union:",
    "5": ":trophy:",
    "8": ":England:",
    "301": ":France:",
    "486": ":Russia:"
}

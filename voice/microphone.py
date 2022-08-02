import pyttsx3

engine = pyttsx3.init()     # инициализация движка

# зададим свойства
engine.setProperty('rate', 150)     # скорость речи
engine.setProperty('volume', 0.7)   # громкость (0-1)

engine.say("I can speak!")      # запись фразы в очередь
engine.say("Я могу говорить!")  # запись фразы в очередь

# очистка очереди и воспроизведение текста
engine.runAndWait()

# выполнение кода останавливается, пока весь текст не сказан

"""
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Приветствую тебя, землянин")
    engine.runAndWait()
    engine.stop()
"""

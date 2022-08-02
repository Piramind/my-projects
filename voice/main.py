from vosk import Model, KaldiRecognizer
import os
import pyaudio

model = Model(r"C:/Users/Crond/my-projects/voice/vosk-model-small-ru-0.22") # полный путь к модели
rec = KaldiRecognizer(model, 44100 )
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16, 
    channels=1, 
    rate=44100 , 
    input=True, 
    frames_per_buffer=44100 
)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break

    print(rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult())

print(rec.FinalResult())
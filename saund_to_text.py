import json

from vosk import Model, KaldiRecognizer, SetLogLevel
import os
import wave

# переменная содержащая путь к финальному каталогу
finaly_dir_txt = os.path.abspath(r'D:\code\datashcool\databasetest\finaly_direct')

SetLogLevel(0)

def voice_to_text() -> None:
    # Переменная содержащая список имён файлов обрабатываемого каталога
    talk = os.listdir(os.path.abspath(r"D:\code\datashcool\databasetest\goodformatsaund"))
    # переменная содержащая имя путь к обрабатываемому каталогу
    directory_sound = os.path.abspath(r"D:\code\datashcool\databasetest\goodformatsaund")
    for txtt in talk:
        rap = os.path.abspath(f"{directory_sound}\\{txtt}")
        wf = wave.open(f"{rap}", "rb")
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            print("С аудиофайлом что то не то")
            exit(1)

        model = Model("vosk-model-ru-0.42")
        rec = KaldiRecognizer(model, wf.getframerate())
        with open (os.path.abspath(f'{finaly_dir_txt}\{os.path.splitext(txtt)[0]}.txt'), "w", encoding = "utf-8") as file:
            while True:
                data = wf.readframes(4000)
                if len(data)== 0:
                    break 
                if rec.AcceptWaveform(data):
                    rec_text = json.loads(rec.Result())
                    print(rec_text.get("text"))
                    file.writelines(f"{rec_text.get('text')}\n")
                else:
                    pass


voice_to_text()


# подключаем пакет moviepy
from moviepy.editor import * 
import os 


def video_to_audio_transcription():
    
    #Указываем путь к каталогу обрабатываемых файлов (вынести в конфиг py)
    ferst_directory = os.path.abspath("D:\code\datashcool\databasetest\openvideo")

    #Указываем директорию для сохранения обработанных файлов
    final_directory = os.path.abspath("D:\code\datashcool\databasetest\savesaund")


    # все имена файлов папки сохраняем в список (вынести в конфиг py)
    list_name_origin_files = os.listdir(ferst_directory)

    # выводим список имен файлов
    print('\n'.join(list_name_origin_files))

    # перебираем последовательно все файлы имена которых в списке
    for _name_file in list_name_origin_files:
        print("Конвертируем файл: \n" +
              _name_file)

        # извлекаем аудиодорожку
        audio = AudioFileClip(ferst_directory + "\\" + _name_file)

        # изменяем расширение на mp3 + сохраняем в введенную директорию, меняем пробелы на "_".
        audio.write_audiofile(final_directory + "\\" + (os.path.splitext(_name_file.replace(" ", "_"))[0] + ".mp3"))
    print("Конвертация файлов закончена!")

video_to_audio_transcription()



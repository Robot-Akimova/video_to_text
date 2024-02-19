# Добавить:
#ПЕРЕМЕННЫЕ ДЛЯ НАСТРОЙКИ ВЫХОДНОГО ПАРАМЕТРА ДЕКОДЕРА: (скорость, частота, шумы, каналы, и т.д.)
#функцию sabprocess вместо os.system
#Инфа по ffmpeg 
# https://help.ubuntu.ru/wiki/ffmpeg#%D0%BA%D0%BB%D1%8E%D1%87%D0%B8_%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%B2_ffmpeg_%D0%B4%D0%BB%D1%8F_%D0%B0%D1%83%D0%B4%D0%B8%D0%BE

import os
import pathlib

# Имена переменных
go_ffmpeg_ran = os.path.abspath("D:\code\datashcool\Lib\site-packages\imageio_ffmpeg\\binaries\\ffmpeg-win64-v4.2.2.exe")
save_good_format_saund = os.path.abspath("D:\code\datashcool\databasetest\goodformatsaund")
directory = os.path.abspath("D:\code\datashcool\databasetest\savesaund")
list_mp3 = os.listdir(directory)

os.system("chcp 65001 > nul")

def convert_good_format_sound_to_vosk():   
    for i in list_mp3:
        os.system(f'{go_ffmpeg_ran} -i {directory}\\{i} -c:a pcm_s16le -ar 16000 -ac 1 {save_good_format_saund}\\{i.replace(".mp3", ".wav")}') # "/"{i.replace(".mp3", ".wav")}')
        print(f'{go_ffmpeg_ran} -i {directory}\{i}')
            
# Та же функция на sabprocess
def convert_good_format_sound_to_vosk_sabprocess():
    pass

convert_good_format_sound_to_vosk()




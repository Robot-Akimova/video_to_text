# КОД НЕ РАБОТАЕТ И НАВЕРНОЕ НЕ НУЖЕН
# # https://qna.habr.com/q/859487
# # ffmpeg -f concat -i 1.txt -acodec copy outputfile.wav
# # ничего не получилось пока не нагуглил что список должен быть такого вида:
# # file '01.wav'
# # file '02.wav'

# # Хрень не работает
# import ffmpeg
# import subprocess
# import os
# from goodformat import go_ffmpeg_ran

# write = os.path.abspath("databasetest\\finaly_direct\\workffmpegshit.txt") 
# finaly = os.path.abspath("databasetest\\finaly_direct\\outputfile.wav")
# def concatenation_wav():
#     #путь к директории где лежат файлы
#     one_file_dir_path = os.path.abspath("databasetest\goodformatsaund")
#     #список всех имён директории для записи в txt файл
#     spisok = os.listdir(os.path.abspath("databasetest\goodformatsaund"))
    

#     print('Создание списка файлов для обьединения в один')
#     print("\n".join(spisok))
#     #with open("databasetest\\workffmpegshit.txt", "w") as list_concatenation_wav:
#     list_concatenation_wav = open(os.path.abspath("databasetest\\finaly_direct\\workffmpegshit.txt"), "w")
#     for z in spisok:
        
#         f = os.path.abspath(one_file_dir_path + "\\" + z)
#         print(f)
#         list_concatenation_wav.write("\n" + "file " + os.path.abspath(one_file_dir_path + z))

# concatenation_wav()

# os.system(f"{go_ffmpeg_ran} -f concat -safe 0 -i {write} {finaly}")


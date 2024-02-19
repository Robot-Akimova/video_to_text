# Импорты
from video_to_saund import video_to_audio_transcription
from goodformat import convert_good_format_sound_to_vosk
from saund_to_text import voice_to_text
  
def main():
    # Конвертируем видео в mp3
    video_to_audio_transcription()
    # Преобразовываем mp3 в формат необходимый транскрибации VOSK
    convert_good_format_sound_to_vosk()
    #Добавить функцию обьединения аудиодорожек в одну для исключения множественной
    #загрузки нейросети в процессорную память
    # Обрабатываем звук в текст
    voice_to_text() #  - рабочая функция


main()






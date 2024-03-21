from moviepy.editor import VideoFileClip
from pathlib import Path

files = []

folder = Path('VIDEOS')

for file in folder.iterdir():
    files.append(file)


def converttomp3(mp4file, mp3file):
    video = VideoFileClip(mp4file)
    audio = video.audio
    audio.write_audiofile(mp3file)
    audio.close()
    video.close()


for file in files:
    str_file = str(file)[6:-4]
    converttomp3(f'{str(file)}', f'AUDIOS/{str_file}.mp3')
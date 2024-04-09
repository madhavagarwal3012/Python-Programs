from pytube import YouTube
from pytube.cli import on_progress

link = input('> Enter Link: ')
print()

yt = YouTube(link, on_progress_callback=on_progress)

print(f'Video Title: {yt.title}')
print(f'Number of Views: {yt.views}')
print()

save_path = 'D:/Users/madhav aggarwal/Desktop'

video = yt.streams.get_highest_resolution()
video.download(output_path=save_path)

print('> Video Successfully Downloaded!!')

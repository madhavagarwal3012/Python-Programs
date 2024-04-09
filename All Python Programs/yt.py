from pytube import YouTube
from pytube.cli import on_progress

link = input('> Enter Link: ')
print()

yt = YouTube(link, on_progress_callback=on_progress)

save_path = 'C:/Users/madhav aggarwal/Desktop'

print(f'Video Title: {yt.title}')
print(f'Number of Views: {yt.views}')
print()
print("Enter Choice\n1)Download Video+Audio\n2)Download Only Audio\n3)Download Only Video")
print()

user_command=int(input())
if user_command==1:
    video = yt.streams.get_highest_resolution()
    video.download(output_path=save_path)
    print('> Video(Audio)Successfully Downloaded!!')

elif user_command==2:
    audio = yt.streams.filter(only_audio=True).all
    audio[0].download(output_path=save_path)
    print('> Audio Successfully Downloaded!!')

else:
    user_command==3
    video_without_audio = yt.streams.all()
    video_without_audio[2].download(output_path=save_path)
    print('> Video Successfully Downloaded!!')
    

    

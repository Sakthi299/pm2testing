#pip install pafy
#pip install youtube_dl
import pafy

url = "https://youtu.be/oEJdRYRCZ-0"

video = pafy.new(url)
print(video.title)
print(video.likes)





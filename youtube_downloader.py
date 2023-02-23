import sys
from pytube import YouTube

url = sys.argv[1]
yt = YouTube(url)

print(yt.streams.filter(progressive=True))

stream = yt.streams.get_highest_resolution()
stream.download()

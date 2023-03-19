from pytube import YouTube

link = input("Enter a youtube video's URL")

yt = Youtube(link)
yt.streams.first().download()

print("downloaded", link)
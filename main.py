import pytubefix as pytube

url = input("Video linkini yapıştırın: ")
yt = pytube.YouTube(url)

print("İndiriliyor...")
yt.streams.get_highest_resolution().download()
print("Bitti!")
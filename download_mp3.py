## you need to install youtube_dl << pip install youtube_dl >>
from __future__ import unicode_literals
import youtube_dl

## The function that downloads video in mp3 format
def download(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
            
## calling the function and passing the url of the youtube video as parameter
url = input('your url :')
download(url)

